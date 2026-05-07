from __future__ import annotations

from builtins import list as _list
from typing import Any

from ecstasy_sdk.models import (
    AccessRing,
    TransportRing,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncRingManagerResource:
    """Ресурсный клиент Ecstasy API для группы `Ring Manager`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def get_access_ring(self, head_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_access-ring_read.
        """

        path_params = {"head_name": head_name}
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/access-ring/{head_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_access_rings(self) -> _list[AccessRing]:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_access-rings_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/access-rings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[AccessRing],
        )

    async def get_transport_ring(self, ring_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_transport-ring_read.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_transport_ring_solutions(self, ring_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_transport-ring_solutions_list.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}/solutions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def create_transport_ring_solutions(self, ring_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_transport-ring_solutions_create.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return await self._transport.request(
            "POST",
            "/ring-manager/transport-ring/{ring_name}/solutions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_transport_ring_solutions_last(self, ring_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_transport-ring_solutions_last_list.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}/solutions/last",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_transport_ring_status(self, ring_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_transport-ring_status_list.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}/status",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_transport_rings(self) -> _list[TransportRing]:
        """Выполняет операцию Ecstasy API.

        operationId: ring-manager_transport-rings_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/ring-manager/transport-rings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[TransportRing],
        )
