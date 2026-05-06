"""Pydantic-схемы, сгенерированные из docs/swagger.json."""

from __future__ import annotations

from typing import Any, cast

from pydantic import Field

from ecstasy_sdk.models.base import EcstasyModel


class User(EcstasyModel):
    """Схема `User` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    username: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_staff: bool | None = None
    is_superuser: bool | None = None
    is_active: bool | None = None
    date_joined: str | None = None


class UserPermissions(EcstasyModel):
    """Схема `UserPermissions` из Ecstasy API."""

    permissions: str | None = None
    console: str | None = None
    ecstasy_loop_url: str | None = None


class Devices(EcstasyModel):
    """Схема `Devices` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    ip: str
    name: str
    vendor: str | None = None
    group: str
    auth_group: int
    model: str | None = None
    serial_number: str | None = None
    os_version: str | None = None
    port_scan_protocol: str | None = None
    cmd_protocol: str | None = None
    active: bool | None = None
    collect_interfaces: bool | None = None
    collect_mac_addresses: bool | None = None
    collect_vlan_info: bool | None = None
    collect_configurations: bool | None = None
    connection_pool_size: int | None = None
    console_url: str | None = None


class BulkDeviceCommandExecution(EcstasyModel):
    """Схема `BulkDeviceCommandExecution` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    task_id: str
    user: str
    command_id: int | None = Field(..., alias="commandId")
    command_name: str = Field(..., alias="commandName")
    command_body: str = Field(..., alias="commandBody")
    context: dict[str, Any] | None = None
    status: str | None = None
    progress: int | None = None
    processed: int | None = None
    total: int | None = None
    launched_at: str = Field(..., alias="launchedAt")
    finished_at: str | None = Field(..., alias="finishedAt")
    success_count: int | None = Field(None, alias="successCount")
    error_count: int | None = Field(None, alias="errorCount")
    skipped_count: int | None = Field(None, alias="skippedCount")


class BulkDeviceCommandExecutionResult(EcstasyModel):
    """Схема `BulkDeviceCommandExecutionResult` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    device_id: int | None = Field(..., alias="deviceId")
    device_name: str = Field(..., alias="deviceName")
    status: str | None = None
    command_text: str = Field(..., alias="commandText")
    output: str | None = None
    detail: str | None = None
    error: str | None = None
    duration: float | None = None
    created_at: str | None = None
    updated_at: str | None = None


class BulkCommandTaskResultSwagger(EcstasyModel):
    """Схема `BulkCommandTaskResultSwagger` из Ecstasy API."""

    device_id: int = Field(..., alias="deviceId")
    device_name: str = Field(..., alias="deviceName")
    status: str
    command_id: int = Field(..., alias="commandId")
    command_text: str = Field(..., alias="commandText")
    output: str
    detail: str
    error: str
    duration: float


class BulkCommandTaskStatusSwagger(EcstasyModel):
    """Схема `BulkCommandTaskStatusSwagger` из Ecstasy API."""

    task_id: str = Field(..., alias="taskId")
    status: str
    progress: int | None = None
    processed: int | None = None
    total: int | None = None
    results_count: int = Field(..., alias="resultsCount")
    result_device_ids: list[int] = Field(..., alias="resultDeviceIds")
    results: list[BulkCommandTaskResultSwagger]


class ExecuteBulkDeviceCommandRequestSwagger(EcstasyModel):
    """Схема `ExecuteBulkDeviceCommandRequestSwagger` из Ecstasy API."""

    device_ids: list[int]
    port: dict[str, str] | None = None
    ip: dict[str, str] | None = None
    mac: dict[str, str] | None = None
    number: dict[str, int] | None = None
    word: dict[str, str] | None = None


class BulkCommandLaunchDeviceSwagger(EcstasyModel):
    """Схема `BulkCommandLaunchDeviceSwagger` из Ecstasy API."""

    device_id: int = Field(..., alias="deviceId")
    device_name: str = Field(..., alias="deviceName")
    detail: str | None = None


class BulkCommandLaunchResponseSwagger(EcstasyModel):
    """Схема `BulkCommandLaunchResponseSwagger` из Ecstasy API."""

    task_id: str = Field(..., alias="taskId")
    devices: list[BulkCommandLaunchDeviceSwagger]
    skipped: list[BulkCommandLaunchDeviceSwagger]


