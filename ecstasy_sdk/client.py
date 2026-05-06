"""Синхронный клиент Ecstasy API."""

import httpx
from pydantic import SecretStr

from ecstasy_sdk.config import EcstasyConfig
from ecstasy_sdk.resources.accounts import AccountsResource
from ecstasy_sdk.resources.devices import DevicesResource
from ecstasy_sdk.resources.gather import GatherResource
from ecstasy_sdk.resources.gpon import GponResource
from ecstasy_sdk.resources.maps import MapsResource
from ecstasy_sdk.resources.ring_manager import RingManagerResource
from ecstasy_sdk.resources.tools import ToolsResource
from ecstasy_sdk.transport.sync import SyncTransport


class EcstasyClient:
    """Синхронный клиент Ecstasy API."""

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
        http_client: httpx.Client | None = None,
    ) -> None:
        """Создает синхронный клиент Ecstasy API."""

        self.config = EcstasyConfig(
            base_url=base_url,
            token=SecretStr(token),
            api_base_path=api_base_path,
            timeout=timeout,
            verify=verify,
            follow_redirects=follow_redirects,
            user_agent=user_agent,
        )
        self._transport = SyncTransport(self.config, client=http_client)
        self.accounts = AccountsResource(self._transport)
        self.devices = DevicesResource(self._transport)
        self.gpon = GponResource(self._transport)
        self.gather = GatherResource(self._transport)
        self.maps = MapsResource(self._transport)
        self.ring_manager = RingManagerResource(self._transport)
        self.tools = ToolsResource(self._transport)

    def __enter__(self) -> "EcstasyClient":
        """Входит в sync context manager."""

        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        """Закрывает клиент при выходе из context manager."""

        self.close()

    def close(self) -> None:
        """Закрывает HTTP-сессию клиента."""

        self._transport.close()
