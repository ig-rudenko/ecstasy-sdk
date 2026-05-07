from __future__ import annotations

from builtins import list as _list
from typing import Any

from ecstasy_sdk.models import (
    ADSLProfile,
    BrasPairSessionResult,
    BrassSession,
    BulkCommandLaunchResponse,
    BulkCommandTaskStatus,
    BulkDeviceCommandExecution,
    BulkDeviceCommandExecutionResult,
    ChangeDescription,
    ChangeDescriptionRequest,
    ConfigFile,
    CutBrasSession,
    DeviceCommands,
    DeviceInfo,
    DeviceMedia,
    DevicePoolStatuses,
    Devices,
    DevicesDetail,
    DevicesDetailUpdate,
    DevicesInterfaceWorkloadResult,
    DeviceViewings,
    DeviceVlan,
    ExecuteBulkDeviceCommandRequest,
    InterfaceDetailInfo,
    InterfacesComments,
    InterfacesList,
    InterfaceWorkload,
    MacListResult,
    Page,
    PoEPortStatus,
    PortControl,
    UserDeviceAction,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncDevicesResource:
    """Ресурсный клиент Ecstasy API для группы `Devices`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def list(
        self,
        *,
        group: str | None = None,
        vendor: str | None = None,
        model: str | None = None,
        ip: str | None = None,
        serial_number: str | None = None,
        os_version: str | None = None,
        port_scan_protocol: str | None = None,
        cmd_protocol: str | None = None,
        active: str | None = None,
        collect_interfaces: str | None = None,
        collect_mac_addresses: str | None = None,
        collect_vlan_info: str | None = None,
        collect_configurations: str | None = None,
        connection_pool_size: str | None = None,
        name: str | None = None,
        return_fields: str | None = None,
        page: int | None = None,
    ) -> Page[Devices]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_list.
        """

        path_params = None
        query = {
            "group": group,
            "vendor": vendor,
            "model": model,
            "ip": ip,
            "serial_number": serial_number,
            "os_version": os_version,
            "port_scan_protocol": port_scan_protocol,
            "cmd_protocol": cmd_protocol,
            "active": active,
            "collect_interfaces": collect_interfaces,
            "collect_mac_addresses": collect_mac_addresses,
            "collect_vlan_info": collect_vlan_info,
            "collect_configurations": collect_configurations,
            "connection_pool_size": connection_pool_size,
            "name": name,
            "return_fields": return_fields,
            "page": page,
        }
        return await self._transport.request(
            "GET", "/devices/", path_params=path_params, query=query, body=None, response_model=Page[Devices]
        )

    async def create(self, data: Devices) -> Devices:
        """Выполняет операцию Ecstasy API.

        operationId: devices_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST", "/devices/", path_params=path_params, query=query, body=data, response_model=Devices
        )

    async def list_all(
        self,
        *,
        group: str | None = None,
        vendor: str | None = None,
        model: str | None = None,
        ip: str | None = None,
        serial_number: str | None = None,
        os_version: str | None = None,
        port_scan_protocol: str | None = None,
        cmd_protocol: str | None = None,
        active: str | None = None,
        collect_interfaces: str | None = None,
        collect_mac_addresses: str | None = None,
        collect_vlan_info: str | None = None,
        collect_configurations: str | None = None,
        connection_pool_size: str | None = None,
        name: str | None = None,
        return_fields: str | None = None,
    ) -> _list[Devices]:
        """Выполняет операцию Ecstasy API.

        operationId: devices__all_list.
        """

        path_params = None
        query = {
            "group": group,
            "vendor": vendor,
            "model": model,
            "ip": ip,
            "serial_number": serial_number,
            "os_version": os_version,
            "port_scan_protocol": port_scan_protocol,
            "cmd_protocol": cmd_protocol,
            "active": active,
            "collect_interfaces": collect_interfaces,
            "collect_mac_addresses": collect_mac_addresses,
            "collect_vlan_info": collect_vlan_info,
            "collect_configurations": collect_configurations,
            "connection_pool_size": connection_pool_size,
            "name": name,
            "return_fields": return_fields,
        }
        return await self._transport.request(
            "GET",
            "/devices/_all",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[Devices],
        )

    async def get_by_zabbix(self, host_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_by-zabbix_read.
        """

        path_params = {"host_id": host_id}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/by-zabbix/{host_id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_commands_history(
        self, *, page: int | None = None, page_size: int | None = None
    ) -> Page[BulkDeviceCommandExecution]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_history_list.
        """

        path_params = None
        query = {"page": page, "page_size": page_size}
        return await self._transport.request(
            "GET",
            "/devices/commands/history",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[BulkDeviceCommandExecution],
        )

    async def list_commands_history_results(
        self, execution_id: str, *, page: int | None = None, page_size: int | None = None
    ) -> Page[BulkDeviceCommandExecutionResult]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_history_results_list.
        """

        path_params = {"execution_id": execution_id}
        query = {"page": page, "page_size": page_size}
        return await self._transport.request(
            "GET",
            "/devices/commands/history/{execution_id}/results",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[BulkDeviceCommandExecutionResult],
        )

    async def get_commands_tasks(self, task_id: str) -> BulkCommandTaskStatus:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_tasks_read.
        """

        path_params = {"task_id": task_id}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/commands/tasks/{task_id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=BulkCommandTaskStatus,
        )

    async def create_commands_execute_multiple(
        self, command_id: str, data: ExecuteBulkDeviceCommandRequest
    ) -> BulkCommandLaunchResponse:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_execute-multiple_create.
        """

        path_params = {"command_id": command_id}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/commands/{command_id}/execute-multiple",
            path_params=path_params,
            query=query,
            body=data,
            response_model=BulkCommandLaunchResponse,
        )

    async def create_comments(self, data: InterfacesComments) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        operationId: devices_comments_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST",
            "/devices/comments",
            path_params=path_params,
            query=query,
            body=data,
            response_model=InterfacesComments,
        )

    async def get_comments(self, id_: int) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        operationId: devices_comments_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfacesComments,
        )

    async def update_comments(self, id_: int, data: InterfacesComments) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        operationId: devices_comments_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=InterfacesComments,
        )

    async def patch_comments(self, id_: int, data: InterfacesComments) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        operationId: devices_comments_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=InterfacesComments,
        )

    async def delete_comments(self, id_: int) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: devices_comments_delete.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "DELETE",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def create_cut_session(self, data: BrassSession) -> CutBrasSession:
        """Выполняет операцию Ecstasy API.

        operationId: devices_cut-session_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST",
            "/devices/cut-session",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CutBrasSession,
        )

    async def list_session(self, *, mac: str | None = None) -> BrasPairSessionResult:
        """Выполняет операцию Ecstasy API.

        operationId: devices_session_list.
        """

        path_params = None
        query = {"mac": mac}
        return await self._transport.request(
            "GET",
            "/devices/session",
            path_params=path_params,
            query=query,
            body=None,
            response_model=BrasPairSessionResult,
        )

    async def list_workload_interfaces(
        self,
        *,
        group: str | None = None,
        vendor: str | None = None,
        model: str | None = None,
        ip: str | None = None,
        serial_number: str | None = None,
        os_version: str | None = None,
        port_scan_protocol: str | None = None,
        cmd_protocol: str | None = None,
        active: str | None = None,
        collect_interfaces: str | None = None,
        collect_mac_addresses: str | None = None,
        collect_vlan_info: str | None = None,
        collect_configurations: str | None = None,
        connection_pool_size: str | None = None,
        name: str | None = None,
        return_fields: str | None = None,
    ) -> DevicesInterfaceWorkloadResult:
        """Выполняет операцию Ecstasy API.

        operationId: devices_workload_interfaces_list.
        """

        path_params = None
        query = {
            "group": group,
            "vendor": vendor,
            "model": model,
            "ip": ip,
            "serial_number": serial_number,
            "os_version": os_version,
            "port_scan_protocol": port_scan_protocol,
            "cmd_protocol": cmd_protocol,
            "active": active,
            "collect_interfaces": collect_interfaces,
            "collect_mac_addresses": collect_mac_addresses,
            "collect_vlan_info": collect_vlan_info,
            "collect_configurations": collect_configurations,
            "connection_pool_size": connection_pool_size,
            "name": name,
            "return_fields": return_fields,
        }
        return await self._transport.request(
            "GET",
            "/devices/workload/interfaces",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicesInterfaceWorkloadResult,
        )

    async def get_workload_interfaces(self, device_name_or_ip: str) -> InterfaceWorkload:
        """Выполняет операцию Ecstasy API.

        operationId: devices_workload_interfaces_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/workload/interfaces/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfaceWorkload,
        )

    async def get(self, device_name_or_ip: str) -> DevicesDetail:
        """Выполняет операцию Ecstasy API.

        operationId: devices_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicesDetail,
        )

    async def update(self, device_name_or_ip: str, data: DevicesDetailUpdate) -> DevicesDetailUpdate:
        """Выполняет операцию Ecstasy API.

        operationId: devices_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "PUT",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DevicesDetailUpdate,
        )

    async def patch(self, device_name_or_ip: str, data: DevicesDetailUpdate) -> DevicesDetailUpdate:
        """Выполняет операцию Ecstasy API.

        operationId: devices_partial_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "PATCH",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DevicesDetailUpdate,
        )

    async def delete(self, device_name_or_ip: str) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: devices_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_actions(self, device_name_or_ip: str) -> _list[UserDeviceAction]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_actions_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/actions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[UserDeviceAction],
        )

    async def list_cable_diag(self, device_name_or_ip: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_cable-diag_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/cable-diag",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def create_change_description(
        self, device_name_or_ip: str, data: ChangeDescriptionRequest
    ) -> ChangeDescription:
        """Выполняет операцию Ecstasy API.

        operationId: devices_change-description_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/change-description",
            path_params=path_params,
            query=query,
            body=data,
            response_model=ChangeDescription,
        )

    async def create_change_dsl_profile(self, device_name_or_ip: str, data: ADSLProfile) -> dict[str, Any]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_change-dsl-profile_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/change-dsl-profile",
            path_params=path_params,
            query=query,
            body=data,
            response_model=dict[str, Any],
        )

    async def create_collect_config(self, device_name_or_ip: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_collect-config_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/collect-config",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_commands(self, device_name_or_ip: str) -> _list[DeviceCommands]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/commands",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceCommands],
        )

    async def create_commands_execute(self, device_name_or_ip: str, command_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_execute_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "command_id": command_id}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/commands/{command_id}/execute",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def create_commands_validate(self, device_name_or_ip: str, command_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_commands_validate_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "command_id": command_id}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/commands/{command_id}/validate",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def get_config(self, device_name_or_ip: str, file_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_config_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "file_name": file_name}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/config/{file_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def delete_config(self, device_name_or_ip: str, file_name: str) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: devices_config_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "file_name": file_name}
        query = None
        return await self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}/config/{file_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_configs(self, device_name_or_ip: str) -> _list[ConfigFile]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_configs_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/configs",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[ConfigFile],
        )

    async def list_info(self, device_name_or_ip: str) -> DeviceInfo:
        """Выполняет операцию Ecstasy API.

        operationId: devices_info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DeviceInfo,
        )

    async def list_interface_info(self, device_name_or_ip: str) -> InterfaceDetailInfo:
        """Выполняет операцию Ecstasy API.

        operationId: devices_interface-info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/interface-info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfaceDetailInfo,
        )

    async def list_interfaces(
        self,
        device_name_or_ip: str,
        *,
        current_status: bool | None = None,
        vlans: bool | None = None,
        add_links: bool | None = None,
        add_comments: bool | None = None,
        add_zabbix_graph: bool | None = None,
    ) -> InterfacesList:
        """Выполняет операцию Ecstasy API.

        operationId: devices_interfaces_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {
            "current_status": current_status,
            "vlans": vlans,
            "add_links": add_links,
            "add_comments": add_comments,
            "add_zabbix_graph": add_zabbix_graph,
        }
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/interfaces",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfacesList,
        )

    async def list_macs(self, device_name_or_ip: str, *, port: str | None = None) -> MacListResult:
        """Выполняет операцию Ecstasy API.

        operationId: devices_macs_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"port": port}
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/macs",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacListResult,
        )

    async def list_media(self, device_name_or_ip: str) -> _list[DeviceMedia]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_media_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/media",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceMedia],
        )

    async def create_media(self, device_name_or_ip: str, data: DeviceMedia) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        operationId: devices_media_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/media",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DeviceMedia,
        )

    async def get_media(self, device_name_or_ip: str, id_: int) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        operationId: devices_media_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DeviceMedia,
        )

    async def update_media(self, device_name_or_ip: str, id_: int, data: DeviceMedia) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        operationId: devices_media_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DeviceMedia,
        )

    async def patch_media(self, device_name_or_ip: str, id_: int, data: DeviceMedia) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        operationId: devices_media_partial_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DeviceMedia,
        )

    async def delete_media(self, device_name_or_ip: str, id_: int) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: devices_media_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return await self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_pool(self, device_name_or_ip: str) -> DevicePoolStatuses:
        """Выполняет операцию Ecstasy API.

        operationId: devices_pool_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/pool",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicePoolStatuses,
        )

    async def delete_pool(self, device_name_or_ip: str) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: devices_pool_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}/pool",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def create_port_status(self, device_name_or_ip: str, data: PortControl) -> PortControl:
        """Выполняет операцию Ecstasy API.

        operationId: devices_port-status_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/port-status",
            path_params=path_params,
            query=query,
            body=data,
            response_model=PortControl,
        )

    async def create_set_poe_out(self, device_name_or_ip: str, data: PoEPortStatus) -> PoEPortStatus:
        """Выполняет операцию Ecstasy API.

        operationId: devices_set-poe-out_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/set-poe-out",
            path_params=path_params,
            query=query,
            body=data,
            response_model=PoEPortStatus,
        )

    async def list_stats(self, device_name_or_ip: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_stats_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/stats",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_viewings(self, device_name_or_ip: str) -> _list[DeviceViewings]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_viewings_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/viewings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceViewings],
        )

    async def create_viewings(self, device_name_or_ip: str, data: DeviceViewings) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: devices_viewings_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/viewings",
            path_params=path_params,
            query=query,
            body=data,
            response_model=None,
        )

    async def list_vlan_info(self, device_name_or_ip: str) -> _list[DeviceVlan]:
        """Выполняет операцию Ecstasy API.

        operationId: devices_vlan-info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return await self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/vlan-info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceVlan],
        )
