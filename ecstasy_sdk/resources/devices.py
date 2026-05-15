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
    CollectConfigResponse,
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
    GetDeviceByZabbix,
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
        """Этот класс представляет собой ListAPIView, который возвращает список всех устройств в базе данных.

        :param group: (необязательный, query).
        :param vendor: (необязательный, query).
        :param model: (необязательный, query).
        :param ip: (необязательный, query).
        :param serial_number: (необязательный, query).
        :param os_version: (необязательный, query).
        :param port_scan_protocol: (необязательный, query).
        :param cmd_protocol: (необязательный, query).
        :param active: (необязательный, query).
        :param collect_interfaces: Collect interfaces (необязательный, query).
        :param collect_mac_addresses: (необязательный, query).
        :param collect_vlan_info: (необязательный, query).
        :param collect_configurations: (необязательный, query).
        :param connection_pool_size: (необязательный, query).
        :param name: (необязательный, query).
        :param return_fields: Список полей для возврата, по умолчанию все (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).

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
        return self._transport.request(
            "GET", "/devices/", path_params=path_params, query=query, body=None, response_model=Page[Devices]
        )

    def create(self, data: Devices) -> Devices:
        """Этот класс представляет собой ListAPIView, который возвращает список всех устройств в базе данных.

        :param data: Тело запроса. (обязательный, body).

        operationId: devices_create.
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
        """Возвращаем список всех устройств, без пагинации

        :param group: (необязательный, query).
        :param vendor: (необязательный, query).
        :param model: (необязательный, query).
        :param ip: (необязательный, query).
        :param serial_number: (необязательный, query).
        :param os_version: (необязательный, query).
        :param port_scan_protocol: (необязательный, query).
        :param cmd_protocol: (необязательный, query).
        :param active: (необязательный, query).
        :param collect_interfaces: Collect interfaces (необязательный, query).
        :param collect_mac_addresses: (необязательный, query).
        :param collect_vlan_info: (необязательный, query).
        :param collect_configurations: (необязательный, query).
        :param connection_pool_size: (необязательный, query).
        :param name: (необязательный, query).
        :param return_fields: Список полей для возврата, по умолчанию все (необязательный, query).

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
        return self._transport.request(
            "GET",
            "/devices/_all",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[Devices],
        )

    def get_by_zabbix(self, host_id: str) -> GetDeviceByZabbix:
        """Преобразование идентификатора узла сети "host_id" Zabbix в URL ecstasy.

        :param request: Запрос. :param host_id: Идентификатор узла сети в Zabbix.

        :param host_id: (обязательный, path).

        operationId: devices_by-zabbix_read.
        """

        path_params = {"host_id": host_id}
        query = None
        return self._transport.request(
            "GET",
            "/devices/by-zabbix/{host_id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=GetDeviceByZabbix,
        )

    def list_commands_history(
        self, *, page: int | None = None, page_size: int | None = None
    ) -> Page[BulkDeviceCommandExecution]:
        """List bulk command executions with nested device results.

        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).

        operationId: devices_commands_history_list.
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
        """List paginated device results for one execution.

        :param execution_id: (обязательный, path).
        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).

        operationId: devices_commands_history_results_list.
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

    def get_commands_tasks(self, task_id: str) -> BulkCommandTaskStatus:
        """Return current task state, progress and cached results.

        :param task_id: (обязательный, path).

        operationId: devices_commands_tasks_read.
        """

        path_params = {"task_id": task_id}
        query = None
        return self._transport.request(
            "GET",
            "/devices/commands/tasks/{task_id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=BulkCommandTaskStatus,
        )

    def create_commands_execute_multiple(
        self, command_id: str, data: ExecuteBulkDeviceCommandRequest
    ) -> BulkCommandLaunchResponse:
        """Validate request and dispatch celery task.

        :param command_id: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_commands_execute-multiple_create.
        """

        path_params = {"command_id": command_id}
        query = None
        return self._transport.request(
            "POST",
            "/devices/commands/{command_id}/execute-multiple",
            path_params=path_params,
            query=query,
            body=data,
            response_model=BulkCommandLaunchResponse,
        )

    def create_comments(self, data: InterfacesComments) -> InterfacesComments:
        """
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_comments_create.
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
        """
        :param id_: A unique integer value identifying this Комментарий к интерфейсу. (обязательный, path).

        operationId: devices_comments_read.
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
        """
        :param id_: A unique integer value identifying this Комментарий к интерфейсу. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_comments_update.
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
        """
        :param id_: A unique integer value identifying this Комментарий к интерфейсу. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_comments_partial_update.
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
        """
        :param id_: A unique integer value identifying this Комментарий к интерфейсу. (обязательный, path).

        operationId: devices_comments_delete.
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

    def create_cut_session(self, data: BrassSession) -> CutBrasSession:
        """## Сбрасываем сессию абонента и перезагружаем порт на оборудовании

        Данные формы: - str:`mac` - max:24 - str:`device` - max:255 - str:`port` - max:50 Сбрасываем сессию и перезагружаем порт на оборудовании Возвращаем: { "portReloadStatus": "RELOAD STATUS", "errors": [] }

        :param data: Тело запроса. (обязательный, body).

        operationId: devices_cut-session_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/devices/cut-session",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CutBrasSession,
        )

    def get_session(self, *, mac: str | None = None) -> BrasPairSessionResult:
        """## Возвращаем сессию на BRAS для конкретного MAC адреса

        Пример ответа: { "BRAS1": { "session": null, "errors": [ "Не удалось подключиться" ] }, "BRAS2": { "session": " ... ", "errors": [] } }

        :param mac: (обязательный, query).

        operationId: devices_session_list.
        """

        path_params = None
        query = {"mac": mac}
        return self._transport.request(
            "GET",
            "/devices/session",
            path_params=path_params,
            query=query,
            body=None,
            response_model=BrasPairSessionResult,
        )

    def get_workload_interfaces_all(
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
        """
        :param group: (необязательный, query).
        :param vendor: (необязательный, query).
        :param model: (необязательный, query).
        :param ip: (необязательный, query).
        :param serial_number: (необязательный, query).
        :param os_version: (необязательный, query).
        :param port_scan_protocol: (необязательный, query).
        :param cmd_protocol: (необязательный, query).
        :param active: (необязательный, query).
        :param collect_interfaces: Collect interfaces (необязательный, query).
        :param collect_mac_addresses: (необязательный, query).
        :param collect_vlan_info: (необязательный, query).
        :param collect_configurations: (необязательный, query).
        :param connection_pool_size: (необязательный, query).
        :param name: (необязательный, query).
        :param return_fields: Список полей для возврата, по умолчанию все (необязательный, query).

        operationId: devices_workload_interfaces__all_list.
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
            "/devices/workload/interfaces/_all",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicesInterfaceWorkloadResult,
        )

    def get_workload_interfaces(self, device_name_or_ip: str) -> InterfaceWorkload:
        """
        :param device_name_or_ip: (обязательный, path).

        operationId: devices_workload_interfaces_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/workload/interfaces/{device_name_or_ip}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfaceWorkload,
        )

    def get(self, device_name_or_ip: str) -> DevicesDetail:
        """
        :param device_name_or_ip: (обязательный, path).

        operationId: devices_read.
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
        """
        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_update.
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
        """
        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_partial_update.
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
        """
        :param device_name_or_ip: (обязательный, path).

        operationId: devices_delete.
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

    def list_actions(self, device_name_or_ip: str, *, page: int | None = None) -> Page[UserDeviceAction]:
        """
        :param device_name_or_ip: (обязательный, path).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: devices_actions_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"page": page}
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/actions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[UserDeviceAction],
        )

    def list_cable_diag(self, device_name_or_ip: str, *, port: str | None = None) -> _list[dict[str, Any]]:
        """## Запускаем диагностику кабеля на порту

        Для этого необходимо передать порт в параметре URL `?port=eth1` Функция возвращает данные в виде словаря. В зависимости от результата диагностики некоторые ключи могут отсутствовать за ненадобностью. { "len": "-", # Длина кабеля в метрах, либо "-", когда не определено "status": "", # Состояние на порту (Up, Down, Empty) "pair1": { "status": "", # Статус первой пары (Open, Short) "len": "", # Длина первой пары в метрах }, "pair2": { "status": "", # Статус второй пары (Open, Short) "len": "", # Длина второй пары в метрах } }

        :param device_name_or_ip: (обязательный, path).
        :param port: Порт (интерфейс) оборудования (обязательный, query).

        operationId: devices_cable-diag_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"port": port}
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/cable-diag",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[dict[str, Any]],
        )

    def create_change_description(
        self, device_name_or_ip: str, data: ChangeDescriptionRequest
    ) -> ChangeDescription:
        """## Меняем описание на порту оборудования

        Требуется передать JSON: { "port": "порт оборудования", "description": "новое описание порта" } Если указанного порта не существует на оборудовании, то будет отправлен ответ со статусом `400` { "detail": "Неверный порт {port}" } Если описание слишком длинное, то будет отправлен ответ со статусом `400` { "detail": "Слишком длинное описание! Укажите не более {max_length} символов." }

        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_change-description_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/change-description",
            path_params=path_params,
            query=query,
            body=data,
            response_model=ChangeDescription,
        )

    def create_change_dsl_profile(self, device_name_or_ip: str, data: ADSLProfile) -> dict[str, Any]:
        """Изменяем профиль xDSL порта на другой

        Возвращаем `{ "status": status }` или `{ "error": error }`

        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_change-dsl-profile_create.
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

    def create_collect_config(self, device_name_or_ip: str) -> CollectConfigResponse:
        """## В реальном времени смотрим и сохраняем конфигурацию оборудования

        Если такая конфигурация уже имеется, то файл не будет создан (чтобы не было лишних копий)

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_collect-config_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/collect-config",
            path_params=path_params,
            query=query,
            body=None,
            response_model=CollectConfigResponse,
        )

    def list_commands(self, device_name_or_ip: str) -> _list[DeviceCommands]:
        """Return available commands for the selected device.

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_commands_list.
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

    def create_commands_execute(
        self, device_name_or_ip: str, command_id: str, data: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute a command on a single device.

        :param device_name_or_ip: (обязательный, path).
        :param command_id: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_commands_execute_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "command_id": command_id}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/commands/{command_id}/execute",
            path_params=path_params,
            query=query,
            body=data,
            response_model=dict[str, Any],
        )

    def create_commands_validate(
        self, device_name_or_ip: str, command_id: str, data: dict[str, Any]
    ) -> dict[str, Any]:
        """Validate a command for a single device.

        :param device_name_or_ip: (обязательный, path).
        :param command_id: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_commands_validate_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "command_id": command_id}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/commands/{command_id}/validate",
            path_params=path_params,
            query=query,
            body=data,
            response_model=dict[str, Any],
        )

    def get_config(self, device_name_or_ip: str, file_name: str) -> dict[str, Any]:
        """## Отправляет содержимое файла конфигурации

        :param device_name_or_ip: (обязательный, path).
        :param file_name: (обязательный, path).

        operationId: devices_config_read.
        """

        path_params = {"device_name_or_ip": device_name_or_ip, "file_name": file_name}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/config/{file_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=dict[str, Any],
        )

    def delete_config(self, device_name_or_ip: str, file_name: str) -> None:
        """## Удаляет файл конфигурации

        :param device_name_or_ip: (обязательный, path).
        :param file_name: (обязательный, path).

        operationId: devices_config_delete.
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

    def list_configs(self, device_name_or_ip: str) -> _list[ConfigFile]:
        """## Перечень файлов конфигураций указанного оборудования

        Пример ответа: [ { "name": "config_file_96f7d499c739875.txt", "size": 19346, "modTime": "11:53 28.03.2023", } ]

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_configs_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/configs",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[ConfigFile],
        )

    def get_info(self, device_name_or_ip: str, *, page: int | None = None) -> DeviceInfo:
        """Возвращаем общую информацию оборудования

        Пример вывода: { "deviceName": "DEVICE-NAME", "deviceIP": "10.10.10.10", "elasticStackLink": "URL", "zabbixHostID": "45632", "zabbixInfo": { "description": "ОПИСАНИЕ ОБОРУДОВАНИЯ В ZABBIX", "inventory": { "type": "Eltex", "type_full": "MES3324F 28-port 1G/10G Managed Switch", "serialno_a": "", "macaddress_a": "", "hardware": "MES3324F 28-port 1G/10G Managed Switch", ... "model": "MES3324F", "vendor": "Eltex" } }, "permission": 3, "coords": [ 23.322332, 32.233223 ], "consoleURL": "", "uptime": 23434, }

        :param device_name_or_ip: (обязательный, path).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: devices_info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"page": page}
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DeviceInfo,
        )

    def get_interface_info(self, device_name_or_ip: str) -> InterfaceDetailInfo:
        """## Общая информация об определенном порте оборудования

        В зависимости от типа оборудования информация будет совершенно разной Поле `portDetailInfo.type` указывает тип данных, которые могут быть Строкой или Объектом. Возможные значения: "text", "html", "error", "adsl", "gpon", "eltex-gpon", "mikrotik". { "portDetailInfo": { "type": "text", - Тип данных для детальной информации о порте "data": "" - Сами данные }, "portConfig": "Конфигурация порта (из файла конфигурации)", "portType": "COPPER" - (SFP, COMBO), "portErrors": "Ошибки на порту", "hasCableDiag": true - Имеется ли на данном типе оборудования возможность диагностики порта }

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_interface-info_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/interface-info",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfaceDetailInfo,
        )

    def get_interfaces(
        self,
        device_name_or_ip: str,
        *,
        current_status: bool | None = None,
        vlans: bool | None = None,
        add_links: bool | None = None,
        add_comments: bool | None = None,
        add_zabbix_graph: bool | None = None,
    ) -> InterfacesList:
        """Вывод интерфейсов оборудования

        Пример вывода: { "interfaces": [ { "name": "gi1/0/1", "status": "up", "description": "To_DEVICE-1", "link": { "deviceName": "DEVICE-1", "url": "/device/DEVICE-1" }, "comments": [ { "text": "Какой-то комментарий", "user": "irudenko", "id": 14 } ], "vlans": [], }, ... { "name": "te1/0/4", "status": "down", "description": "" } ], "deviceAvailable": true, "collected": "2023-03-01T15:13:11.559175" }

        :param device_name_or_ip: (обязательный, path).
        :param current_status: (необязательный, query).
        :param vlans: (необязательный, query).
        :param add_links: (необязательный, query).
        :param add_comments: (необязательный, query).
        :param add_zabbix_graph: (необязательный, query).

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
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/interfaces",
            path_params=path_params,
            query=query,
            body=None,
            response_model=InterfacesList,
        )

    def get_macs(self, device_name_or_ip: str, *, port: str | None = None) -> MacListResult:
        """## Смотрим MAC-адреса на порту оборудования

        Для этого необходимо передать порт в параметре URL `?port=eth1` Если порт верный и там есть MAC-адреса, то будет вот такой ответ: { "count": 47, "result": [ { "vlanID": "1051", "mac": "00-04-96-51-AD-3D", "vlanName": "Описание VLAN" }, ... ] }

        :param device_name_or_ip: (обязательный, path).
        :param port: Порт (интерфейс) оборудования (обязательный, query).

        operationId: devices_macs_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"port": port}
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/macs",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MacListResult,
        )

    def list_media(self, device_name_or_ip: str, *, page: int | None = None) -> Page[DeviceMedia]:
        """
        :param device_name_or_ip: (обязательный, path).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: devices_media_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = {"page": page}
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/media",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[DeviceMedia],
        )

    def create_media(self, device_name_or_ip: str, data: DeviceMedia) -> DeviceMedia:
        """
        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_media_create.
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
        """
        :param device_name_or_ip: (обязательный, path).
        :param id_: A unique integer value identifying this Медиафайл. (обязательный, path).

        operationId: devices_media_read.
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
        """
        :param device_name_or_ip: (обязательный, path).
        :param id_: A unique integer value identifying this Медиафайл. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_media_update.
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
        """
        :param device_name_or_ip: (обязательный, path).
        :param id_: A unique integer value identifying this Медиафайл. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_media_partial_update.
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
        """
        :param device_name_or_ip: (обязательный, path).
        :param id_: A unique integer value identifying this Медиафайл. (обязательный, path).

        operationId: devices_media_delete.
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

    def get_pool(self, device_name_or_ip: str) -> DevicePoolStatuses:
        """Возвращает максимальное кол-во сессий в пуле подключений и список статусов работоспособности текущих пулов.

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_pool_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/pool",
            path_params=path_params,
            query=query,
            body=None,
            response_model=DevicePoolStatuses,
        )

    def delete_pool(self, device_name_or_ip: str) -> None:
        """Очищает пул всех текущих подключений

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_pool_delete.
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
        """## Изменяем состояние порта оборудования

        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_port-status_create.
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
        """Устанавливает PoE статус на порту

        :param device_name_or_ip: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: devices_set-poe-out_create.
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

    def list_stats(self, device_name_or_ip: str) -> _list[dict[str, Any]]:
        """Возвращаем данные CPU, FLASH, RAM, TEMP

        Пример вывода: { "cpu": { "util": [ 2 ] }, "ram": { "util": 15 }, "flash": { "util": 50 }, "temp": { "value": 43.5, "status": "normal" } }

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_stats_list.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "GET",
            "/devices/{device_name_or_ip}/stats",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[dict[str, Any]],
        )

    def list_viewings(self, device_name_or_ip: str) -> _list[DeviceViewings]:
        """
        :param device_name_or_ip: (обязательный, path).

        operationId: devices_viewings_list.
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

    def create_viewings(self, device_name_or_ip: str) -> Any:
        """
        :param device_name_or_ip: (обязательный, path).

        operationId: devices_viewings_create.
        """

        path_params = {"device_name_or_ip": device_name_or_ip}
        query = None
        return self._transport.request(
            "POST",
            "/devices/{device_name_or_ip}/viewings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_vlan_info(self, device_name_or_ip: str) -> _list[DeviceVlan]:
        """Возвращаем информацию о VLAN-ах

        :param device_name_or_ip: (обязательный, path).

        operationId: devices_vlan-info_list.
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