class InterfacesComments(EcstasyModel):
    """Схема `InterfacesComments` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    interface: str
    comment: str
    user: int | None = None
    device: str


class BrassSession(EcstasyModel):
    """Схема `BrassSession` из Ecstasy API."""

    mac: str
    device: str | None = None
    port: str | None = None


class CutBrasSessionSwagger(EcstasyModel):
    """Схема `CutBrasSessionSwagger` из Ecstasy API."""

    errors: list[str]
    port_reload_status: str = Field(..., alias="portReloadStatus")


class BrasSessionSwagger(EcstasyModel):
    """Схема `BrasSessionSwagger` из Ecstasy API."""

    session: str | None
    errors: list[str]


class BrasPairSessionResultSwagger(EcstasyModel):
    """Схема `BrasPairSessionResultSwagger` из Ecstasy API."""

    b_r_a_s1: BrasSessionSwagger = Field(..., alias="BRAS1")
    b_r_a_s2: BrasSessionSwagger = Field(..., alias="BRAS2")


class InterfaceWorkloadSwagger(EcstasyModel):
    """Схема `InterfaceWorkloadSwagger` из Ecstasy API."""

    count: int
    abons: int
    abons_up: int
    abons_up_with_desc: int
    abons_up_no_desc: int
    abons_down: int
    abons_down_with_desc: int
    abons_down_no_desc: int


class DevicesInterfaceWorkloadSwagger(EcstasyModel):
    """Схема `DevicesInterfaceWorkloadSwagger` из Ecstasy API."""

    interfaces_count: list[InterfaceWorkloadSwagger]
    ip: str
    name: str
    vendor: str | None
    group: str
    model: str | None


class DevicesInterfaceWorkloadResultSwagger(EcstasyModel):
    """Схема `DevicesInterfaceWorkloadResultSwagger` из Ecstasy API."""

    devices_count: int
    devices: list[DevicesInterfaceWorkloadSwagger]


class DeviceAuthGroup(EcstasyModel):
    """Схема `DeviceAuthGroup` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None


class DeviceGroup(EcstasyModel):
    """Схема `DeviceGroup` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None


class DevicesDetail(EcstasyModel):
    """Схема `DevicesDetail` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    ip: str
    name: str
    model: str | None = None
    vendor: str | None = None
    serial_number: str | None = None
    os_version: str | None = None
    auth_group: DeviceAuthGroup
    group: DeviceGroup
    snmp_community: str | None = None
    port_scan_protocol: str | None = None
    cmd_protocol: str | None = None
    interface_pattern: str | None = None
    active: bool | None = None
    collect_interfaces: bool | None = None
    collect_mac_addresses: bool | None = None
    collect_vlan_info: bool | None = None
    collect_configurations: bool | None = None
    connection_pool_size: int | None = None


class DevicesDetailUpdate(EcstasyModel):
    """Схема `DevicesDetailUpdate` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    ip: str
    name: str
    model: str | None = None
    vendor: str | None = None
    serial_number: str | None = None
    os_version: str | None = None
    auth_group: int
    group: int
    snmp_community: str | None = None
    port_scan_protocol: str | None = None
    cmd_protocol: str | None = None
    interface_pattern: str | None = None
    active: bool | None = None
    collect_interfaces: bool | None = None
    collect_mac_addresses: bool | None = None
    collect_vlan_info: bool | None = None
    collect_configurations: bool | None = None
    connection_pool_size: int | None = None


class UserDeviceAction(EcstasyModel):
    """Схема `UserDeviceAction` из Ecstasy API."""

    time: str | None = None
    user: str
    action: str


class ChangeDescriptionRequestSwagger(EcstasyModel):
    """Схема `ChangeDescriptionRequestSwagger` из Ecstasy API."""

    port: str
    description: str


class ChangeDescriptionSwagger(EcstasyModel):
    """Схема `ChangeDescriptionSwagger` из Ecstasy API."""

    description: str
    port: str
    saved: str


class ADSLProfile(EcstasyModel):
    """Схема `ADSLProfile` из Ecstasy API."""

    index: int
    port: str


class DeviceCommands(EcstasyModel):
    """Схема `DeviceCommands` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None
    command: str
    device_vendor: str


class ConfigFileSwagger(EcstasyModel):
    """Схема `ConfigFileSwagger` из Ecstasy API."""

    name: str
    size: int
    mod_time: str = Field(..., alias="modTime")


