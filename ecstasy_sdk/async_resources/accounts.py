from __future__ import annotations

from typing import Any

from ecstasy_sdk.models import (
    User,
    UserPermissions,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncAccountsResource:
    """Ресурсный клиент Ecstasy API для группы `Accounts`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def get_myself(self) -> User:
        """Выполняет операцию Ecstasy API.

        operationId: accounts_myself_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/accounts/myself",
            path_params=path_params,
            query=query,
            body=None,
            response_model=User,
        )

    async def get_myself_permissions(self) -> UserPermissions:
        """Выполняет операцию Ecstasy API.

        operationId: accounts_myself_permissions_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/accounts/myself/permissions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=UserPermissions,
        )

    async def get_oidc_config(self) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: accounts_oidc_config_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/accounts/oidc/config",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )
