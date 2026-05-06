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