class DeviceInfoSwagger(EcstasyModel):
    """Схема `DeviceInfoSwagger` из Ecstasy API."""

    device_name: str = Field(..., alias="deviceName")
    device_i_p: str = Field(..., alias="deviceIP")
    elastic_stack_link: str = Field(..., alias="elasticStackLink")
    zabbix_host_i_d: str = Field(..., alias="zabbixHostID")
    zabbix_info: dict[str, str | None] = Field(..., alias="zabbixInfo")
    permission: int
    coords: list[float]
    uptime: int
    console_u_r_l: str = Field(..., alias="consoleURL")


class PortDetailInfo(EcstasyModel):
    """Схема `PortDetailInfo` из Ecstasy API."""

    type_: str = Field(..., alias="type")
    data: str | None = None


class InterfaceDetailInfoSwagger(EcstasyModel):
    """Схема `InterfaceDetailInfoSwagger` из Ecstasy API."""

    port_detail_info: PortDetailInfo = Field(..., alias="portDetailInfo")
    port_config: str = Field(..., alias="portConfig")
    port_type: str = Field(..., alias="portType")
    port_errors: str = Field(..., alias="portErrors")
    has_cable_diag: bool = Field(..., alias="hasCableDiag")


class LinkToAnotherDeviceSwagger(EcstasyModel):
    """Схема `LinkToAnotherDeviceSwagger` из Ecstasy API."""

    device_name: str = Field(..., alias="deviceName")
    url: str


class InterfaceComment(EcstasyModel):
    """Схема `InterfaceComment` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    user: str
    text: str


class InterfaceInfoSwagger(EcstasyModel):
    """Схема `InterfaceInfoSwagger` из Ecstasy API."""

    name: str
    status: str
    description: str
    vlans: list[int]
    link: LinkToAnotherDeviceSwagger | None = None
    comments: list[InterfaceComment] | None = None


class InterfacesListSwagger(EcstasyModel):
    """Схема `InterfacesListSwagger` из Ecstasy API."""

    interfaces: list[InterfaceInfoSwagger]
    device_available: bool = Field(..., alias="deviceAvailable")
    collected: str


class MacListSwagger(EcstasyModel):
    """Схема `MacListSwagger` из Ecstasy API."""

    vlan_i_d: int = Field(..., alias="vlanID")
    mac: str
    vlan_name: str = Field(..., alias="vlanName")


class MacListResultSwagger(EcstasyModel):
    """Схема `MacListResultSwagger` из Ecstasy API."""

    result: list[MacListSwagger]
    count: int


class DeviceMedia(EcstasyModel):
    """Схема `DeviceMedia` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    file: str | None = None
    name: str | None = None
    file_type: str | None = None
    is_image: bool | None = None
    description: str | None = None
    mod_time: str | None = None
    url: str | None = None


class DevicePoolStatusesSwagger(EcstasyModel):
    """Схема `DevicePoolStatusesSwagger` из Ecstasy API."""

    connection_pool_size: int = Field(..., alias="connectionPoolSize")
    statuses: list[bool]


class PortControl(EcstasyModel):
    """Схема `PortControl` из Ecstasy API."""

    port: str
    status: str
    save: bool


class PoEPortStatus(EcstasyModel):
    """Схема `PoEPortStatus` из Ecstasy API."""

    port: str
    status: str


class DeviceViewings(EcstasyModel):
    """Схема `DeviceViewings` из Ecstasy API."""

    username: str | None = None
    started: str | None = None
    updated: str | None = None


class DeviceVlanPort(EcstasyModel):
    """Схема `DeviceVlanPort` из Ecstasy API."""

    port: str
    desc: str | None = None


class DeviceVlan(EcstasyModel):
    """Схема `DeviceVlan` из Ecstasy API."""

    ports: list[DeviceVlanPort]
    vlan: int
    desc: str
    datetime: str | None = None


class MacGatherScanTask(EcstasyModel):
    """Схема `MacGatherScanTask` из Ecstasy API."""

    task_id: str | None = None


class MacGatherStatus(EcstasyModel):
    """Схема `MacGatherStatus` из Ecstasy API."""

    status: str | None = None
    progress: str | None = None


class NodesSwagger(EcstasyModel):
    """Схема `NodesSwagger` из Ecstasy API."""

    id_: str = Field(..., alias="id")
    label: str
    shape: str
    color: str


