"""Тесты асинхронного клиента SDK."""

import httpx
import pytest

from ecstasy_sdk import AsyncEcstasyClient
from ecstasy_sdk.models import User


@pytest.mark.asyncio
async def test_async_client_sends_authorization_and_validates_response() -> None:
    """Проверяет URL, Authorization и Pydantic-валидацию async ответа."""

    seen: dict[str, str | None] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        seen["authorization"] = request.headers.get("authorization")
        return httpx.Response(200, json=[{"id": 1, "username": "admin"}])

    client = AsyncEcstasyClient(
        "https://example.com/",
        "Token test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    )

    users = await client.accounts.get_myself()

    assert seen["url"] == "https://example.com/api/v1/accounts/myself"
    assert seen["authorization"] == "Token test"
    assert isinstance(users[0], User)
    assert users[0].username == "admin"

    await client.aclose()
