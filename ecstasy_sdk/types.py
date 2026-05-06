"""Типы и query-фильтры SDK."""

from ecstasy_sdk.models.base import EcstasyModel


class DeviceListFilters(EcstasyModel):
    """Фильтры списка устройств."""

    group: str | None = None
    vendor: str | None = None
    model: str | None = None
    ip: str | None = None
    serial_number: str | None = None
    os_version: str | None = None
    port_scan_protocol: str | None = None
    cmd_protocol: str | None = None
    active: str | bool | None = None
    collect_interfaces: str | bool | None = None
    collect_mac_addresses: str | bool | None = None
    collect_vlan_info: str | bool | None = None
    collect_configurations: str | bool | None = None
    connection_pool_size: str | int | None = None
    name: str | None = None
    return_fields: str | list[str] | None = None


class InterfaceListFilters(EcstasyModel):
    """Фильтры списка интерфейсов устройства."""

    current_status: str | bool | None = None
    vlans: str | None = None
    add_links: str | bool | None = None
    add_comments: str | bool | None = None
    add_zabbix_graph: str | bool | None = None


class End3TechDataFilters(EcstasyModel):
    """Фильтры технических данных End3."""

    house: str | None = None
    block: str | None = None
    tech_capability_status: str | None = None
    street: str | None = None