class EdgesSwagger(EcstasyModel):
    """Схема `EdgesSwagger` из Ecstasy API."""

    to: str
    title: str
    value: int
    color: str
    from_: str = Field(..., alias="from")


class MacTracerouteSwagger(EcstasyModel):
    """Схема `MacTracerouteSwagger` из Ecstasy API."""

    nodes: list[NodesSwagger]
    edges: list[EdgesSwagger]


class BuildingAddress(EcstasyModel):
    """Схема `BuildingAddress` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    region: str
    settlement: str
    plan_structure: str = Field(..., alias="planStructure")
    street: str
    house: str
    block: str
    building_type: bool
    floors: int
    total_entrances: int


class Address(EcstasyModel):
    """Схема `Address` из Ecstasy API."""

    region: str | None = None
    settlement: str | None = None
    plan_structure: str | None = Field(None, alias="planStructure")
    street: str | None = None
    house: str
    block: int | None = None
    floor: int | None = None
    apartment: int | None = None


class End3(EcstasyModel):
    """Схема `End3` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    address: Address
    capacity: int
    location: str
    type_: str = Field(..., alias="type")


class CommonCustomerSerializer(EcstasyModel):
    """Схема `CommonCustomerSerializer` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    type_: str = Field(..., alias="type")
    first_name: str | None = Field(..., alias="firstName")
    surname: str | None = None
    last_name: str | None = Field(..., alias="lastName")
    company_name: str | None = Field(..., alias="companyName")
    contract: str
    phone: str | None = None


class SubscriberHouseOLTState(EcstasyModel):
    """Схема `SubscriberHouseOLTState` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    house_address: Address | None = Field(None, alias="houseAddress")
    device_name: str | None = Field(None, alias="deviceName")
    device_port: str | None = Field(None, alias="devicePort")


class SubscriberConnection(EcstasyModel):
    """Схема `SubscriberConnection` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    address: Address
    ip: str | None = None
    ont_id: int
    ont_serial: str | None = None
    ont_mac: str | None = None
    order: str | None = None
    transit: int | None = None
    description: str | None = None
    connected_at: str | None = None
    services: list[str]
    status: str
    tech_capability_id: int
    house_o_l_t_state: list[SubscriberHouseOLTState] | None = Field(None, alias="houseOLTState")
    end3: End3
    end3_port: int = Field(..., alias="end3Port")


class CustomerDetail(EcstasyModel):
    """Схема `CustomerDetail` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    type_: str = Field(..., alias="type")
    first_name: str | None = Field(..., alias="firstName")
    surname: str | None = None
    connections: list[SubscriberConnection] | None = None
    last_name: str | None = Field(..., alias="lastName")
    company_name: str | None = Field(..., alias="companyName")
    contract: str
    phone: str | None = None


class OLTSubscriber(EcstasyModel):
    """Схема `OLTSubscriber` из Ecstasy API."""

    olt_port: str = Field(..., alias="oltPort")
    count: int


class UpdateSubscriberData(EcstasyModel):
    """Схема `UpdateSubscriberData` из Ecstasy API."""

    address: Address
    ip: str | None = None
    tech_capability_id: int | None = None
    description: str | None = None
    ont_id: int
    ont_serial: str | None = None
    ont_mac: str | None = None
    order: str | None = None
    transit: int | None = None
    connected_at: str | None = None
    services: list[str]


class CreateCustomerSerializer(EcstasyModel):
    """Схема `CreateCustomerSerializer` из Ecstasy API."""

    id_: int | None = Field(..., alias="id")
    type_: str = Field(..., alias="type")
    first_name: str | None = Field(None, alias="firstName")
    surname: str | None = None
    last_name: str | None = Field(None, alias="lastName")
    company_name: str | None = Field(None, alias="companyName")
    contract: str
    phone: str | None = None


class SubscriberData(EcstasyModel):
    """Схема `SubscriberData` из Ecstasy API."""

    address: Address
    tech_capability: int | None = None
    customer: CreateCustomerSerializer
    description: str | None = None
    ip: str | None = None
    ont_id: int
    ont_serial: str | None = None
    ont_mac: str | None = None
    order: str | None = None
    transit: int | None = None
    connected_at: str | None = None
    services: list[str]


