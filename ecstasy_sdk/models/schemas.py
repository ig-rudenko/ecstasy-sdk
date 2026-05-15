"""Pydantic-схемы, сгенерированные из OpenAPI-документации."""

from __future__ import annotations

from typing import Any, cast

from pydantic import Field

from ecstasy_sdk.models.base import EcstasyModel


class User(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    username: str = Field(
        ..., description="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_."
    )
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_staff: bool | None = Field(
        None, description="Отметьте, если пользователь может входить в административную часть сайта."
    )
    is_superuser: bool | None = Field(
        None, description="Указывает, что пользователь имеет все права без явного их назначения."
    )
    is_active: bool | None = Field(
        None,
        description="Отметьте, если пользователь должен считаться активным. Уберите эту отметку вместо удаления учётной записи.",
    )
    date_joined: str | None = None


class UserPermissions(EcstasyModel):
    permissions: list[str]
    console: str | None
    ecstasy_loop_url: str | None


class OIDC(EcstasyModel):
    enabled: bool
    url: str
    client_id: str = Field(..., alias="clientId")
    realm: str
    authorization_endpoint: str = Field(..., alias="authorizationEndpoint")
    token_endpoint: str = Field(..., alias="tokenEndpoint")
    userinfo_endpoint: str = Field(..., alias="userinfoEndpoint")
    logout_endpoint: str = Field(..., alias="logoutEndpoint")


class Devices(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    ip: str = Field(..., description="ipv4")
    name: str = Field(..., description="Уникальное поле")
    vendor: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    group: str
    auth_group: int
    model: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    serial_number: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    os_version: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    port_scan_protocol: str | None = Field(
        None,
        description="Выберите протокол, с помощью которого будет осуществляться сканирование интерфейсов",
    )
    cmd_protocol: str | None = Field(
        None,
        description="Выберите протокол, с помощью которого будет осуществляться подключение для вызова команд (например: поиск MAC адресов или сброс порта)",
    )
    active: bool | None = None
    collect_interfaces: bool | None = Field(
        None,
        description='Если включено, то будут собраны интерфейсы во время периодической задачи "interfaces_scan"',
    )
    collect_mac_addresses: bool | None = Field(
        None,
        description='Если включено, то будут собраны MAC адреса во время периодической задачи "mac_table_gather_task"',
    )
    collect_vlan_info: bool | None = Field(
        None,
        description='Если включено, то будет собрана VLAN информация во время периодической задачи "vlan_table_gather_task"',
    )
    collect_configurations: bool | None = Field(
        None,
        description='Если включено, то будут собраны конфигурации во время периодической задачи "configuration_gather_task"',
    )
    connection_pool_size: int | None = Field(
        None, description="Количество подключений к оборудованию, которые могут быть одновременно открыты"
    )
    console_url: str | None = None


class GetDeviceByZabbix(EcstasyModel):
    device: str


class BulkDeviceCommandExecution(EcstasyModel):
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


class BulkCommandTaskResult(EcstasyModel):
    device_id: int = Field(..., alias="deviceId")
    device_name: str = Field(..., alias="deviceName")
    status: str
    command_id: int = Field(..., alias="commandId")
    command_text: str = Field(..., alias="commandText")
    output: str
    detail: str
    error: str
    duration: float


class BulkCommandTaskStatus(EcstasyModel):
    task_id: str = Field(..., alias="taskId")
    status: str
    progress: int | None = None
    processed: int | None = None
    total: int | None = None
    results_count: int = Field(..., alias="resultsCount")
    result_device_ids: list[int] = Field(..., alias="resultDeviceIds")
    results: list[BulkCommandTaskResult]


class ExecuteBulkDeviceCommandRequest(EcstasyModel):
    device_ids: list[int]
    port: dict[str, str] | None = None
    ip: dict[str, str] | None = None
    mac: dict[str, str] | None = None
    number: dict[str, int] | None = None
    word: dict[str, str] | None = None


class BulkCommandLaunchDevice(EcstasyModel):
    device_id: int = Field(..., alias="deviceId")
    device_name: str = Field(..., alias="deviceName")
    detail: str | None = None


class BulkCommandLaunchResponse(EcstasyModel):
    task_id: str = Field(..., alias="taskId")
    devices: list[BulkCommandLaunchDevice]
    skipped: list[BulkCommandLaunchDevice]


class InterfacesComments(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    interface: str
    comment: str
    user: int | None = None
    device: str = Field(..., description="Название оборудования")


class BrassSession(EcstasyModel):
    mac: str
    device: str | None = None
    port: str | None = None


class CutBrasSession(EcstasyModel):
    errors: list[str]
    port_reload_status: str = Field(..., alias="portReloadStatus")


class BrasSession(EcstasyModel):
    session: str | None
    errors: list[str]


class BrasPairSessionResult(EcstasyModel):
    bras1: BrasSession = Field(..., alias="BRAS1")
    bras2: BrasSession = Field(..., alias="BRAS2")


class InterfaceWorkload(EcstasyModel):
    count: int
    abons: int
    abons_up: int
    abons_up_with_desc: int
    abons_up_no_desc: int
    abons_down: int
    abons_down_with_desc: int
    abons_down_no_desc: int


class DevicesInterfaceWorkload(EcstasyModel):
    interfaces_count: InterfaceWorkload
    ip: str
    name: str
    vendor: str | None
    group: str
    model: str | None


class DevicesInterfaceWorkloadResult(EcstasyModel):
    devices_count: int
    devices: list[DevicesInterfaceWorkload]


class DeviceAuthGroup(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None


class DeviceGroup(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None


class DevicesDetail(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    ip: str = Field(..., description="ipv4")
    name: str = Field(..., description="Уникальное поле")
    model: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    vendor: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    serial_number: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    os_version: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    auth_group: DeviceAuthGroup
    group: DeviceGroup
    snmp_community: str | None = Field(
        None, description="Версия - v2c. Используется для сбора интерфейсов, если указан протокол - SNMP"
    )
    port_scan_protocol: str | None = Field(
        None,
        description="Выберите протокол, с помощью которого будет осуществляться сканирование интерфейсов",
    )
    cmd_protocol: str | None = Field(
        None,
        description="Выберите протокол, с помощью которого будет осуществляться подключение для вызова команд (например: поиск MAC адресов или сброс порта)",
    )
    interface_pattern: str | None = Field(
        None,
        description="Паттерн, по которому отфильтрованы интерфейсы. Например `^gi\\S+|^eth\\S+`. По умолчанию все интерфейсы.",
    )
    active: bool | None = None
    collect_interfaces: bool | None = Field(
        None,
        description='Если включено, то будут собраны интерфейсы во время периодической задачи "interfaces_scan"',
    )
    collect_mac_addresses: bool | None = Field(
        None,
        description='Если включено, то будут собраны MAC адреса во время периодической задачи "mac_table_gather_task"',
    )
    collect_vlan_info: bool | None = Field(
        None,
        description='Если включено, то будет собрана VLAN информация во время периодической задачи "vlan_table_gather_task"',
    )
    collect_configurations: bool | None = Field(
        None,
        description='Если включено, то будут собраны конфигурации во время периодической задачи "configuration_gather_task"',
    )
    connection_pool_size: int | None = Field(
        None, description="Количество подключений к оборудованию, которые могут быть одновременно открыты"
    )


class DevicesDetailUpdate(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    ip: str = Field(..., description="ipv4")
    name: str = Field(..., description="Уникальное поле")
    model: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    vendor: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    serial_number: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    os_version: str | None = Field(
        None, description="Если не указано, то обновится автоматически при подключении к устройству"
    )
    auth_group: int = Field(
        ...,
        description="Указываем группу, для удаленного подключения к оборудованию. Используется для протоколов telnet и ssh. Если на оборудовании логин/пароль из указанной группы не подошли, то будут автоматически подбираться пары логин/пароль по очереди, указанной в этом списке (кроме неверного)",
    )
    group: int
    snmp_community: str | None = Field(
        None, description="Версия - v2c. Используется для сбора интерфейсов, если указан протокол - SNMP"
    )
    port_scan_protocol: str | None = Field(
        None,
        description="Выберите протокол, с помощью которого будет осуществляться сканирование интерфейсов",
    )
    cmd_protocol: str | None = Field(
        None,
        description="Выберите протокол, с помощью которого будет осуществляться подключение для вызова команд (например: поиск MAC адресов или сброс порта)",
    )
    interface_pattern: str | None = Field(
        None,
        description="Паттерн, по которому отфильтрованы интерфейсы. Например `^gi\\S+|^eth\\S+`. По умолчанию все интерфейсы.",
    )
    active: bool | None = None
    collect_interfaces: bool | None = Field(
        None,
        description='Если включено, то будут собраны интерфейсы во время периодической задачи "interfaces_scan"',
    )
    collect_mac_addresses: bool | None = Field(
        None,
        description='Если включено, то будут собраны MAC адреса во время периодической задачи "mac_table_gather_task"',
    )
    collect_vlan_info: bool | None = Field(
        None,
        description='Если включено, то будет собрана VLAN информация во время периодической задачи "vlan_table_gather_task"',
    )
    collect_configurations: bool | None = Field(
        None,
        description='Если включено, то будут собраны конфигурации во время периодической задачи "configuration_gather_task"',
    )
    connection_pool_size: int | None = Field(
        None, description="Количество подключений к оборудованию, которые могут быть одновременно открыты"
    )


class UserDeviceAction(EcstasyModel):
    time: str | None = None
    user: str
    action: str


class ChangeDescriptionRequest(EcstasyModel):
    port: str
    description: str


class ChangeDescription(EcstasyModel):
    description: str
    port: str
    saved: str


class ADSLProfile(EcstasyModel):
    index: int
    port: str


class CollectConfigResponse(EcstasyModel):
    status: str


class DeviceCommands(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    name: str = Field(..., description="Кратко, что она делает")
    description: str | None = None
    command: str = Field(
        ...,
        description="Вы можете использовать макросы - {port}, чтобы подставить название интерфейса, а также {ip}, {mac}",
    )
    device_vendor: str = Field(
        ..., description="Команда будет доступна только оборудованию с тем же вендором"
    )


class ConfigFile(EcstasyModel):
    name: str
    size: int
    mod_time: str = Field(..., alias="modTime")


class ZabbixMap(EcstasyModel):
    sysmapid: int
    name: str


class DeviceZabbixInfo(EcstasyModel):
    description: str
    monitoring_available: bool = Field(..., alias="monitoringAvailable")
    inventory: dict[str, str | None]
    maps: list[ZabbixMap]


class DeviceInfo(EcstasyModel):
    device_name: str = Field(..., alias="deviceName")
    device_ip: str = Field(..., alias="deviceIP")
    vendor: str | None
    model: str | None
    serial_number: str | None = Field(..., alias="serialNumber")
    os_version: str | None = Field(..., alias="osVersion")
    elastic_stack_link: str = Field(..., alias="elasticStackLink")
    zabbix_host_id: str = Field(..., alias="zabbixHostID")
    zabbix_url: str = Field(..., alias="zabbixURL")
    zabbix_info: DeviceZabbixInfo = Field(..., alias="zabbixInfo")
    permission: int
    coords: list[float] | None
    uptime: int
    console_url: str = Field(..., alias="consoleURL")


class PortDetailInfo(EcstasyModel):
    type_: str = Field(..., alias="type")
    data: str | None = None


class InterfaceDetailInfo(EcstasyModel):
    port_detail_info: PortDetailInfo = Field(..., alias="portDetailInfo")
    port_config: str = Field(..., alias="portConfig")
    port_type: str = Field(..., alias="portType")
    port_errors: str = Field(..., alias="portErrors")
    has_cable_diag: bool = Field(..., alias="hasCableDiag")


class LinkToAnotherDevice(EcstasyModel):
    device_name: str = Field(..., alias="deviceName")
    url: str


class InterfaceComment(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    user: str
    text: str


class InterfaceInfo(EcstasyModel):
    name: str
    status: str
    description: str
    vlans: list[int]
    link: LinkToAnotherDevice | None = None
    comments: list[InterfaceComment] | None = None


class InterfacesList(EcstasyModel):
    interfaces: list[InterfaceInfo]
    device_available: bool = Field(..., alias="deviceAvailable")
    collected: str


class MacList(EcstasyModel):
    vlan_id: int = Field(..., alias="vlanID")
    mac: str
    vlan_name: str = Field(..., alias="vlanName")


class MacListResult(EcstasyModel):
    result: list[MacList]
    count: int


class DeviceMedia(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    file: str | None = None
    name: str | None = None
    file_type: str | None = None
    is_image: bool | None = None
    description: str | None = None
    mod_time: str | None = None
    url: str | None = None


class DevicePoolStatuses(EcstasyModel):
    connection_pool_size: int = Field(..., alias="connectionPoolSize")
    statuses: list[bool]


class PortControl(EcstasyModel):
    port: str
    status: str
    save: bool


class PoEPortStatus(EcstasyModel):
    port: str
    status: str


class DeviceViewings(EcstasyModel):
    username: str | None = None
    started: str | None = None
    updated: str | None = None


class DeviceVlanPort(EcstasyModel):
    port: str
    desc: str | None = None


class DeviceVlan(EcstasyModel):
    ports: list[DeviceVlanPort]
    vlan: int
    desc: str | None = None
    datetime: str | None = None


class MacGatherScanTask(EcstasyModel):
    task_id: str | None = None


class MacGatherStatus(EcstasyModel):
    status: str | None = None
    progress: float | None = None


class Nodes(EcstasyModel):
    id_: str = Field(..., alias="id")
    label: str
    shape: str
    color: str


class Edges(EcstasyModel):
    to: str
    title: str
    value: int
    color: str
    from_: str = Field(..., alias="from")


class MacTraceroute(EcstasyModel):
    nodes: list[Nodes]
    edges: list[Edges]


class VlanPort(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    vlan_id: int | None = None
    vlan_desc: str | None = None
    vlan: int | None = None
    device_id: int | None = None
    device_name: str | None = None
    device_ip: str | None = None
    port: str
    desc: str | None = None


class VlanGatherScanTask(EcstasyModel):
    task_id: str | None = None


class VlanGatherStatus(EcstasyModel):
    status: str | None = None
    progress: float | None = None


class ShortVlanPort(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    port: str
    desc: str | None = None


class Vlan(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    vlan: int
    desc: str | None = None
    device_id: int | None = None
    device_name: str | None = None
    device_ip: str | None = None
    datetime: str | None = None
    ports: list[ShortVlanPort] | None = None


class BuildingAddress(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    region: str
    settlement: str
    plan_structure: str = Field(..., alias="planStructure")
    street: str
    house: str
    block: str
    building_type: bool
    building_id: int | None = None
    floors: int = Field(..., description="кол-во этажей")
    total_entrances: int = Field(..., description="Кол-во подъездов")


class Address(EcstasyModel):
    region: str | None = None
    settlement: str | None = Field(None, description="Любимовка, Верхнесадовое")
    plan_structure: str | None = Field(None, alias="planStructure")
    street: str | None = Field(
        None,
        description="Полное название с указанием типа (улица/проспект/проезд/бульвар/шоссе/переулок/тупик)",
    )
    house: str = Field(..., description="Можно с буквой (русской)")
    block: int | None = None
    floor: int | None = None
    apartment: int | None = None


class End3(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    address: Address
    capacity: int = Field(..., description="Кол-во портов/волокон")
    location: str
    type_: str = Field(..., alias="type")


class CommonCustomerSerializer(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    type_: str = Field(..., alias="type")
    first_name: str | None = Field(..., alias="firstName")
    surname: str | None = None
    last_name: str | None = Field(..., alias="lastName")
    company_name: str | None = Field(..., alias="companyName")
    contract: str
    phone: str | None = None


class SubscriberHouseOLTState(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    house_address: Address | None = Field(None, alias="houseAddress")
    device_name: str | None = Field(None, alias="deviceName")
    device_port: str | None = Field(None, alias="devicePort")


class ViewSubscriberConnectionSerializer(EcstasyModel):
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
    house_olt_state: list[SubscriberHouseOLTState] | None = Field(None, alias="houseOLTState")
    end3: End3
    end3_port: int = Field(..., alias="end3Port")


class CustomerDetail(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    type_: str = Field(..., alias="type")
    first_name: str | None = Field(..., alias="firstName")
    surname: str | None = None
    connections: list[ViewSubscriberConnectionSerializer] | None = None
    last_name: str | None = Field(..., alias="lastName")
    company_name: str | None = Field(..., alias="companyName")
    contract: str
    phone: str | None = None


class ErrorDetailResponse(EcstasyModel):
    detail: str


class OLTSubscriber(EcstasyModel):
    olt_port: str = Field(..., alias="oltPort")
    count: int


class UpdateSubscriberData(EcstasyModel):
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


class CommonSubscriberConnectionSerializer(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    address: Address
    ip: str | None = None
    ont_id: int
    ont_serial: str | None = None
    ont_mac: str | None = None
    order: str | None = None
    transit: int | None = None
    connected_at: str | None = None
    services: list[str]
    status: str
    end3_port: int = Field(..., alias="end3Port")
    customer: CommonCustomerSerializer


class PaginatedSubscriberConnectionListResponse(EcstasyModel):
    count: int
    next: str | None
    previous: str | None
    results: list[CommonSubscriberConnectionSerializer]


class CreateCustomerSerializer(EcstasyModel):
    id_: int | None = Field(..., alias="id")
    type_: str = Field(..., alias="type")
    first_name: str | None = Field(None, alias="firstName")
    surname: str | None = None
    last_name: str | None = Field(None, alias="lastName")
    company_name: str | None = Field(None, alias="companyName")
    contract: str
    phone: str | None = None


class SubscriberData(EcstasyModel):
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


class TechDataCustomerLine(EcstasyModel):
    type_: str | None = Field(..., alias="type")
    count: int
    type_count: int | None = Field(..., alias="typeCount")


class TechDataList(EcstasyModel):
    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    address: BuildingAddress
    building_type: str | None = None
    building_id: int
    entrances: str | None = None
    customer_line: TechDataCustomerLine | None = Field(None, alias="customerLine")


class PaginatedTechDataListResponse(EcstasyModel):
    count: int
    next: str | None
    previous: str | None
    results: list[TechDataList]


class OLTState(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    fiber: str | None = None
    description: str | None = None


class WriteOnlyHouseBAddress(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    region: str | None = None
    settlement: str | None = Field(None, description="Любимовка, Верхнесадовое")
    plan_structure: str | None = Field(None, alias="planStructure")
    street: str | None = Field(
        None,
        description="Полное название с указанием типа (улица/проспект/проезд/бульвар/шоссе/переулок/тупик)",
    )
    house: str = Field(..., description="Можно с буквой (русской)")
    block: int | None = None
    building_type: str
    floors: int
    total_entrances: int


class CreateHouseOLTState(EcstasyModel):
    address: WriteOnlyHouseBAddress
    entrances: str | None = None
    description: str | None = None


class End3Writer(EcstasyModel):
    id_: int = Field(..., alias="id")
    address: Address
    capacity: int = Field(..., description="Кол-во портов/волокон")
    location: str
    type_: str = Field(..., alias="type")


class End3Create(EcstasyModel):
    address: Address | None = None
    build_address: bool = Field(..., alias="buildAddress")
    location: str


class End3CreateList(EcstasyModel):
    type_: str = Field(..., alias="type")
    existing_splitter: End3Writer | None = Field(None, alias="existingSplitter")
    port_count: int = Field(..., alias="portCount")
    list_: list[End3Create] | None = Field(None, alias="list")


class CreateTechData(EcstasyModel):
    olt_state: OLTState = Field(..., alias="oltState")
    house_b: CreateHouseOLTState = Field(..., alias="houseB")
    end3: End3CreateList


class HouseOLTState(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    entrances: str | None = None
    description: str | None = None
    customer_lines: list[End3] = Field(..., alias="customerLines")
    statement: OLTState


class ViewHouseBTechData(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    region: str
    settlement: str
    plan_structure: str = Field(..., alias="planStructure")
    street: str
    house: str
    block: str
    building_type: bool
    floors: int = Field(..., description="кол-во этажей")
    total_entrances: int = Field(..., description="Кол-во подъездов")
    apartment_building: bool = Field(..., description="Многоквартирный дом или частный")
    olt_states: list[HouseOLTState] = Field(..., alias="oltStates")


class ShortViewSubscriberConnection(EcstasyModel):
    connection_id: int = Field(..., alias="connectionID")
    customer_name: str = Field(..., alias="customerName")
    transit: int | None = None
    customer_id: int = Field(..., alias="customerID")


class TechCapability(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    status: str | None = None
    number: int | None = None
    subscribers: list[ShortViewSubscriberConnection] | None = None


class End3TechCapability(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    address: Address
    capacity: int = Field(..., description="Кол-во портов/волокон")
    location: str
    type_: str | None = Field(None, alias="type")
    capability: list[TechCapability] | None = None


class AddEnd3ToHouseOLTState(EcstasyModel):
    end3: End3CreateList
    house_olt_state_id: int = Field(..., alias="houseOltStateID")


class StructuresHouseOLTState(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    address: BuildingAddress
    entrances: str | None = None
    description: str | None = None
    customer_lines: list[End3] = Field(..., alias="customerLines")


class UpdateHouseOLTState(EcstasyModel):
    entrances: str | None = None
    description: str | None = None
    address: WriteOnlyHouseBAddress


class UpdateRetrieveOLTState(EcstasyModel):
    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    fiber: str | None = None
    description: str | None = None


class ViewOLTStatesTechData(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    device_name: str = Field(..., alias="deviceName")
    device_port: str = Field(..., alias="devicePort")
    fiber: str | None = None
    description: str | None = None
    structures: list[StructuresHouseOLTState]


class Map(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None
    interactive: bool | None = Field(
        None,
        description="Автоматическое обновление состояния узлов сети из тех слоев, что созданы через группу Zabbix",
    )
    preview_image: str | None = Field(None, description="Превью")
    type_: str | None = Field(None, alias="type")


class Layer(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    name: str = Field(..., description="Будет отображаться на карте")
    description: str | None = None
    type_: str | None = Field(None, alias="type")
    from_file: str | None = Field(None, description="Файл должен быть GEOJSON")


class MapDetail(EcstasyModel):
    id_: int | None = Field(None, alias="id")
    name: str
    description: str | None = None
    interactive: bool | None = Field(
        None,
        description="Автоматическое обновление состояния узлов сети из тех слоев, что созданы через группу Zabbix",
    )
    preview_image: str | None = Field(None, description="Превью")
    type_: str | None = Field(None, alias="type")
    from_file: str | None = None
    map_url: str | None = Field(
        None,
        description="URL должен быть абсолютным т.е. содержать обозначение протокола (`http://` или `https://`)",
    )


class MapLayer(EcstasyModel):
    groups: list[str]


class GeoJSONFeature(EcstasyModel):
    type_: str = Field(..., alias="type")
    id_: str = Field(..., alias="id")
    geometry: dict[str, str | None]
    properties: dict[str, str | None]


class GeoJSONFeatureCollection(EcstasyModel):
    type_: str | None = Field(None, alias="type")
    features: list[GeoJSONFeature]


class MapLayerRender(EcstasyModel):
    name: str
    type_: str = Field(..., alias="type")
    properties: dict[str, str | None] | None = None
    features: GeoJSONFeatureCollection


class MapProblem(EcstasyModel):
    id_: str = Field(..., alias="id")
    acknowledges: list[list[str]]


class MapUpdateLayers(EcstasyModel):
    problems: list[MapProblem]


class ShortPointRing(EcstasyModel):
    name: str
    ip: str


class AccessRing(EcstasyModel):
    head_name: str
    ports: str
    description: str
    is_normal_rotate_status: bool
    points: list[ShortPointRing]


class TransportRing(EcstasyModel):
    name: str = Field(..., description="Это название будет отображаться в меню колец")
    description: str
    vlans: list[int]


class Comment(EcstasyModel):
    created_time: str = Field(..., alias="createdTime")
    user: str
    text: str


class FoundInterface(EcstasyModel):
    name: str
    status: str
    description: str
    vlans: str
    saved_time: str = Field(..., alias="savedTime", description='Формат: "2 года, 6 месяцев назад"')


class FoundDeviceInterfaces(EcstasyModel):
    devices: str
    comments: list[Comment]
    interfaces: FoundInterface


class SearchInterfaceByDescResult(EcstasyModel):
    interfaces: list[FoundDeviceInterfaces]


class GetVendor(EcstasyModel):
    vendor: str
    address: str


class GetVlanDesc(EcstasyModel):
    name: str
    description: str


class NodeFont(EcstasyModel):
    color: str


class TracerouteNode(EcstasyModel):
    title: str
    group: int
    hidden: bool | None = None
    id_: int = Field(..., alias="id")
    label: str
    shape: str
    value: int
    font: NodeFont


class TracerouteEdge(EcstasyModel):
    value: int
    title: str
    from_: int = Field(..., description="По факту вернется поле `from`")
    to: int


class VlanTraceroute(EcstasyModel):
    nodes: list[TracerouteNode]
    edges: list[TracerouteEdge]
    options: dict[str, str | None] = Field(..., description="Параметры для отображения связей и физики")


for _model in [
    User,
    UserPermissions,
    OIDC,
    Devices,
    GetDeviceByZabbix,
    BulkDeviceCommandExecution,
    BulkDeviceCommandExecutionResult,
    BulkCommandTaskResult,
    BulkCommandTaskStatus,
    ExecuteBulkDeviceCommandRequest,
    BulkCommandLaunchDevice,
    BulkCommandLaunchResponse,
    InterfacesComments,
    BrassSession,
    CutBrasSession,
    BrasSession,
    BrasPairSessionResult,
    InterfaceWorkload,
    DevicesInterfaceWorkload,
    DevicesInterfaceWorkloadResult,
    DeviceAuthGroup,
    DeviceGroup,
    DevicesDetail,
    DevicesDetailUpdate,
    UserDeviceAction,
    ChangeDescriptionRequest,
    ChangeDescription,
    ADSLProfile,
    CollectConfigResponse,
    DeviceCommands,
    ConfigFile,
    ZabbixMap,
    DeviceZabbixInfo,
    DeviceInfo,
    PortDetailInfo,
    InterfaceDetailInfo,
    LinkToAnotherDevice,
    InterfaceComment,
    InterfaceInfo,
    InterfacesList,
    MacList,
    MacListResult,
    DeviceMedia,
    DevicePoolStatuses,
    PortControl,
    PoEPortStatus,
    DeviceViewings,
    DeviceVlanPort,
    DeviceVlan,
    MacGatherScanTask,
    MacGatherStatus,
    Nodes,
    Edges,
    MacTraceroute,
    VlanPort,
    VlanGatherScanTask,
    VlanGatherStatus,
    ShortVlanPort,
    Vlan,
    BuildingAddress,
    Address,
    End3,
    CommonCustomerSerializer,
    SubscriberHouseOLTState,
    ViewSubscriberConnectionSerializer,
    CustomerDetail,
    ErrorDetailResponse,
    OLTSubscriber,
    UpdateSubscriberData,
    CommonSubscriberConnectionSerializer,
    PaginatedSubscriberConnectionListResponse,
    CreateCustomerSerializer,
    SubscriberData,
    TechDataCustomerLine,
    TechDataList,
    PaginatedTechDataListResponse,
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
    GeoJSONFeature,
    GeoJSONFeatureCollection,
    MapLayerRender,
    MapProblem,
    MapUpdateLayers,
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
    "OIDC",
    "Devices",
    "GetDeviceByZabbix",
    "BulkDeviceCommandExecution",
    "BulkDeviceCommandExecutionResult",
    "BulkCommandTaskResult",
    "BulkCommandTaskStatus",
    "ExecuteBulkDeviceCommandRequest",
    "BulkCommandLaunchDevice",
    "BulkCommandLaunchResponse",
    "InterfacesComments",
    "BrassSession",
    "CutBrasSession",
    "BrasSession",
    "BrasPairSessionResult",
    "InterfaceWorkload",
    "DevicesInterfaceWorkload",
    "DevicesInterfaceWorkloadResult",
    "DeviceAuthGroup",
    "DeviceGroup",
    "DevicesDetail",
    "DevicesDetailUpdate",
    "UserDeviceAction",
    "ChangeDescriptionRequest",
    "ChangeDescription",
    "ADSLProfile",
    "CollectConfigResponse",
    "DeviceCommands",
    "ConfigFile",
    "ZabbixMap",
    "DeviceZabbixInfo",
    "DeviceInfo",
    "PortDetailInfo",
    "InterfaceDetailInfo",
    "LinkToAnotherDevice",
    "InterfaceComment",
    "InterfaceInfo",
    "InterfacesList",
    "MacList",
    "MacListResult",
    "DeviceMedia",
    "DevicePoolStatuses",
    "PortControl",
    "PoEPortStatus",
    "DeviceViewings",
    "DeviceVlanPort",
    "DeviceVlan",
    "MacGatherScanTask",
    "MacGatherStatus",
    "Nodes",
    "Edges",
    "MacTraceroute",
    "VlanPort",
    "VlanGatherScanTask",
    "VlanGatherStatus",
    "ShortVlanPort",
    "Vlan",
    "BuildingAddress",
    "Address",
    "End3",
    "CommonCustomerSerializer",
    "SubscriberHouseOLTState",
    "ViewSubscriberConnectionSerializer",
    "CustomerDetail",
    "ErrorDetailResponse",
    "OLTSubscriber",
    "UpdateSubscriberData",
    "CommonSubscriberConnectionSerializer",
    "PaginatedSubscriberConnectionListResponse",
    "CreateCustomerSerializer",
    "SubscriberData",
    "TechDataCustomerLine",
    "TechDataList",
    "PaginatedTechDataListResponse",
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
    "GeoJSONFeature",
    "GeoJSONFeatureCollection",
    "MapLayerRender",
    "MapProblem",
    "MapUpdateLayers",
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
