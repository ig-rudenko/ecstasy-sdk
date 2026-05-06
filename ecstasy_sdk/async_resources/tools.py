from __future__ import annotations

from typing import Any

from ecstasy_sdk.models import (
    GetVendor,
    GetVlanDesc,
    SearchInterfaceByDescResult,
    VlanTraceroute,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncToolsResource:
    """Ресурсный клиент Ecstasy API для группы `Tools`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def list_find_by_desc(
        self, *, is_regex: bool | None = None, pattern: str | None = None
    ) -> SearchInterfaceByDescResult:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: tools_find-by-desc_list.
        """

        path_params = None
        query = {"is_regex": is_regex, "pattern": pattern}
        return await self._transport.request(
            "GET",
            "/tools/find-by-desc",
            path_params=path_params,
            query=query,
            body=None,
            response_model=SearchInterfaceByDescResult,
        )

    async def get_ip_mac_info(self, ip_or_mac: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: tools_ip-mac-info_read.
        """

        path_params = {"ip_or_mac": ip_or_mac}
        query = None
        return await self._transport.request(
            "GET",
            "/tools/ip-mac-info/{ip_or_mac}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def get_mac_vendor(self, mac: str) -> GetVendor:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: tools_mac-vendor_read.
        """

        path_params = {"mac": mac}
        query = None
        return await self._transport.request(
            "GET",
            "/tools/mac-vendor/{mac}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=GetVendor,
        )

    async def list_vlan_desc(self, *, vlan: int | None = None) -> GetVlanDesc:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: tools_vlan-desc_list.
        """

        path_params = None
        query = {"vlan": vlan}
        return await self._transport.request(
            "GET",
            "/tools/vlan-desc",
            path_params=path_params,
            query=query,
            body=None,
            response_model=GetVlanDesc,
        )

    async def list_vlan_traceroute(
        self,
        *,
        vlan: int | None = None,
        ep: bool | None = None,
        ad: bool | None = None,
        double_check: bool | None = None,
        graph_min_length: int | None = None,
    ) -> VlanTraceroute:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: tools_vlan-traceroute_list.
        """

        path_params = None
        query = {
            "vlan": vlan,
            "ep": ep,
            "ad": ad,
            "double_check": double_check,
            "graph_min_length": graph_min_length,
        }
        return await self._transport.request(
            "GET",
            "/tools/vlan-traceroute",
            path_params=path_params,
            query=query,
            body=None,
            response_model=VlanTraceroute,
        )

    async def list_vlans_scan_check(self) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: tools_vlans-scan_check_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/tools/vlans-scan/check",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    get_vlan_traceroute = list_vlan_traceroute

    get_vlan_desc = list_vlan_desc

    find_by_desc = list_find_by_desc