class OLTState(EcstasyModel):
    """Схема `OLTState` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    fiber: str | None = None
    description: str | None = None


class WriteOnlyHouseBAddress(EcstasyModel):
    """Схема `WriteOnlyHouseBAddress` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    region: str | None = None
    settlement: str | None = None
    plan_structure: str | None = Field(None, alias="planStructure")
    street: str | None = None
    house: str
    block: int | None = None
    building_type: str
    floors: int
    total_entrances: int


class CreateHouseOLTState(EcstasyModel):
    """Схема `CreateHouseOLTState` из Ecstasy API."""

    address: WriteOnlyHouseBAddress
    entrances: str | None = None
    description: str | None = None


class End3Writer(EcstasyModel):
    """Схема `End3Writer` из Ecstasy API."""

    id_: int = Field(..., alias="id")
    address: Address
    capacity: int
    location: str
    type_: str = Field(..., alias="type")


class End3Create(EcstasyModel):
    """Схема `End3Create` из Ecstasy API."""

    address: Address | None = None
    build_address: bool = Field(..., alias="buildAddress")
    location: str


class End3CreateList(EcstasyModel):
    """Схема `End3CreateList` из Ecstasy API."""

    type_: str = Field(..., alias="type")
    existing_splitter: End3Writer | None = Field(None, alias="existingSplitter")
    port_count: int = Field(..., alias="portCount")
    list_: list[End3Create] | None = Field(None, alias="list")


class CreateTechData(EcstasyModel):
    """Схема `CreateTechData` из Ecstasy API."""

    olt_state: OLTState = Field(..., alias="oltState")
    house_b: CreateHouseOLTState = Field(..., alias="houseB")
    end3: End3CreateList


class HouseOLTState(EcstasyModel):
    """Схема `HouseOLTState` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    entrances: str | None = None
    description: str | None = None
    customer_lines: list[End3] = Field(..., alias="customerLines")
    statement: OLTState


class ViewHouseBTechData(EcstasyModel):
    """Схема `ViewHouseBTechData` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    region: str
    settlement: str
    plan_structure: str = Field(..., alias="planStructure")
    street: str
    house: str
    block: str
    building_type: bool
    floors: int
    total_entrances: int
    apartment_building: bool
    olt_states: list[HouseOLTState] = Field(..., alias="oltStates")


class ShortViewSubscriberConnection(EcstasyModel):
    """Схема `ShortViewSubscriberConnection` из Ecstasy API."""

    connection_i_d: int = Field(..., alias="connectionID")
    customer_name: str = Field(..., alias="customerName")
    transit: int | None = None
    customer_i_d: int = Field(..., alias="customerID")


class TechCapability(EcstasyModel):
    """Схема `TechCapability` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    status: str | None = None
    number: int | None = None
    subscribers: list[ShortViewSubscriberConnection] | None = None


class End3TechCapability(EcstasyModel):
    """Схема `End3TechCapability` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    address: Address
    capacity: int
    location: str
    type_: str | None = Field(None, alias="type")
    capability: list[TechCapability] | None = None


class AddEnd3ToHouseOLTState(EcstasyModel):
    """Схема `AddEnd3ToHouseOLTState` из Ecstasy API."""

    end3: End3CreateList
    house_olt_state_i_d: int = Field(..., alias="houseOltStateID")


class StructuresHouseOLTState(EcstasyModel):
    """Схема `StructuresHouseOLTState` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    address: BuildingAddress
    entrances: str | None = None
    description: str | None = None
    customer_lines: list[End3] = Field(..., alias="customerLines")


class UpdateHouseOLTState(EcstasyModel):
    """Схема `UpdateHouseOLTState` из Ecstasy API."""

    entrances: str | None = None
    description: str | None = None
    address: WriteOnlyHouseBAddress


class UpdateRetrieveOLTState(EcstasyModel):
    """Схема `UpdateRetrieveOLTState` из Ecstasy API."""

    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    fiber: str | None = None
    description: str | None = None


class ViewOLTStatesTechData(EcstasyModel):
    """Схема `ViewOLTStatesTechData` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    fiber: str | None = None
    description: str | None = None
    structures: list[StructuresHouseOLTState]


class Map(EcstasyModel):
    """Схема `Map` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None
    interactive: bool | None = None
    preview_image: str | None = None
    type_: str | None = Field(None, alias="type")


class Layer(EcstasyModel):
    """Схема `Layer` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None
    type_: str | None = Field(None, alias="type")
    from_file: str | None = None


