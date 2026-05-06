from __future__ import annotations

from builtins import list as _list
from typing import Any

from ecstasy_sdk.models import (
    ADSLProfile,
    BrasPairSessionResultSwagger,
    BrassSession,
    BulkCommandLaunchResponseSwagger,
    BulkCommandTaskStatusSwagger,
    BulkDeviceCommandExecution,
    BulkDeviceCommandExecutionResult,
    ChangeDescriptionRequestSwagger,
    ChangeDescriptionSwagger,
    ConfigFileSwagger,
    CutBrasSessionSwagger,
    DeviceCommands,
    DeviceInfoSwagger,
    DeviceMedia,
    DevicePoolStatusesSwagger,
    Devices,
    DevicesDetail,
    DevicesDetailUpdate,
    DevicesInterfaceWorkloadResultSwagger,
    DeviceViewings,
    DeviceVlan,
    ExecuteBulkDeviceCommandRequestSwagger,
    InterfaceDetailInfoSwagger,
    InterfacesComments,
    InterfacesListSwagger,
    InterfaceWorkloadSwagger,
    MacListResultSwagger,
    Page,
    PoEPortStatus,
    PortControl,
    UserDeviceAction,
)
from ecstasy_sdk.transport.sync import SyncTransport


class DevicesResource:
    """Ресурсный клиент Ecstasy API для группы `Devices`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def list(
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

        Swagger operationId: devices_list.
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
        return self._transport.request(
            "GET", "/devices/", path_params=path_params, query=query, body=None, response_model=Page[Devices]
        )

    def create(self, data: Devices) -> Devices:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST", "/devices/", path_params=path_params, query=query, body=data, response_model=Devices
        )

    def list_all(
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

        Swagger operationId: devices__all_list.
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
        return self._transport.request(
            "GET",
            "/devices/_all",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[Devices],
        )

    def get_by_zabbix(self, host_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_by-zabbix_read.
        """

        path_params = {"host_id": host_id}
        query = None
        return self._transport.request(
            "GET",
            "/devices/by-zabbix/{host_id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_commands_history(
        self, *, page: int | None = None, page_size: int | None = None
    ) -> Page[BulkDeviceCommandExecution]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_history_list.
        """

        path_params = None
        query = {"page": page, "page_size": page_size}
        return self._transport.request(
            "GET",
            "/devices/commands/history",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[BulkDeviceCommandExecution],
        )

    def list_commands_history_results(
        self, execution_id: str, *, page: int | None = None, page_size: int | None = None
    ) -> Page[BulkDeviceCommandExecutionResult]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_history_results_list.
        """

        path_params = {"execution_id": execution_id}
        query = {"page": page, "page_size": page_size}
        return self._transport.request(
            "GET",
            "/devices/commands/history/{execution_id}/results",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[BulkDeviceCommandExecutionResult],
        )

    def get_commands_tasks(self, task_id: str) -> BulkCommandTaskStatusSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_tasks_read.
        """

        path_params = {"task_id": task_id}
        query = None
        return self._transport.request(
            "GET",
            "/devices/commands/tasks/{task_id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=BulkCommandTaskStatusSwagger,
        )

    def create_commands_execute_multiple(
        self, command_id: str, data: ExecuteBulkDeviceCommandRequestSwagger
    ) -> BulkCommandLaunchResponseSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_execute-multiple_create.
        """

        path_params = {"command_id": command_id}
        query = None
        return self._transport.request(
            "POST",
            "/devices/commands/{command_id}/execute-multiple",
            path_params=path_params,
            query=query,
            body=data,
            response_model=BulkCommandLaunchResponseSwagger,
        )

    def create_comments(self, data: InterfacesComments) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_comments_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/devices/comments",
            path_params=path_params,
            query=query,
            body=data,
            response_model=InterfacesComments,
        )

    def get_comments(self, id_: int) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_comments_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfacesComments,
        )

    def update_comments(self, id_: int, data: InterfacesComments) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_comments_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=InterfacesComments,
        )

    def patch_comments(self, id_: int, data: InterfacesComments) -> InterfacesComments:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_comments_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=InterfacesComments,
        )

    def delete_comments(self, id_: int) -> None:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_comments_delete.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "DELETE",
            "/devices/comments/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def create_cut_session(self, data: BrassSession) -> CutBrasSessionSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_cut-session_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/devices/cut-session",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CutBrasSessionSwagger,
        )

    def list_session(self, *, mac: str | None = None) -> BrasPairSessionResultSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_session_list.
        """

        path_params = None
        query = {"mac": mac}
        return self._transport.request(
            "GET",
            "/devices/session",
            path_params=path_params,
            query=query,
            body=None,
            response_model=BrasPairSessionResultSwagger,
        )

    def list_workload_interfaces(
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
    ) -> DevicesInterfaceWorkloadResultSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_workload_interfaces_list.
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
        return self._transport.request(
            "GET",
            "/devices/workload/interfaces",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicesInterfaceWorkloadResultSwagger,
        )

    def get_workload_interfaces(self, device_name_or_ip: str) -> InterfaceWorkloadSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_workload_interfaces_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/workload/interfaces/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfaceWorkloadSwagger,
        )

    def get(self, device_name_or_ip: str) -> DevicesDetail:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicesDetail,
        )

    def update(self, device_name_or_ip: str, data: DevicesDetailUpdate) -> DevicesDetailUpdate:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "PUT",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DevicesDetailUpdate,
        )

    def patch(self, device_name_or_ip: str, data: DevicesDetailUpdate) -> DevicesDetailUpdate:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_partial_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "PATCH",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DevicesDetailUpdate,
        )

    def delete(self, device_name_or_ip: str) -> None:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_actions(self, device_name_or_ip: str) -> _list[UserDeviceAction]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_actions_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/actions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[UserDeviceAction],
        )

    def list_cable_diag(self, device_name_or_ip: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_cable-diag_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/cable-diag",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def create_change_description(
        self, device_name_or_ip: str, data: ChangeDescriptionRequestSwagger
    ) -> ChangeDescriptionSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_change-description_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/change-description",
            path_params=path_params,
            query=query,
            body=data,
            response_model=ChangeDescriptionSwagger,
        )

    def create_change_dsl_profile(self, device_name_or_ip: str, data: ADSLProfile) -> dict[str, Any]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_change-dsl-profile_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/change-dsl-profile",
            path_params=path_params,
            query=query,
            body=data,
            response_model=dict[str, Any],
        )

    def create_collect_config(self, device_name_or_ip: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_collect-config_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/collect-config",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_commands(self, device_name_or_ip: str) -> _list[DeviceCommands]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/commands",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceCommands],
        )

    def create_commands_execute(self, device_name_or_ip: str, command_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_execute_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "command_id": command_id}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/commands/{command_id}/execute",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def create_commands_validate(self, device_name_or_ip: str, command_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_commands_validate_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "command_id": command_id}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/commands/{command_id}/validate",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def get_config(self, device_name_or_ip: str, file_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_config_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "file_name": file_name}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/config/{file_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def delete_config(self, device_name_or_ip: str, file_name: str) -> None:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_config_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "file_name": file_name}
        query = None
        return self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}/config/{file_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_configs(self, device_name_or_ip: str) -> _list[ConfigFileSwagger]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_configs_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/configs",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[ConfigFileSwagger],
        )

    def list_info(self, device_name_or_ip: str) -> DeviceInfoSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DeviceInfoSwagger,
        )

    def list_interface_info(self, device_name_or_ip: str) -> InterfaceDetailInfoSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_interface-info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/interface-info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfaceDetailInfoSwagger,
        )

    def list_interfaces(
        self,
        device_name_or_ip: str,
        *,
        current_status: bool | None = None,
        vlans: bool | None = None,
        add_links: bool | None = None,
        add_comments: bool | None = None,
        add_zabbix_graph: bool | None = None,
    ) -> InterfacesListSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_interfaces_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {
            "current_status": current_status,
            "vlans": vlans,
            "add_links": add_links,
            "add_comments": add_comments,
            "add_zabbix_graph": add_zabbix_graph,
        }
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/interfaces",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfacesListSwagger,
        )

    def list_macs(self, device_name_or_ip: str, *, port: str | None = None) -> MacListResultSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_macs_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"port": port}
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/macs",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacListResultSwagger,
        )

    def list_media(self, device_name_or_ip: str) -> _list[DeviceMedia]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_media_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/media",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceMedia],
        )

    def create_media(self, device_name_or_ip: str, data: DeviceMedia) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_media_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/media",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DeviceMedia,
        )

    def get_media(self, device_name_or_ip: str, id_: int) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_media_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DeviceMedia,
        )

    def update_media(self, device_name_or_ip: str, id_: int, data: DeviceMedia) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_media_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DeviceMedia,
        )

    def patch_media(self, device_name_or_ip: str, id_: int, data: DeviceMedia) -> DeviceMedia:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_media_partial_update.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=DeviceMedia,
        )

    def delete_media(self, device_name_or_ip: str, id_: int) -> None:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_media_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "id": id_}
        query = None
        return self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}/media/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_pool(self, device_name_or_ip: str) -> DevicePoolStatusesSwagger:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_pool_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/pool",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicePoolStatusesSwagger,
        )

    def delete_pool(self, device_name_or_ip: str) -> None:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_pool_delete.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "DELETE",
            "/devices/{device_name_or_ip}/pool",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def create_port_status(self, device_name_or_ip: str, data: PortControl) -> PortControl:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_port-status_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/port-status",
            path_params=path_params,
            query=query,
            body=data,
            response_model=PortControl,
        )

    def create_set_poe_out(self, device_name_or_ip: str, data: PoEPortStatus) -> PoEPortStatus:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_set-poe-out_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/set-poe-out",
            path_params=path_params,
            query=query,
            body=data,
            response_model=PoEPortStatus,
        )

    def list_stats(self, device_name_or_ip: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_stats_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/stats",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_viewings(self, device_name_or_ip: str) -> _list[DeviceViewings]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_viewings_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/viewings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceViewings],
        )

    def create_viewings(self, device_name_or_ip: str, data: DeviceViewings) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_viewings_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/viewings",
            path_params=path_params,
            query=query,
            body=data,
            response_model=None,
        )

    def list_vlan_info(self, device_name_or_ip: str) -> _list[DeviceVlan]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: devices_vlan-info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/vlan-info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[DeviceVlan],
        )
