"""Генерирует основной код SDK из docs/swagger.json."""

from __future__ import annotations

import json
import keyword
import re
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "docs" / "swagger.json").read_text(encoding="utf-8"))
DEFINITIONS = SPEC.get("definitions", {})
PATHS = SPEC.get("paths", {})

RESERVED = set(keyword.kwlist) | {
    "from",
    "class",
    "def",
    "return",
    "global",
    "pass",
    "id",
    "list",
    "dict",
    "str",
    "type",
}

TAG_MODULES = {
    "Accounts": "accounts",
    "Devices": "devices",
    "GPON": "gpon",
    "Gather": "gather",
    "Maps": "maps",
    "Ring Manager": "ring_manager",
    "Tools": "tools",
}
TAG_CLASSES = {
    "Accounts": "AccountsResource",
    "Devices": "DevicesResource",
    "GPON": "GponResource",
    "Gather": "GatherResource",
    "Maps": "MapsResource",
    "Ring Manager": "RingManagerResource",
    "Tools": "ToolsResource",
}
TAG_PREFIX = {
    "Accounts": "accounts",
    "Devices": "devices",
    "GPON": "gpon",
    "Gather": "gather",
    "Maps": "maps",
    "Ring Manager": "ring_manager",
    "Tools": "tools",
}

MODEL_MODULES = {
    "accounts": {"User", "UserPermissions"},
    "devices": {
        "Devices",
        "BulkDeviceCommandExecution",
        "BulkDeviceCommandExecutionResult",
        "BulkCommandTaskResult",
        "BulkCommandTaskStatus",
        "ExecuteBulkDeviceCommandRequest",
        "BulkCommandLaunchDevice",
        "BulkCommandLaunchResponse",
        "InterfacesComments",
        "BrassSession",
        "CutBrasSession",
        "BrasSession",
        "BrasPairSessionResult",
        "InterfaceWorkload",
        "DevicesInterfaceWorkload",
        "DevicesInterfaceWorkloadResult",
        "DeviceAuthGroup",
        "DeviceGroup",
        "DevicesDetail",
        "DevicesDetailUpdate",
        "UserDeviceAction",
        "ChangeDescriptionRequest",
        "ChangeDescription",
        "ADSLProfile",
        "DeviceCommands",
        "ConfigFile",
        "DeviceInfo",
        "PortDetailInfo",
        "InterfaceDetailInfo",
        "LinkToAnotherDevice",
        "InterfaceComment",
        "InterfaceInfo",
        "InterfacesList",
        "MacList",
        "MacListResult",
        "DeviceMedia",
        "DevicePoolStatuses",
        "PortControl",
        "PoEPortStatus",
        "DeviceViewings",
        "DeviceVlanPort",
        "DeviceVlan",
    },
    "gather": {
        "MacGatherScanTask",
        "MacGatherStatus",
        "Nodes",
        "Edges",
        "MacTraceroute",
    },
    "gpon": {
        "BuildingAddress",
        "Address",
        "End3",
        "CommonCustomerSerializer",
        "SubscriberHouseOLTState",
        "SubscriberConnection",
        "CustomerDetail",
        "OLTSubscriber",
        "UpdateSubscriberData",
        "CreateCustomerSerializer",
        "SubscriberData",
        "OLTState",
        "WriteOnlyHouseBAddress",
        "CreateHouseOLTState",
        "End3Writer",
        "End3Create",
        "End3CreateList",
        "CreateTechData",
        "HouseOLTState",
        "ViewHouseBTechData",
        "ShortViewSubscriberConnection",
        "TechCapability",
        "End3TechCapability",
        "AddEnd3ToHouseOLTState",
        "StructuresHouseOLTState",
        "UpdateHouseOLTState",
        "UpdateRetrieveOLTState",
        "ViewOLTStatesTechData",
    },
    "maps": {"Map", "Layer", "MapDetail", "MapLayer"},
    "ring_manager": {"ShortPointRing", "AccessRing", "TransportRing"},
    "tools": {
        "Comment",
        "FoundInterface",
        "FoundDeviceInterfaces",
        "SearchInterfaceByDescResult",
        "GetVendor",
        "GetVlanDesc",
        "NodeFont",
        "TracerouteNode",
        "TracerouteEdge",
        "VlanTraceroute",
    },
}