class MapDetail(EcstasyModel):
    """Схема `MapDetail` из Ecstasy API."""

    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None
    interactive: bool | None = None
    preview_image: str | None = None
    type_: str | None = Field(None, alias="type")
    from_file: str | None = None
    map_url: str | None = None


class MapLayer(EcstasyModel):
    """Схема `MapLayer` из Ecstasy API."""

    groups: list[str]


class ShortPointRing(EcstasyModel):
    """Схема `ShortPointRing` из Ecstasy API."""

    name: str
    ip: str


class AccessRing(EcstasyModel):
    """Схема `AccessRing` из Ecstasy API."""

    head_name: str
    ports: str
    description: str
    is_normal_rotate_status: bool
    points: list[ShortPointRing]


class TransportRing(EcstasyModel):
    """Схема `TransportRing` из Ecstasy API."""

    name: str
    description: str
    vlans: list[int]


class Comment(EcstasyModel):
    """Схема `Comment` из Ecstasy API."""

    created_time: str = Field(..., alias="createdTime")
    user: str
    text: str


class FoundInterface(EcstasyModel):
    """Схема `FoundInterface` из Ecstasy API."""

    name: str
    status: str
    description: str
    vlans: str
    saved_time: str = Field(..., alias="savedTime")


class FoundDeviceInterfaces(EcstasyModel):
    """Схема `FoundDeviceInterfaces` из Ecstasy API."""

    devices: str
    comments: list[Comment]
    interfaces: FoundInterface


class SearchInterfaceByDescResult(EcstasyModel):
    """Схема `SearchInterfaceByDescResult` из Ecstasy API."""

    interfaces: list[FoundDeviceInterfaces]


class GetVendor(EcstasyModel):
    """Схема `GetVendor` из Ecstasy API."""

    vendor: str
    address: str


class GetVlanDesc(EcstasyModel):
    """Схема `GetVlanDesc` из Ecstasy API."""

    name: str
    description: str


class NodeFont(EcstasyModel):
    """Схема `NodeFont` из Ecstasy API."""

    color: str


class TracerouteNode(EcstasyModel):
    """Схема `TracerouteNode` из Ecstasy API."""

    title: str
    group: int
    hidden: bool | None = None
    id_: int = Field(..., alias="id")
    label: str
    shape: str
    value: int
    font: NodeFont


class TracerouteEdge(EcstasyModel):
    """Схема `TracerouteEdge` из Ecstasy API."""

    value: int
    title: str
    from_: int
    to: int


class VlanTraceroute(EcstasyModel):
    """Схема `VlanTraceroute` из Ecstasy API."""

    nodes: list[TracerouteNode]
    edges: list[TracerouteEdge]
    options: dict[str, str | None]


for _model in [
    User,
    UserPermissions,
    Devices,
    BulkDeviceCommandExecution,
    BulkDeviceCommandExecutionResult,
    BulkCommandTaskResultSwagger,
    BulkCommandTaskStatusSwagger,
    ExecuteBulkDeviceCommandRequestSwagger,
    BulkCommandLaunchDeviceSwagger,
    BulkCommandLaunchResponseSwagger,
    InterfacesComments,
    BrassSession,
    CutBrasSessionSwagger,
    BrasSessionSwagger,
    BrasPairSessionResultSwagger,
    InterfaceWorkloadSwagger,
    DevicesInterfaceWorkloadSwagger,
    DevicesInterfaceWorkloadResultSwagger,
    DeviceAuthGroup,
    DeviceGroup,
    DevicesDetail,
    DevicesDetailUpdate,
    UserDeviceAction,
    ChangeDescriptionRequestSwagger,
    ChangeDescriptionSwagger,
    ADSLProfile,
    DeviceCommands,
    ConfigFileSwagger,
    DeviceInfoSwagger,
    PortDetailInfo,
    InterfaceDetailInfoSwagger,
    LinkToAnotherDeviceSwagger,
    InterfaceComment,
    InterfaceInfoSwagger,
    InterfacesListSwagger,
    MacListSwagger,
    MacListResultSwagger,
    DeviceMedia,
    DevicePoolStatusesSwagger,
    PortControl,
    PoEPortStatus,
    DeviceViewings,
    DeviceVlanPort,
    DeviceVlan,
    MacGatherScanTask,
    MacGatherStatus,
    NodesSwagger,
    EdgesSwagger,
    MacTracerouteSwagger,
    BuildingAddress,
    Address,
    End3,
    CommonCustomerSerializer,
    SubscriberHouseOLTState,
    SubscriberConnection,
    CustomerDetail,
    OLTSubscriber,
    UpdateSubscriberData,
    CreateCustomerSerializer,
    SubscriberData,
    OLTState,
    WriteOnlyHouseBAddress,
    CreateHouseOLTState,
    End3Writer,
    End3Create,
    End3CreateList,
    CreateTechData,
    HouseOLTState,
    ViewHouseBTechData,
    ShortViewSubscriberConnection,
    TechCapability,
    End3TechCapability,
    AddEnd3ToHouseOLTState,
    StructuresHouseOLTState,
    UpdateHouseOLTState,
    UpdateRetrieveOLTState,
    ViewOLTStatesTechData,
    Map,
    Layer,
    MapDetail,
    MapLayer,
    ShortPointRing,
    AccessRing,
    TransportRing,
    Comment,
    FoundInterface,
    FoundDeviceInterfaces,
    SearchInterfaceByDescResult,
    GetVendor,
    GetVlanDesc,
    NodeFont,
    TracerouteNode,
    TracerouteEdge,
    VlanTraceroute,
]:
    cast(type[EcstasyModel], _model).model_rebuild()

