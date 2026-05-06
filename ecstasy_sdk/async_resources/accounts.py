from __future__ import annotations

from builtins import list as _list
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

    async def list_myself(self) -> _list[User]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: accounts_myself_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/accounts/myself",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[User],
        )

    async def list_myself_permissions(self) -> _list[UserPermissions]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: accounts_myself_permissions_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/accounts/myself/permissions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[UserPermissions],
        )

    async def list_oidc_config(self) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: accounts_oidc_config_list.
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

    get_myself = list_myself

    get_permissions = list_myself_permissions

    get_oidc_config = list_oidc_config
