# ecstasy-sdk

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Code style: black](https://img.shields.io/badge/code_style-black-black.svg)
![CI](https://github.com/ig-rudenko/ecstasy-sdk/actions/workflows/ci-publish.yml/badge.svg)

---

Python SDK для работы с [Ecstasy](https://github.com/ig-rudenko/ecstasy) API.

Библиотека предоставляет синхронный и асинхронный клиенты, Pydantic-схемы запросов и ответов, типизированные resource-клиенты по группам API и единый транспорт на базе `httpx`.

## Возможности

- Sync клиент: `EcstasyClient`.
- Async клиент: `AsyncEcstasyClient`.
- Pydantic v2 модели для swagger definitions.

## Установка

```bash
pip install ecstasy-sdk
```

## Быстрый старт

### Синхронный клиент

```python
from ecstasy_sdk import EcstasyClient

client = EcstasyClient(
    base_url="https://ecstasy.example.com",
    token="<api-token>",
)

try:
    users = client.accounts.get_myself()
    device = client.devices.get("switch-01")
    interfaces = client.devices.list_interfaces("switch-01")
finally:
    client.close()
```

Можно использовать context manager:

```python
from ecstasy_sdk import EcstasyClient

with EcstasyClient("https://ecstasy.example.com", "<api-token>") as client:
    page = client.devices.list(page=1)
    for device in page.results:
        print(device.name, device.ip)
```

### Асинхронный клиент

```python
from ecstasy_sdk import AsyncEcstasyClient


async def main() -> None:
    async with AsyncEcstasyClient(
        base_url="https://ecstasy.example.com",
        token="<api-token>",
    ) as client:
        users = await client.accounts.get_myself()
        device = await client.devices.get("switch-01")
        interfaces = await client.devices.list_interfaces("switch-01")
```

## Авторизация

SDK всегда отправляет токен в заголовке `Authorization` с префиксом `Token`.

Передавайте только значение API-токена без префикса:

```python
client = EcstasyClient(
    base_url="https://ecstasy.example.com",
    token="abc123",
)
```

Итоговый HTTP-заголовок будет таким:

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

Асинхронный клиент имеет те же группы и те же имена методов, но методы нужно вызывать через `await`.

## Примеры

### Accounts

```python
users = client.accounts.get_myself()
permissions = client.accounts.get_permissions()
oidc_config = client.accounts.get_oidc_config()
```

### Devices

```python
devices_page = client.devices.list(page=1, group="access")
all_devices = client.devices.list_all(vendor="Huawei")

device = client.devices.get("switch-01")
interfaces = client.devices.list_interfaces(
    "switch-01",
    add_links=True,
    add_comments=True,
)
macs = client.devices.list_macs("switch-01", port="GigabitEthernet0/1")
configs = client.devices.list_configs("switch-01")
```

Создание или обновление выполняется через Pydantic-модели:

```python
from ecstasy_sdk.models import DevicesDetailUpdate

payload = DevicesDetailUpdate(
    ip="192.0.2.10",
    name="switch-01",
    auth_group=1,
    group="access",
)

updated = client.devices.update("switch-01", payload)
```

### GPON

```python
customers = client.gpon.list_customers()
customer = client.gpon.get_customers("123")

subscriber_data = client.gpon.list_subscriber_data()
tech_data = client.gpon.get_tech_data("olt-01")
```

### Tools

```python
vendor = client.tools.get_mac_vendor("00:11:22:33:44:55")
vlan_desc = client.tools.get_vlan_desc(vlan=100)
trace = client.tools.get_vlan_traceroute(vlan=100, graph_min_length=3)
found = client.tools.find_by_desc(pattern="client", is_regex=False)
```

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

## Сырые ответы

Если в swagger для endpoint'а нет response schema, SDK возвращает raw payload:

- `dict[str, Any]` или `list[Any]` для JSON;
- `str` для текстовых ответов;
- `bytes` для бинарных ответов;
- `None` для HTTP 204.

## Генерация кода из swagger

Основной код моделей и resource-клиентов можно регенерировать из `docs/swagger.json`:

```bash
uv run python scripts/generate_sdk.py
```

После регенерации нужно выполнить проверки:

```bash
./checks.sh
```

## Проверки разработки

Текущий набор проверок:

```bash
uv run ruff check --fix ecstasy_sdk
uv run black -l 110 ecstasy_sdk
uv run mypy ecstasy_sdk
uv run --extra dev pytest
```

## Требования

- Python `>=3.12`.
- `httpx`.
- `pydantic`.
- `typing-extensions` для Python ниже 3.13.

## Статус

Пакет находится в начальной стадии разработки `0.x`. Публичный API может уточняться по мере проверки SDK на реальном Ecstasy API.