__all__ = [
    "User",
    "UserPermissions",
    "Devices",
    "BulkDeviceCommandExecution",
    "BulkDeviceCommandExecutionResult",
    "BulkCommandTaskResultSwagger",
    "BulkCommandTaskStatusSwagger",
    "ExecuteBulkDeviceCommandRequestSwagger",
    "BulkCommandLaunchDeviceSwagger",
    "BulkCommandLaunchResponseSwagger",
    "InterfacesComments",
    "BrassSession",
    "CutBrasSessionSwagger",
    "BrasSessionSwagger",
    "BrasPairSessionResultSwagger",
    "InterfaceWorkloadSwagger",
    "DevicesInterfaceWorkloadSwagger",
    "DevicesInterfaceWorkloadResultSwagger",
    "DeviceAuthGroup",
    "DeviceGroup",
    "DevicesDetail",
    "DevicesDetailUpdate",
    "UserDeviceAction",
    "ChangeDescriptionRequestSwagger",
    "ChangeDescriptionSwagger",
    "ADSLProfile",
    "DeviceCommands",
    "ConfigFileSwagger",
    "DeviceInfoSwagger",
    "PortDetailInfo",
    "InterfaceDetailInfoSwagger",
    "LinkToAnotherDeviceSwagger",
    "InterfaceComment",
    "InterfaceInfoSwagger",
    "InterfacesListSwagger",
    "MacListSwagger",
    "MacListResultSwagger",
    "DeviceMedia",
    "DevicePoolStatusesSwagger",
    "PortControl",
    "PoEPortStatus",
    "DeviceViewings",
    "DeviceVlanPort",
    "DeviceVlan",
    "MacGatherScanTask",
    "MacGatherStatus",
    "NodesSwagger",
    "EdgesSwagger",
    "MacTracerouteSwagger",
    "BuildingAddress",
    "Address",
    "End3",
    "CommonCustomerSerializer",
    "SubscriberHouseOLTState",
    "SubscriberConnection",
    "CustomerDetail",
    "OLTSubscriber",
    "UpdateSubscriberData",
    "CreateCustomerSerializer",
    "SubscriberData",
    "OLTState",
    "WriteOnlyHouseBAddress",
    "CreateHouseOLTState",
    "End3Writer",
    "End3Create",
    "End3CreateList",
    "CreateTechData",
    "HouseOLTState",
    "ViewHouseBTechData",
    "ShortViewSubscriberConnection",
    "TechCapability",
    "End3TechCapability",
    "AddEnd3ToHouseOLTState",
    "StructuresHouseOLTState",
    "UpdateHouseOLTState",
    "UpdateRetrieveOLTState",
    "ViewOLTStatesTechData",
    "Map",
    "Layer",
    "MapDetail",
    "MapLayer",
    "ShortPointRing",
    "AccessRing",
    "TransportRing",
    "Comment",
    "FoundInterface",
    "FoundDeviceInterfaces",
    "SearchInterfaceByDescResult",
    "GetVendor",
    "GetVlanDesc",
    "NodeFont",
    "TracerouteNode",
    "TracerouteEdge",
    "VlanTraceroute",
]