def snake(value: str) -> str:
    """Преобразует строку в snake_case."""

    value = value.replace("-", "_").replace("/", "_")
    value = re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()
    value = re.sub(r"[^0-9a-zA-Z_]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    if not value:
        value = "value"
    if value[0].isdigit():
        value = f"field_{value}"
    return value


def py_name(name: str) -> str:
    """Возвращает безопасное Python-имя."""

    result = snake(name)
    if result in RESERVED:
        result += "_"
    return result


def method_name(name: str) -> str:
    """Возвращает безопасное имя метода."""

    result = snake(name)
    if keyword.iskeyword(result):
        result += "_"
    return result


def class_name(name: str) -> str:
    """Возвращает безопасное имя класса."""

    return re.sub(r"[^0-9a-zA-Z_]", "", name)


def schema_type(schema: dict, *, required: bool = True) -> str:
    """Преобразует swagger schema в Python type expression."""

    if not schema:
        typ = "Any"
    elif "$ref" in schema:
        typ = class_name(schema["$ref"].split("/")[-1])
    else:
        stype = schema.get("type")
        if stype == "array":
            typ = f"list[{schema_type(schema.get('items', {}), required=True)}]"
        elif stype == "integer":
            typ = "int"
        elif stype == "number":
            typ = "float"
        elif stype == "boolean":
            typ = "bool"
        elif stype == "string":
            typ = "str"
        elif stype == "object":
            props = schema.get("properties")
            if props and {"count", "results"}.issubset(props):
                results = props.get("results", {})
                item_type = "Any"
                if results.get("type") == "array":
                    item_type = schema_type(results.get("items", {}), required=True)
                typ = f"Page[{item_type}]"
            elif "additionalProperties" in schema:
                typ = f"dict[str, {schema_type(schema.get('additionalProperties') or {}, required=True)}]"
            else:
                typ = "dict[str, Any]"
        else:
            typ = "Any"
    if (not required or schema.get("x-nullable")) and " | None" not in typ:
        typ = f"{typ} | None"
    return typ


def resource_type_expr(type_expr: str) -> str:
    """Адаптирует type expression для resource-классов."""

    return type_expr.replace("list[", "_list[")


def response_type(operation: dict) -> tuple[str, str]:
    """Возвращает type hint и response_model для операции."""

    responses = operation.get("responses", {})
    for code in ["200", "201", "202", "204"]:
        response = responses.get(code)
        if response is None:
            continue
        schema = response.get("schema")
        if code == "204":
            return "None", "None"
        if not schema:
            return "Any", "None"
        typ = resource_type_expr(schema_type(schema))
        return typ, typ
    return "Any", "None"


def body_param(operation: dict) -> tuple[str | None, str, bool]:
    """Возвращает body-параметр операции."""

    for param in operation.get("parameters", []):
        if param.get("in") == "body":
            name = py_name(param.get("name") or "data")
            typ = schema_type(param.get("schema") or {})
            return name, typ, bool(param.get("required"))
    return None, "None", False


def param_type(param: dict) -> str:
    """Возвращает type hint параметра."""

    schema = {"type": param.get("type", "string")}
    if param.get("x-nullable"):
        schema["x-nullable"] = True
    return schema_type(schema, required=bool(param.get("required")))


def operation_method_name(tag: str, operation_id: str, used: set[str]) -> str:
    """Строит имя метода ресурса по operationId."""

    sanitized = snake(operation_id)
    prefix = TAG_PREFIX[tag]
    rest = sanitized[len(prefix) + 1 :] if sanitized.startswith(prefix + "_") else sanitized
    suffixes = [
        ("partial_update", "patch"),
        ("update", "update"),
        ("delete", "delete"),
        ("create", "create"),
        ("read", "get"),
        ("list", "list"),
    ]
    name = rest
    for suffix, verb in suffixes:
        if rest == suffix:
            name = verb
            break
        marker = "_" + suffix
        if rest.endswith(marker):
            subject = rest[: -len(marker)]
            name = f"{verb}_{subject}" if subject else verb
            break
    name = method_name(name)
    base = name
    counter = 2
    while name in used:
        name = f"{base}_{counter}"
        counter += 1
    used.add(name)
    return name


def all_params(path_item: dict, operation: dict) -> list[dict]:
    """Возвращает path-level и operation-level параметры."""

    return list(path_item.get("parameters") or []) + list(operation.get("parameters") or [])


def build_core_files(files: dict[str, str]) -> None:
    """Добавляет вручную написанные базовые модули."""

    files["ecstasy_sdk/models/base.py"] = dedent('''\
        """Базовые Pydantic-модели SDK."""

        from pydantic import BaseModel, ConfigDict


        class EcstasyModel(BaseModel):
            """Базовая модель SDK с мягкой совместимостью со swagger."""

            model_config = ConfigDict(
                populate_by_name=True,
                extra="allow",
                arbitrary_types_allowed=True,
            )
        ''')
    files["ecstasy_sdk/models/common.py"] = dedent('''\
        """Общие модели SDK."""

        from typing import Any

        from ecstasy_sdk.models.base import EcstasyModel


        class Page[T](EcstasyModel):
            """Страница результатов DRF pagination."""

            count: int
            next: str | None = None
            previous: str | None = None
            results: list[T]


        class RawResponse(EcstasyModel):
            """Контейнер для неописанного swagger ответа."""

            data: dict[str, Any] | list[Any] | str | bytes | None = None


        class EmptyResponse(EcstasyModel):
            """Пустой ответ API."""

            pass
        ''')
    files["ecstasy_sdk/config.py"] = dedent('''\
        """Конфигурация клиента Ecstasy API."""

        from typing import Any

        import httpx
        from pydantic import BaseModel, ConfigDict, SecretStr, field_validator


        class EcstasyConfig(BaseModel):
            """Конфигурация клиента Ecstasy API."""

            model_config = ConfigDict(arbitrary_types_allowed=True)

            base_url: str
            token: SecretStr
            api_base_path: str = "/api/v1"
            timeout: float | httpx.Timeout = 30.0
            verify: bool = True
            follow_redirects: bool = False
            user_agent: str = "ecstasy-sdk"

            @field_validator("base_url")
            @classmethod
            def normalize_base_url(cls, value: Any) -> str:
                """Нормализует базовый URL без завершающего слеша."""

                return str(value).rstrip("/")

            @field_validator("api_base_path")
            @classmethod
            def normalize_api_base_path(cls, value: str) -> str:
                """Нормализует базовый путь API."""

                value = value.strip() or "/api/v1"
                if not value.startswith("/"):
                    value = f"/{value}"
                return value.rstrip("/")

            @property
            def authorization_header(self) -> str:
                """Возвращает значение заголовка Authorization с префиксом Token."""

                token = self.token.get_secret_value().strip()
                if token.lower().startswith("token "):
                    return token
                return f"Token {token}"
        ''')
    files["ecstasy_sdk/exceptions.py"] = dedent('''\
        """Исключения ecstasy-sdk."""

        from typing import Any


        class EcstasyError(Exception):
            """Базовая ошибка SDK."""


        class EcstasyConfigError(EcstasyError):
            """Ошибка конфигурации SDK."""


        class EcstasyTransportError(EcstasyError):
            """Ошибка транспортного уровня."""


        class EcstasyTimeoutError(EcstasyTransportError):
            """Ошибка таймаута HTTP-запроса."""


        class EcstasyAPIError(EcstasyError):
            """Ошибка, полученная от Ecstasy API."""

            def __init__(
                self,
                message: str,
                *,
                status_code: int,
                method: str,
                url: str,
                request_id: str | None = None,
                response_text: str = "",
                response_json: dict[str, Any] | list[Any] | None = None,
            ) -> None:
                """Инициализирует ошибку API."""

                super().__init__(message)
                self.status_code = status_code
                self.method = method
                self.url = url
                self.request_id = request_id
                self.response_text = response_text
                self.response_json = response_json


        class EcstasyBadRequestError(EcstasyAPIError):
            """Ошибка 400 Bad Request."""


        class EcstasyUnauthorizedError(EcstasyAPIError):
            """Ошибка 401 Unauthorized."""


        class EcstasyForbiddenError(EcstasyAPIError):
            """Ошибка 403 Forbidden."""


        class EcstasyNotFoundError(EcstasyAPIError):
            """Ошибка 404 Not Found."""


        class EcstasyConflictError(EcstasyAPIError):
            """Ошибка 409 Conflict."""


        class EcstasyValidationError(EcstasyAPIError):
            """Ошибка валидации API."""


        class EcstasyServerError(EcstasyAPIError):
            """Серверная ошибка API."""


        class EcstasyResponseValidationError(EcstasyError):
            """Ошибка валидации ответа API через Pydantic."""
        ''')
    files["ecstasy_sdk/filters.py"] = dedent('''\
        """Query-фильтры SDK."""

        from ecstasy_sdk.models.base import EcstasyModel


        class DeviceListFilters(EcstasyModel):
            """Фильтры списка устройств."""

            group: str | None = None
            vendor: str | None = None
            model: str | None = None
            ip: str | None = None
            serial_number: str | None = None
            os_version: str | None = None
            port_scan_protocol: str | None = None
            cmd_protocol: str | None = None
            active: str | bool | None = None
            collect_interfaces: str | bool | None = None
            collect_mac_addresses: str | bool | None = None
            collect_vlan_info: str | bool | None = None
            collect_configurations: str | bool | None = None
            connection_pool_size: str | int | None = None
            name: str | None = None
            return_fields: str | list[str] | None = None


        class InterfaceListFilters(EcstasyModel):
            """Фильтры списка интерфейсов устройства."""

            current_status: str | bool | None = None
            vlans: str | None = None
            add_links: str | bool | None = None
            add_comments: str | bool | None = None
            add_zabbix_graph: str | bool | None = None


        class End3TechDataFilters(EcstasyModel):
            """Фильтры технических данных End3."""

            house: str | None = None
            block: str | None = None
            tech_capability_status: str | None = None
            street: str | None = None
        ''')
    files["ecstasy_sdk/pagination.py"] = dedent('''\
        """Утилиты пагинации SDK."""

        from ecstasy_sdk.models.common import Page

        __all__ = ["Page"]
        ''')


def build_transport_files(files: dict[str, str]) -> None:
    """Добавляет HTTP-транспорт."""

    files["ecstasy_sdk/transport/base.py"] = dedent('''\
        """Общая логика HTTP-транспорта."""

        from collections.abc import Mapping
        from typing import Any
        from urllib.parse import quote

        import httpx
        from pydantic import BaseModel, TypeAdapter, ValidationError

        from ecstasy_sdk.config import EcstasyConfig
        from ecstasy_sdk.exceptions import (
            EcstasyAPIError,
            EcstasyBadRequestError,
            EcstasyConflictError,
            EcstasyForbiddenError,
            EcstasyNotFoundError,
            EcstasyResponseValidationError,
            EcstasyServerError,
            EcstasyUnauthorizedError,
            EcstasyValidationError,
        )


        class BaseTransport:
            """Базовая логика транспорта Ecstasy API."""

            def __init__(self, config: EcstasyConfig) -> None:
                """Сохраняет конфигурацию транспорта."""

                self.config = config

            @property
            def headers(self) -> dict[str, str]:
                """Возвращает базовые заголовки HTTP-запросов."""

                return {
                    "Accept": "application/json",
                    "Authorization": self.config.authorization_header,
                    "User-Agent": self.config.user_agent,
                }

            def build_url(self, path: str, path_params: Mapping[str, Any] | None = None) -> str:
                """Собирает полный URL с path-параметрами."""

                rendered_path = path
                for key, value in (path_params or {}).items():
                    rendered_path = rendered_path.replace("{" + key + "}", quote(str(value), safe=""))
                return f"{self.config.base_url}{self.config.api_base_path}{rendered_path}"

            def serialize_query(self, query: Mapping[str, Any] | BaseModel | None) -> dict[str, Any] | None:
                """Сериализует query-параметры."""

                if query is None:
                    return None
                if isinstance(query, BaseModel):
                    raw = query.model_dump(mode="json", by_alias=True, exclude_none=True)
                else:
                    raw = {key: value for key, value in query.items() if value is not None}
                result: dict[str, Any] = {}
                for key, value in raw.items():
                    if isinstance(value, list):
                        result[key] = ",".join(str(item) for item in value)
                    else:
                        result[key] = value
                return result or None

            def serialize_body(self, body: BaseModel | Mapping[str, Any] | None) -> Any:
                """Сериализует тело запроса."""

                if body is None:
                    return None
                if isinstance(body, BaseModel):
                    return body.model_dump(mode="json", by_alias=True, exclude_none=False)
                return dict(body)

            def parse_response(self, response: httpx.Response, response_model: Any = None) -> Any:
                """Парсит и валидирует ответ API."""

                if response.status_code == 204:
                    return None
                content_type = response.headers.get("content-type", "").lower()
                if "application/json" in content_type:
                    payload: Any = response.json()
                elif content_type.startswith("text/") or "html" in content_type:
                    payload = response.text
                elif response.content:
                    payload = response.content
                else:
                    payload = None
                if response_model is None:
                    return payload
                try:
                    return TypeAdapter(response_model).validate_python(payload)
                except ValidationError as exc:
                    raise EcstasyResponseValidationError(str(exc)) from exc

            def raise_for_status(self, response: httpx.Response) -> None:
                """Преобразует HTTP-ошибки в исключения SDK."""

                if response.status_code < 400:
                    return
                response_json = None
                try:
                    response_json = response.json()
                except ValueError:
                    response_json = None
                message = f"Ecstasy API returned HTTP {response.status_code}"
                error_class: type[EcstasyAPIError]
                if response.status_code == 400:
                    error_class = EcstasyBadRequestError
                elif response.status_code == 401:
                    error_class = EcstasyUnauthorizedError
                elif response.status_code == 403:
                    error_class = EcstasyForbiddenError
                elif response.status_code == 404:
                    error_class = EcstasyNotFoundError
                elif response.status_code == 409:
                    error_class = EcstasyConflictError
                elif response.status_code == 422:
                    error_class = EcstasyValidationError
                elif response.status_code >= 500:
                    error_class = EcstasyServerError
                else:
                    error_class = EcstasyAPIError
                raise error_class(
                    message,
                    status_code=response.status_code,
                    method=response.request.method,
                    url=str(response.request.url),
                    request_id=response.headers.get("x-request-id"),
                    response_text=response.text,
                    response_json=response_json,
                )
        ''')
    files["ecstasy_sdk/transport/sync.py"] = dedent('''\
        """Синхронный HTTP-транспорт."""

        from collections.abc import Mapping
        from typing import Any

        import httpx
        from pydantic import BaseModel

        from ecstasy_sdk.config import EcstasyConfig
        from ecstasy_sdk.exceptions import EcstasyTimeoutError, EcstasyTransportError
        from ecstasy_sdk.transport.base import BaseTransport


        class SyncTransport(BaseTransport):
            """Синхронный транспорт Ecstasy API."""

            def __init__(self, config: EcstasyConfig, client: httpx.Client | None = None) -> None:
                """Создает синхронный HTTP-клиент."""

                super().__init__(config)
                self.client = client or httpx.Client(
                    timeout=config.timeout,
                    verify=config.verify,
                    follow_redirects=config.follow_redirects,
                    headers=self.headers,
                )

            def request(
                self,
                method: str,
                path: str,
                *,
                path_params: Mapping[str, Any] | None = None,
                query: Mapping[str, Any] | BaseModel | None = None,
                body: BaseModel | Mapping[str, Any] | None = None,
                response_model: Any = None,
            ) -> Any:
                """Выполняет синхронный HTTP-запрос к Ecstasy API."""

                url = self.build_url(path, path_params)
                try:
                    response = self.client.request(
                        method,
                        url,
                        headers=self.headers,
                        params=self.serialize_query(query),
                        json=self.serialize_body(body) if body is not None else None,
                    )
                except httpx.TimeoutException as exc:
                    raise EcstasyTimeoutError(str(exc)) from exc
                except httpx.RequestError as exc:
                    raise EcstasyTransportError(str(exc)) from exc
                self.raise_for_status(response)
                return self.parse_response(response, response_model)

            def close(self) -> None:
                """Закрывает HTTP-клиент."""

                self.client.close()
        ''')
    files["ecstasy_sdk/transport/async_.py"] = dedent('''\
        """Асинхронный HTTP-транспорт."""

        from collections.abc import Mapping
        from typing import Any

        import httpx
        from pydantic import BaseModel

        from ecstasy_sdk.config import EcstasyConfig
        from ecstasy_sdk.exceptions import EcstasyTimeoutError, EcstasyTransportError
        from ecstasy_sdk.transport.base import BaseTransport


        class AsyncTransport(BaseTransport):
            """Асинхронный транспорт Ecstasy API."""

            def __init__(self, config: EcstasyConfig, client: httpx.AsyncClient | None = None) -> None:
                """Создает асинхронный HTTP-клиент."""

                super().__init__(config)
                self.client = client or httpx.AsyncClient(
                    timeout=config.timeout,
                    verify=config.verify,
                    follow_redirects=config.follow_redirects,
                    headers=self.headers,
                )

            async def request(
                self,
                method: str,
                path: str,
                *,
                path_params: Mapping[str, Any] | None = None,
                query: Mapping[str, Any] | BaseModel | None = None,
                body: BaseModel | Mapping[str, Any] | None = None,
                response_model: Any = None,
            ) -> Any:
                """Выполняет асинхронный HTTP-запрос к Ecstasy API."""

                url = self.build_url(path, path_params)
                try:
                    response = await self.client.request(
                        method,
                        url,
                        headers=self.headers,
                        params=self.serialize_query(query),
                        json=self.serialize_body(body) if body is not None else None,
                    )
                except httpx.TimeoutException as exc:
                    raise EcstasyTimeoutError(str(exc)) from exc
                except httpx.RequestError as exc:
                    raise EcstasyTransportError(str(exc)) from exc
                self.raise_for_status(response)
                return self.parse_response(response, response_model)

            async def aclose(self) -> None:
                """Закрывает HTTP-клиент."""

                await self.client.aclose()
        ''')
    files["ecstasy_sdk/transport/__init__.py"] = dedent('''\
        """HTTP-транспорты SDK."""

        from ecstasy_sdk.transport.async_ import AsyncTransport
        from ecstasy_sdk.transport.sync import SyncTransport

        __all__ = ["AsyncTransport", "SyncTransport"]
        ''')


def build_model_files(files: dict[str, str]) -> list[str]:
    """Генерирует Pydantic-схемы."""

    schema_lines = [
        '"""Pydantic-схемы, сгенерированные из docs/swagger.json."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, cast",
        "",
        "from pydantic import Field",
        "",
        "from ecstasy_sdk.models.base import EcstasyModel",
        "from ecstasy_sdk.models.common import Page",
        "",
    ]
    all_model_names = []
    for name, schema in DEFINITIONS.items():
        cls = class_name(name)
        all_model_names.append(cls)
        schema_lines.append(f"class {cls}(EcstasyModel):")
        schema_lines.append(f'    """Схема `{name}` из Ecstasy API."""')
        props = schema.get("properties") or {}
        required = set(schema.get("required") or [])
        if not props:
            schema_lines.append("    pass")
            schema_lines.append("")
            continue
        for prop_name, prop_schema in props.items():
            field_name = py_name(prop_name)
            typ = schema_type(prop_schema, required=prop_name in required)
            alias_needed = field_name != prop_name
            default = "..." if prop_name in required else "None"
            if alias_needed:
                schema_lines.append(f"    {field_name}: {typ} = Field({default}, alias={prop_name!r})")
            elif prop_name in required:
                schema_lines.append(f"    {field_name}: {typ}")
            else:
                schema_lines.append(f"    {field_name}: {typ} = None")
        schema_lines.append("")
    schema_lines.append("for _model in [")
    for name in all_model_names:
        schema_lines.append(f"    {name},")
    schema_lines.append("]:")
    schema_lines.append("    cast(type[EcstasyModel], _model).model_rebuild()")
    schema_lines.append("")
    schema_lines.append("__all__ = [")
    for name in all_model_names:
        schema_lines.append(f"    {name!r},")
    schema_lines.append("]")
    schema_lines.append("")
    files["ecstasy_sdk/models/schemas.py"] = "\n".join(schema_lines)

    for module, names in MODEL_MODULES.items():
        exports = [class_name(name) for name in DEFINITIONS if name in names]
        lines = [f'"""Модели SDK для группы `{module}`."""', "", "from ecstasy_sdk.models.schemas import ("]
        for name in exports:
            lines.append(f"    {name},")
        lines.extend([")", "", "__all__ = ["])
        for name in exports:
            lines.append(f"    {name!r},")
        lines.extend(["]", ""])
        files[f"ecstasy_sdk/models/{module}.py"] = "\n".join(lines)

    init_lines = [
        '"""Pydantic-модели ecstasy-sdk."""',
        "",
        "from ecstasy_sdk.models.common import EmptyResponse, Page, RawResponse",
        "from ecstasy_sdk.models.schemas import (",
    ]
    for name in all_model_names:
        init_lines.append(f"    {name},")
    init_lines.extend([")", "", "__all__ = [", '    "Page",', '    "RawResponse",', '    "EmptyResponse",'])
    for name in all_model_names:
        init_lines.append(f"    {name!r},")
    init_lines.extend(["]", ""])
    files["ecstasy_sdk/models/__init__.py"] = "\n".join(init_lines)
    return all_model_names


def build_resource_files(files: dict[str, str]) -> int:
    """Генерирует sync и async resource-клиенты."""

    ops_by_tag = {tag: [] for tag in TAG_MODULES}  # type: ignore
    for path, path_item in PATHS.items():
        for method, operation in path_item.items():
            if method == "parameters":
                continue
            tag = (operation.get("tags") or ["Other"])[0]
            if tag in ops_by_tag:
                ops_by_tag[tag].append((path, method.upper(), path_item, operation))

    model_names = {class_name(name) for name in DEFINITIONS}
    model_names.add("Page")

    for tag, operations in ops_by_tag.items():
        module = TAG_MODULES[tag]
        class_base = TAG_CLASSES[tag]
        for is_async in [False, True]:
            class_name_res = "Async" + class_base if is_async else class_base
            used_model_names: set[str] = set()
            for _, _, _, operation in operations:
                body_name, body_type, _ = body_param(operation)
                return_hint, response_expr = response_type(operation)
                type_text = (
                    f"{body_type} {return_hint} {response_expr}"
                    if body_name
                    else f"{return_hint} {response_expr}"
                )
                used_model_names.update(name for name in model_names if name in type_text)
            model_import = (
                "from ecstasy_sdk.models import (\n"
                + "".join(f"    {name},\n" for name in sorted(used_model_names))
                + ")\n"
            )
            transport_import = (
                "from ecstasy_sdk.transport.async_ import AsyncTransport"
                if is_async
                else "from ecstasy_sdk.transport.sync import SyncTransport"
            )
            lines = [
                "from __future__ import annotations\n\n"
                "from builtins import list as _list\n"
                "from typing import Any\n\n"
                f"{model_import}{transport_import}\n"
            ]
            transport_type = "AsyncTransport" if is_async else "SyncTransport"
            lines.append(f"class {class_name_res}:")
            lines.append(f'    """Ресурсный клиент Ecstasy API для группы `{tag}`."""')
            lines.append("")
            lines.append(f"    def __init__(self, transport: {transport_type}) -> None:")
            lines.append('        """Сохраняет транспорт ресурса."""')
            lines.append("")
            lines.append("        self._transport = transport")
            lines.append("")
            used: set[str] = set()
            for path, method, path_item, operation in operations:
                operation_id = operation.get("operationId") or f"{method.lower()}_{path}"
                method_name = operation_method_name(tag, operation_id, used)
                params = all_params(path_item, operation)
                path_params = [param for param in params if param.get("in") == "path"]
                query_params = [param for param in params if param.get("in") == "query"]
                body_name, body_type, body_required = body_param(operation)
                body_type = resource_type_expr(body_type)
                return_hint, response_expr = response_type(operation)
                signature_parts = ["self"]
                for param in path_params:
                    signature_parts.append(f"{py_name(param['name'])}: {param_type(param)}")
                if body_name:
                    if body_required:
                        signature_parts.append(f"{body_name}: {body_type}")
                    else:
                        signature_parts.append(f"{body_name}: {body_type} = None")
                if query_params:
                    signature_parts.append("*")
                    for param in query_params:
                        query_type = param_type(param)
                        if " | None" not in query_type:
                            query_type = f"{query_type} | None"
                        signature_parts.append(f"{py_name(param['name'])}: {query_type} = None")
                signature = ", ".join(signature_parts)
                async_prefix = "async " if is_async else ""
                lines.append(f"    {async_prefix}def {method_name}({signature}) -> {return_hint}:")
                lines.append('        """Выполняет операцию Ecstasy API.')
                lines.append("")
                lines.append(f"        operationId: {operation_id}.")
                lines.append('        """')
                lines.append("")
                if path_params:
                    entries = ", ".join(
                        f"{param['name']!r}: {py_name(param['name'])}" for param in path_params
                    )
                    lines.append(f"        path_params = {{{entries}}}")
                else:
                    lines.append("        path_params = None")
                if query_params:
                    entries = ", ".join(
                        f"{param['name']!r}: {py_name(param['name'])}" for param in query_params
                    )
                    lines.append(f"        query = {{{entries}}}")
                else:
                    lines.append("        query = None")
                call = (
                    f"self._transport.request({method!r}, {path!r}, path_params=path_params, query=query, "
                    f"body={body_name if body_name else 'None'}, response_model={response_expr})"
                )
                if is_async:
                    lines.append(f"        return await {call}")
                else:
                    lines.append(f"        return {call}")
                lines.append("")
            aliases = []
            if tag == "Accounts":
                aliases = [
                    ("get_myself", "list_myself"),
                    ("get_permissions", "list_myself_permissions"),
                    ("get_oidc_config", "list_oidc_config"),
                ]
            elif tag == "Devices":
                aliases = [
                    ("list_all", "list_all"),
                    ("get_by_zabbix", "get_by_zabbix"),
                    ("list_interfaces", "list_interfaces"),
                ]
            elif tag == "Tools":
                aliases = [
                    ("get_vlan_traceroute", "list_vlan_traceroute"),
                    ("get_vlan_desc", "list_vlan_desc"),
                    ("find_by_desc", "list_find_by_desc"),
                ]
            for alias, target in aliases:
                if alias == target or target not in used or alias in used:
                    continue
                lines.append(f"    {alias} = {target}")
                lines.append("")
            target_dir = "async_resources" if is_async else "resources"
            files[f"ecstasy_sdk/{target_dir}/{module}.py"] = "\n".join(lines)

    for package in ["resources", "async_resources"]:
        is_async = package == "async_resources"
        lines = [f'"""{"Асинхронные" if is_async else "Синхронные"} ресурсные клиенты SDK."""', ""]
        all_exports = []
        for tag, module in TAG_MODULES.items():
            cls = ("Async" if is_async else "") + TAG_CLASSES[tag]
            lines.append(f"from ecstasy_sdk.{package}.{module} import {cls}")
            all_exports.append(cls)
        lines.extend(["", "__all__ = ["])
        for cls in all_exports:
            lines.append(f"    {cls!r},")
        lines.extend(["]", ""])
        files[f"ecstasy_sdk/{package}/__init__.py"] = "\n".join(lines)

    return sum(len(value) for value in ops_by_tag.values())


def build_client_files(files: dict[str, str]) -> None:
    """Добавляет верхнеуровневые клиенты."""

    sync_lines = [
        '"""Синхронный клиент Ecstasy API."""',
        "",
        "import httpx",
        "from pydantic import SecretStr",
        "",
        "from ecstasy_sdk.config import EcstasyConfig",
    ]
    for tag, module in TAG_MODULES.items():
        sync_lines.append(f"from ecstasy_sdk.resources.{module} import {TAG_CLASSES[tag]}")
    sync_lines.append("from ecstasy_sdk.transport.sync import SyncTransport")
    sync_lines.extend(["", "", "class EcstasyClient:", '    """Синхронный клиент Ecstasy API."""', ""])
    sync_lines.append(
        '    def __init__(self, base_url: str, token: str, *, api_base_path: str = "/api/v1", '
        "timeout: float | httpx.Timeout = 30.0, verify: bool = True, follow_redirects: bool = False, "
        'user_agent: str = "ecstasy-sdk", http_client: httpx.Client | None = None) -> None:'
    )
    sync_lines.append('        """Создает синхронный клиент Ecstasy API."""')
    sync_lines.append("")
    sync_lines.append(
        "        self.config = EcstasyConfig(base_url=base_url, token=SecretStr(token), api_base_path=api_base_path, "
        "timeout=timeout, verify=verify, follow_redirects=follow_redirects, user_agent=user_agent)"
    )
    sync_lines.append("        self._transport = SyncTransport(self.config, client=http_client)")
    for tag, module in TAG_MODULES.items():
        sync_lines.append(f"        self.{module} = {TAG_CLASSES[tag]}(self._transport)")
    sync_lines.extend(
        [
            "",
            '    def __enter__(self) -> "EcstasyClient":',
            '        """Входит в sync context manager."""',
            "",
            "        return self",
            "",
            "    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:",
            '        """Закрывает клиент при выходе из context manager."""',
            "",
            "        self.close()",
            "",
            "    def close(self) -> None:",
            '        """Закрывает HTTP-сессию клиента."""',
            "",
            "        self._transport.close()",
            "",
        ]
    )
    files["ecstasy_sdk/client.py"] = "\n".join(sync_lines)

    async_lines = [
        '"""Асинхронный клиент Ecstasy API."""',
        "",
        "from types import TracebackType",
        "",
        "import httpx",
        "from pydantic import SecretStr",
        "",
        "from ecstasy_sdk.config import EcstasyConfig",
    ]
    for tag, module in TAG_MODULES.items():
        async_lines.append(f"from ecstasy_sdk.async_resources.{module} import Async{TAG_CLASSES[tag]}")
    async_lines.append("from ecstasy_sdk.transport.async_ import AsyncTransport")
    async_lines.extend(["", "", "class AsyncEcstasyClient:", '    """Асинхронный клиент Ecstasy API."""', ""])
    async_lines.append(
        '    def __init__(self, base_url: str, token: str, *, api_base_path: str = "/api/v1", '
        "timeout: float | httpx.Timeout = 30.0, verify: bool = True, follow_redirects: bool = False, "
        'user_agent: str = "ecstasy-sdk", http_client: httpx.AsyncClient | None = None) -> None:'
    )
    async_lines.append('        """Создает асинхронный клиент Ecstasy API."""')
    async_lines.append("")
    async_lines.append(
        "        self.config = EcstasyConfig(base_url=base_url, token=SecretStr(token), api_base_path=api_base_path, "
        "timeout=timeout, verify=verify, follow_redirects=follow_redirects, user_agent=user_agent)"
    )
    async_lines.append("        self._transport = AsyncTransport(self.config, client=http_client)")
    for tag, module in TAG_MODULES.items():
        async_lines.append(f"        self.{module} = Async{TAG_CLASSES[tag]}(self._transport)")
    async_lines.extend(
        [
            "",
            '    async def __aenter__(self) -> "AsyncEcstasyClient":',
            '        """Входит в async context manager."""',
            "",
            "        return self",
            "",
            "    async def __aexit__(",
            "        self,",
            "        exc_type: type[BaseException] | None,",
            "        exc: BaseException | None,",
            "        traceback: TracebackType | None,",
            "    ) -> None:",
            '        """Закрывает клиент при выходе из async context manager."""',
            "",
            "        await self.aclose()",
            "",
            "    async def aclose(self) -> None:",
            '        """Закрывает HTTP-сессию клиента."""',
            "",
            "        await self._transport.aclose()",
            "",
        ]
    )
    files["ecstasy_sdk/async_client.py"] = "\n".join(async_lines)
    files["ecstasy_sdk/__init__.py"] = dedent('''\
        """Python SDK для работы с Ecstasy API."""

        from ecstasy_sdk._version import __version__
        from ecstasy_sdk.async_client import AsyncEcstasyClient
        from ecstasy_sdk.client import EcstasyClient

        __all__ = ["AsyncEcstasyClient", "EcstasyClient", "__version__"]
        ''')


def main() -> None:
    """Запускает генерацию SDK."""

    files: dict[str, str] = {}
    for directory in [
        "ecstasy_sdk/models",
        "ecstasy_sdk/transport",
        "ecstasy_sdk/resources",
        "ecstasy_sdk/async_resources",
    ]:
        (ROOT / directory).mkdir(parents=True, exist_ok=True)
    build_core_files(files)
    build_transport_files(files)
    model_names = build_model_files(files)
    operation_count = build_resource_files(files)
    build_client_files(files)
    for rel_path, content in files.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if not content.endswith("\n"):
            content += "\n"
        path.write_text(content, encoding="utf-8")
    print(f"generated files: {len(files)}")
    print(f"models: {len(model_names)}")
    print(f"operations: {operation_count}")


if __name__ == "__main__":
    main()
