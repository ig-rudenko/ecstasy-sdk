from __future__ import annotations

from ecstasy_sdk.models import (
    MacGatherScanTask,
    MacGatherStatus,
    MacTraceroute,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncGatherResource:
    """Ресурсный клиент Ecstasy API для группы `Gather`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def create_mac_address_scan_run(self, data: MacGatherScanTask) -> MacGatherScanTask:
        """Выполняет операцию Ecstasy API.

        operationId: gather_mac-address_scan_run_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST",
            "/gather/mac-address/scan/run",
            path_params=path_params,
            query=query,
            body=data,
            response_model=MacGatherScanTask,
        )

    async def get_mac_address_scan_status(self) -> MacGatherStatus:
        """Выполняет операцию Ecstasy API.

        operationId: gather_mac-address_scan_status_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/gather/mac-address/scan/status",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacGatherStatus,
        )

    async def get_traceroute_mac_address(self, mac: str) -> MacTraceroute:
        """Выполняет операцию Ecstasy API.

        operationId: gather_traceroute_mac-address_read.
        """

        path_params = {"mac": mac}
        query = None
        return await self._transport.request(
            "GET",
            "/gather/traceroute/mac-address/{mac}/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacTraceroute,
        )
