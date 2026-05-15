from __future__ import annotations

from ecstasy_sdk.models import (
    OIDC,
    User,
    UserPermissions,
)
from ecstasy_sdk.transport.sync import SyncTransport


class AccountsResource:
    """Ресурсный клиент Ecstasy API для группы `Accounts`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def get_myself(self) -> User:
        """
        operationId: accounts_myself_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET", "/accounts/myself", path_params=path_params, query=query, body=None, response_model=User
        )

    def get_myself_permissions(self) -> UserPermissions:
        """
        operationId: accounts_myself_permissions_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/accounts/myself/permissions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=UserPermissions,
        )

    def get_oidc_config(self) -> OIDC:
        """
        operationId: accounts_oidc_config_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/accounts/oidc/config",
            path_params=path_params,
            query=query,
            body=None,
            response_model=OIDC,
        )

    get_permissions = get_myself_permissions
