"""Тесты синхронного клиента SDK."""

import httpx
import pytest

from ecstasy_sdk import EcstasyClient
from ecstasy_sdk.exceptions import EcstasyForbiddenError
from ecstasy_sdk.models import Devices, Page, User


def test_client_sends_authorization_and_validates_response() -> None:
    """Проверяет URL, Authorization и Pydantic-валидацию ответа."""

    seen: dict[str, str | None] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["authorization"] = request.headers.get("authorization")
        return httpx.Response(200, json=[{"id": 1, "username": "admin"}])

    client = EcstasyClient(
        "https://example.com/",
        "Token test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )

    users = client.accounts.get_myself()

    assert seen["url"] == "https://example.com/api/v1/accounts/myself"
    assert seen["authorization"] == "Token test"
    assert isinstance(users[0], User)
    assert users[0].username == "admin"

    client.close()


def test_client_validates_paginated_response() -> None:
    """Проверяет DRF pagination модель."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "count": 1,
                "next": None,
                "previous": None,
                "results": [{"ip": "192.0.2.1", "name": "switch-01", "group": "access", "auth_group": 1}],
            },
        )

    client = EcstasyClient(
        "https://example.com",
        "Token test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )

    page = client.devices.list()

    assert isinstance(page, Page)
    assert isinstance(page.results[0], Devices)
    assert page.results[0].name == "switch-01"

    client.close()


def test_client_raises_api_error() -> None:
    """Проверяет преобразование HTTP-ошибок в SDK exception."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(403, request=request, json={"detail": "forbidden"})

    client = EcstasyClient(
        "https://example.com",
        "Token test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )

    with pytest.raises(EcstasyForbiddenError):
        client.accounts.get_myself()

    client.close()
