from __future__ import annotations

from ecstasy_sdk.models import (
    MacGatherScanTask,
    MacGatherStatus,
    MacTraceroute,
    Page,
    Vlan,
    VlanGatherScanTask,
    VlanGatherStatus,
    VlanPort,
)
from ecstasy_sdk.transport.sync import SyncTransport


class GatherResource:
    """Ресурсный клиент Ecstasy API для группы `Gather`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def create_mac_address_scan_run(self) -> MacGatherScanTask:
        """Запускает сканирование MAC-адресов.

        operationId: gather_mac-address_scan_run_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/gather/mac-address/scan/run",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacGatherScanTask,
        )

    def get_mac_address_scan_status(self) -> MacGatherStatus:
        """Проверяет, выполняется ли сканирование MAC-адресов и возвращает результаты.

        operationId: gather_mac-address_scan_status_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/gather/mac-address/scan/status",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacGatherStatus,
        )

    def get_traceroute_mac_address(self, mac: str) -> MacTraceroute:
        """# Находит все записи в базе данных, которые содержат необходимый MAC-адрес, а затем строит граф связей между этими MAC.

        :param mac: (обязательный, path).

        operationId: gather_traceroute_mac-address_read.
        """

        path_params = {"mac": mac}
        query = None
        return self._transport.request(
            "GET",
            "/gather/traceroute/mac-address/{mac}/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacTraceroute,
        )

    def list_vlan_ports(
        self,
        *,
        device_id: str | None = None,
        device: str | None = None,
        vlan: str | None = None,
        port: str | None = None,
        page: int | None = None,
    ) -> Page[VlanPort]:
        """Return collected VLAN port rows for devices available to the user.

        :param device_id: Device ID (необязательный, query).
        :param device: Device by IP or name (необязательный, query).
        :param vlan: VLAN (необязательный, query).
        :param port: Port (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: gather_vlan-ports_list.
        """

        path_params = None
        query = {"device_id": device_id, "device": device, "vlan": vlan, "port": port, "page": page}
        return self._transport.request(
            "GET",
            "/gather/vlan-ports/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[VlanPort],
        )

    def get_vlan_ports(self, id_: str) -> VlanPort:
        """Return one collected VLAN port row.

        :param id_: (обязательный, path).

        operationId: gather_vlan-ports_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gather/vlan-ports/{id}/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=VlanPort,
        )

    def create_vlan_scan_run(self) -> VlanGatherScanTask:
        """Запускает сканирование VLAN-ов.

        operationId: gather_vlan_scan_run_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/gather/vlan/scan/run",
            path_params=path_params,
            query=query,
            body=None,
            response_model=VlanGatherScanTask,
        )

    def get_vlan_scan_status(self) -> VlanGatherStatus:
        """Проверяет, выполняется ли сканирование VLAN-ов и возвращает результаты.

        operationId: gather_vlan_scan_status_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/gather/vlan/scan/status",
            path_params=path_params,
            query=query,
            body=None,
            response_model=VlanGatherStatus,
        )

    def list_vlans(
        self,
        *,
        device_id: str | None = None,
        device: str | None = None,
        vlan: str | None = None,
        port: str | None = None,
        page: int | None = None,
    ) -> Page[Vlan]:
        """Return collected VLAN rows for devices available to the user.

        :param device_id: (необязательный, query).
        :param device: Device by IP or name (необязательный, query).
        :param vlan: (необязательный, query).
        :param port: Port (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: gather_vlans_list.
        """

        path_params = None
        query = {"device_id": device_id, "device": device, "vlan": vlan, "port": port, "page": page}
        return self._transport.request(
            "GET",
            "/gather/vlans/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[Vlan],
        )

    def get_vlans(self, id_: str) -> Vlan:
        """Return one collected VLAN row.

        :param id_: (обязательный, path).

        operationId: gather_vlans_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET", "/gather/vlans/{id}/", path_params=path_params, query=query, body=None, response_model=Vlan
        )
