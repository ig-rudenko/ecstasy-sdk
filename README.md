# ecstasy-sdk

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Code style: black](https://img.shields.io/badge/code_style-black-black.svg)
![CI](https://github.com/ig-rudenko/ecstasy-sdk/actions/workflows/ci-publish.yml/badge.svg)

Python SDK для работы с [Ecstasy](https://github.com/ig-rudenko/ecstasy) API.

Библиотека предоставляет синхронный и асинхронный клиенты, Pydantic-модели запросов и ответов, типизированные resource-клиенты по группам API и единый транспорт на базе `httpx`.

## Возможности

- Sync клиент: `EcstasyClient`.
- Async клиент: `AsyncEcstasyClient`.
- Pydantic v2 модели.

## Установка

```bash
pip install ecstasy-sdk
```

## Быстрый старт

### Синхронный клиент

```python
from ecstasy_sdk import EcstasyClient

with EcstasyClient(
    base_url="https://ecstasy.example.com",
    token="<api-token>",
) as client:
    me = client.accounts.get_myself()
    device = client.devices.get("switch-01")
    interfaces = client.devices.get_interfaces("switch-01", add_links=True)

    print(me.username)
    print(device.name)
    print(len(interfaces.interfaces))
```

### Асинхронный клиент

```python
from ecstasy_sdk import AsyncEcstasyClient


async def main() -> None:
    async with AsyncEcstasyClient(
        base_url="https://ecstasy.example.com",
        token="<api-token>",
    ) as client:
        me = await client.accounts.get_myself()
        device = await client.devices.get("switch-01")
        interfaces = await client.devices.get_interfaces("switch-01")

        print(me.username, device.name, len(interfaces.interfaces))
```

## Авторизация

SDK отправляет токен в заголовке `Authorization`. Если передать токен без префикса, SDK добавит `Token` автоматически:

```python
client = EcstasyClient(
    base_url="https://ecstasy.example.com",
    token="abc123",
)
```

Итоговый HTTP-заголовок:

```text
Authorization: Token abc123
```

## Resource-клиенты

У клиента доступны группы API:

```python
client.accounts
client.devices
client.gpon
client.gather
client.maps
client.ring_manager
client.tools
```

Асинхронный клиент имеет те же группы и те же имена методов, но методы вызываются через `await`.

## Примеры

### Accounts

```python
me = client.accounts.get_myself()
permissions = client.accounts.get_permissions()
oidc = client.accounts.get_oidc_config()

print(me.username)
print(oidc.authorization_endpoint)
```

### Devices

```python
devices_page = client.devices.list(page=1, group="access")
all_devices = client.devices.list_all(vendor="Huawei")

device = client.devices.get("switch-01")
interfaces = client.devices.get_interfaces(
    "switch-01",
    add_links=True,
    add_comments=True,
)
macs = client.devices.get_macs("switch-01", port="GigabitEthernet0/1")
configs = client.devices.list_configs("switch-01")
```

Создание или обновление выполняется через Pydantic-модели:

```python
from ecstasy_sdk.models import DevicesDetailUpdate

payload = DevicesDetailUpdate(
    ip="192.0.2.10",
    name="switch-01",
    auth_group=1,
    group=2,
)

updated = client.devices.update("switch-01", payload)
```

### GPON

```python
customers = client.gpon.list_customers(page=1, search="Иванов")
customer = client.gpon.get_customers("123")

subscriber_data = client.gpon.list_subscriber_data(contract="100200")
tech_data = client.gpon.get_tech_data("olt-01", port="0/1")
end3 = client.gpon.list_tech_data_end3(street="Ленина", house="10")
```

### Tools

```python
vendor = client.tools.get_mac_vendor("00:11:22:33:44:55")
vlan_desc = client.tools.get_vlan_desc(vlan=100)
trace = client.tools.get_vlan_traceroute(vlan=100, graph_min_length=3)
found = client.tools.get_find_by_desc(pattern="client", is_regex=False)
```

## Модели

Модели экспортируются из `ecstasy_sdk.models`:

```python
from ecstasy_sdk.models import OIDC, BrasPairSessionResult, DeviceInfo, DevicesDetail
```

Имена моделей очищаются от технических суффиксов OpenAPI. Например, модель результата BRAS-сессий доступна как `BrasPairSessionResult`, а поля с аббревиатурами сохраняют читаемые Python-имена:

```python
result.bras1
device.device_ip
subscriber.connection_id
```

Оригинальные имена JSON-полей сохраняются через Pydantic alias.

## Пагинация

Endpoint'ы с DRF pagination возвращают `Page[T]`:

```python
page = client.devices.list(page=1)

print(page.count)
print(page.next)

for device in page.results:
    print(device.name)
```

## Обработка ошибок

SDK преобразует HTTP-ошибки в исключения `ecstasy_sdk.exceptions`.

```python
from ecstasy_sdk import EcstasyClient
from ecstasy_sdk.exceptions import EcstasyAPIError, EcstasyForbiddenError

client = EcstasyClient("https://ecstasy.example.com", "<api-token>")

try:
    device = client.devices.get("switch-01")
except EcstasyForbiddenError:
    print("Недостаточно прав")
except EcstasyAPIError as exc:
    print(exc.status_code)
    print(exc.response_json)
finally:
    client.close()
```

Основные исключения:

- `EcstasyBadRequestError` для HTTP 400.
- `EcstasyUnauthorizedError` для HTTP 401.
- `EcstasyForbiddenError` для HTTP 403.
- `EcstasyNotFoundError` для HTTP 404.
- `EcstasyConflictError` для HTTP 409.
- `EcstasyValidationError` для HTTP 422.
- `EcstasyServerError` для HTTP 5xx.
- `EcstasyTransportError` для сетевых ошибок.
- `EcstasyTimeoutError` для timeout.
- `EcstasyResponseValidationError` для ошибок Pydantic-валидации ответа.

### Problem Details

Если API возвращает `application/problem+json`, SDK сохраняет поля RFC 9457 в `EcstasyAPIError`:

```python
try:
    client.devices.get("switch-01")
except EcstasyAPIError as exc:
    print(exc.title)
    print(exc.detail)
    print(exc.problem_type)
    print(exc.instance)
    print(exc.errors)
```

Полный payload также доступен в `exc.response_json`.

## Сырые ответы

Если в OpenAPI-документации для endpoint'а нет response schema, SDK возвращает raw payload:

- `dict[str, Any]` или `list[Any]` для JSON и `*+json`;
- `str` для текстовых ответов;
- `bytes` для бинарных ответов;
- `None` для HTTP 204.

## Генерация кода из OpenAPI

Основной код моделей и resource-клиентов можно регенерировать из `docs/swagger.json`:

```bash
uv run python scripts/generate_sdk.py
```

Генератор обновляет:

- `ecstasy_sdk/models/`;
- `ecstasy_sdk/resources/`;
- `ecstasy_sdk/async_resources/`;
- базовые клиентские и транспортные файлы, которые создаются шаблонами генератора.

После регенерации нужно выполнить проверки:

```bash
./checks.sh
```

## Проверки разработки

Текущий набор проверок:

```bash
uv run ruff check --fix ecstasy_sdk scripts tests
uv run black -l 110 ecstasy_sdk scripts tests
uv run mypy ecstasy_sdk scripts tests
uv run --extra dev pytest
```

## Требования

- Python `>=3.12`.
- `httpx`.
- `pydantic`.
- `typing-extensions` для Python ниже 3.13.

## Статус

Пакет находится в начальной стадии разработки `0.x`. Публичный API может уточняться по мере проверки SDK на реальном Ecstasy API.
