"""Асинхронный клиент Ecstasy API."""

from types import TracebackType

import httpx
from pydantic import SecretStr

from ecstasy_sdk.async_resources.accounts import AsyncAccountsResource
from ecstasy_sdk.async_resources.devices import AsyncDevicesResource
from ecstasy_sdk.async_resources.gather import AsyncGatherResource
from ecstasy_sdk.async_resources.gpon import AsyncGponResource
from ecstasy_sdk.async_resources.maps import AsyncMapsResource
from ecstasy_sdk.async_resources.ring_manager import AsyncRingManagerResource
from ecstasy_sdk.async_resources.tools import AsyncToolsResource
from ecstasy_sdk.config import EcstasyConfig
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncEcstasyClient:
    """Асинхронный клиент Ecstasy API."""

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        api_base_path: str = "/api/v1",
        timeout: float | httpx.Timeout = 30.0,
        verify: bool = True,
        follow_redirects: bool = False,
        user_agent: str = "ecstasy-sdk",
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """Создает асинхронный клиент Ecstasy API."""

        self.config = EcstasyConfig(
            base_url=base_url,
            token=SecretStr(token),
            api_base_path=api_base_path,
            timeout=timeout,
            verify=verify,
            follow_redirects=follow_redirects,
            user_agent=user_agent,
        )
        self._transport = AsyncTransport(self.config, client=http_client)
        self.accounts = AsyncAccountsResource(self._transport)
        self.devices = AsyncDevicesResource(self._transport)
        self.gpon = AsyncGponResource(self._transport)
        self.gather = AsyncGatherResource(self._transport)
        self.maps = AsyncMapsResource(self._transport)
        self.ring_manager = AsyncRingManagerResource(self._transport)
        self.tools = AsyncToolsResource(self._transport)

    async def __aenter__(self) -> "AsyncEcstasyClient":
        """Входит в async context manager."""

        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Закрывает клиент при выходе из async context manager."""

        await self.aclose()

    async def aclose(self) -> None:
        """Закрывает HTTP-сессию клиента."""

        await self._transport.aclose()
