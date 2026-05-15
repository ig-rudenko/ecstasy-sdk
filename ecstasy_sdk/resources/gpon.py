from __future__ import annotations

from builtins import list as _list

from ecstasy_sdk.models import (
    AddEnd3ToHouseOLTState,
    BuildingAddress,
    CommonCustomerSerializer,
    CommonSubscriberConnectionSerializer,
    CreateTechData,
    CustomerDetail,
    End3,
    End3TechCapability,
    OLTSubscriber,
    Page,
    PaginatedSubscriberConnectionListResponse,
    PaginatedTechDataListResponse,
    StructuresHouseOLTState,
    SubscriberData,
    TechCapability,
    UpdateHouseOLTState,
    UpdateRetrieveOLTState,
    UpdateSubscriberData,
    ViewHouseBTechData,
    ViewOLTStatesTechData,
)
from ecstasy_sdk.transport.sync import SyncTransport


class GponResource:
    """Ресурсный клиент Ecstasy API для группы `GPON`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def list_addresses_buildings(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
        device: str | None = None,
        port: str | None = None,
        search: str | None = None,
    ) -> Page[BuildingAddress]:
        """
        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).
        :param device: (необязательный, query).
        :param port: (необязательный, query).
        :param search: (необязательный, query).

        operationId: gpon_addresses_buildings_list.
        """

        path_params = None
        query = {"page": page, "page_size": page_size, "device": device, "port": port, "search": search}
        return self._transport.request(
            "GET",
            "/gpon/addresses/buildings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[BuildingAddress],
        )

    def list_addresses_end3(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
        address_id: int | None = None,
        search: str | None = None,
    ) -> _list[End3]:
        """Возвращает список сплиттеров/райзеров вместе с их адресами

        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).
        :param address_id: (необязательный, query).
        :param search: (необязательный, query).

        operationId: gpon_addresses_end3_list.
        """

        path_params = None
        query = {"page": page, "page_size": page_size, "address_id": address_id, "search": search}
        return self._transport.request(
            "GET",
            "/gpon/addresses/end3",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[End3],
        )

    def list_customers(
        self, *, page: int | None = None, page_size: int | None = None, search: str | None = None
    ) -> Page[CommonCustomerSerializer]:
        """
        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).
        :param search: (необязательный, query).

        operationId: gpon_customers_list.
        """

        path_params = None
        query = {"page": page, "page_size": page_size, "search": search}
        return self._transport.request(
            "GET",
            "/gpon/customers",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[CommonCustomerSerializer],
        )

    def get_customers(self, id_: str) -> CustomerDetail:
        """
        :param id_: (обязательный, path).

        operationId: gpon_customers_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=CustomerDetail,
        )

    def update_customers(self, id_: str, data: CustomerDetail) -> CustomerDetail:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_customers_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CustomerDetail,
        )

    def patch_customers(self, id_: str, data: CustomerDetail) -> CustomerDetail:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_customers_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CustomerDetail,
        )

    def delete_customers(self, id_: str) -> None:
        """
        :param id_: (обязательный, path).

        operationId: gpon_customers_delete.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "DELETE",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_devices_names(self) -> _list[str]:
        """
        operationId: gpon_devices-names_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/gpon/devices-names",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[str],
        )

    def list_permissions(self) -> _list[str]:
        """
        operationId: gpon_permissions_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/gpon/permissions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[str],
        )

    def get_ports_names(self, device_name: str) -> _list[str]:
        """
        :param device_name: (обязательный, path).

        operationId: gpon_ports-names_read.
        """

        path_params = {"device_name": device_name}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/ports-names/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[str],
        )

    def list_statistic_subscribers_count(self, device_name: str) -> _list[OLTSubscriber]:
        """
        :param device_name: (обязательный, path).

        operationId: gpon_statistic_subscribers-count_list.
        """

        path_params = {"device_name": device_name}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/statistic/subscribers-count/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[OLTSubscriber],
        )

    def get_subscriber_connection(self, id_: int) -> UpdateSubscriberData:
        """
        :param id_: A unique integer value identifying this subscriber connection. (обязательный, path).

        operationId: gpon_subscriber-connection_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=UpdateSubscriberData,
        )

    def update_subscriber_connection(self, id_: int, data: UpdateSubscriberData) -> UpdateSubscriberData:
        """
        :param id_: A unique integer value identifying this subscriber connection. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_subscriber-connection_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateSubscriberData,
        )

    def patch_subscriber_connection(self, id_: int, data: UpdateSubscriberData) -> UpdateSubscriberData:
        """
        :param id_: A unique integer value identifying this subscriber connection. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_subscriber-connection_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateSubscriberData,
        )

    def delete_subscriber_connection(self, id_: int) -> None:
        """
        :param id_: A unique integer value identifying this subscriber connection. (обязательный, path).

        operationId: gpon_subscriber-connection_delete.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "DELETE",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_subscriber_data(
        self,
        *,
        general: str | None = None,
        region: str | None = None,
        settlement: str | None = None,
        plan_structure: str | None = None,
        street: str | None = None,
        house: str | None = None,
        block: str | None = None,
        customer_name: str | None = None,
        contract: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedSubscriberConnectionListResponse:
        """
        :param general: (необязательный, query).
        :param region: (необязательный, query).
        :param settlement: (необязательный, query).
        :param plan_structure: (необязательный, query).
        :param street: (необязательный, query).
        :param house: (необязательный, query).
        :param block: (необязательный, query).
        :param customer_name: (необязательный, query).
        :param contract: (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).

        operationId: gpon_subscriber-data_list.
        """

        path_params = None
        query = {
            "general": general,
            "region": region,
            "settlement": settlement,
            "planStructure": plan_structure,
            "street": street,
            "house": house,
            "block": block,
            "customerName": customer_name,
            "contract": contract,
            "page": page,
            "page_size": page_size,
        }
        return self._transport.request(
            "GET",
            "/gpon/subscriber-data",
            path_params=path_params,
            query=query,
            body=None,
            response_model=PaginatedSubscriberConnectionListResponse,
        )

    def create_subscriber_data(self, data: SubscriberData) -> SubscriberData:
        """
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_subscriber-data_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/gpon/subscriber-data",
            path_params=path_params,
            query=query,
            body=data,
            response_model=SubscriberData,
        )

    def get_subscribers_on_device(
        self, device_name: str, *, port: str | None = None, ont_id: int | None = None
    ) -> _list[CommonSubscriberConnectionSerializer]:
        """
        :param device_name: (обязательный, path).
        :param port: (обязательный, query).
        :param ont_id: (необязательный, query).

        operationId: gpon_subscribers-on-device_read.
        """

        path_params = {"device_name": device_name}
        query = {"port": port, "ont_id": ont_id}
        return self._transport.request(
            "GET",
            "/gpon/subscribers-on-device/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[CommonSubscriberConnectionSerializer],
        )

    def list_tech_data(
        self,
        *,
        region: str | None = None,
        settlement: str | None = None,
        plan_structure: str | None = None,
        street: str | None = None,
        house: str | None = None,
        block: str | None = None,
        device_name: str | None = None,
        device_port: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedTechDataListResponse:
        """Предназначен для создания и просмотра технических данных

        :param region: (необязательный, query).
        :param settlement: (необязательный, query).
        :param plan_structure: (необязательный, query).
        :param street: (необязательный, query).
        :param house: (необязательный, query).
        :param block: (необязательный, query).
        :param device_name: (необязательный, query).
        :param device_port: (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).
        :param page_size: Number of results to return per page. (необязательный, query).

        operationId: gpon_tech-data_list.
        """

        path_params = None
        query = {
            "region": region,
            "settlement": settlement,
            "planStructure": plan_structure,
            "street": street,
            "house": house,
            "block": block,
            "deviceName": device_name,
            "devicePort": device_port,
            "page": page,
            "page_size": page_size,
        }
        return self._transport.request(
            "GET",
            "/gpon/tech-data",
            path_params=path_params,
            query=query,
            body=None,
            response_model=PaginatedTechDataListResponse,
        )

    def create_tech_data(self, data: CreateTechData) -> CreateTechData:
        """Предназначен для создания и просмотра технических данных

        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/gpon/tech-data",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CreateTechData,
        )

    def get_tech_data_building(self, id_: str) -> ViewHouseBTechData:
        """
        :param id_: (обязательный, path).

        operationId: gpon_tech-data_building_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/tech-data/building/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=ViewHouseBTechData,
        )

    def list_tech_data_end3(
        self,
        *,
        house: str | None = None,
        block: str | None = None,
        tech_capability_status: str | None = None,
        street: str | None = None,
        page: int | None = None,
    ) -> Page[End3TechCapability]:
        """
        :param house: Дом (необязательный, query).
        :param block: Блок (необязательный, query).
        :param tech_capability_status: Статус тех. возможности (необязательный, query).
        :param street: Улица (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: gpon_tech-data_end3_list.
        """

        path_params = None
        query = {
            "house": house,
            "block": block,
            "tech_capability_status": tech_capability_status,
            "street": street,
            "page": page,
        }
        return self._transport.request(
            "GET",
            "/gpon/tech-data/end3",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[End3TechCapability],
        )

    def create_tech_data_end3(self, data: AddEnd3ToHouseOLTState) -> AddEnd3ToHouseOLTState:
        """
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_end3_create.
        """

        path_params = None
        query = None
        return self._transport.request(
            "POST",
            "/gpon/tech-data/end3",
            path_params=path_params,
            query=query,
            body=data,
            response_model=AddEnd3ToHouseOLTState,
        )

    def get_tech_data_end3(self, id_: str) -> End3TechCapability:
        """
        :param id_: (обязательный, path).

        operationId: gpon_tech-data_end3_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=End3TechCapability,
        )

    def update_tech_data_end3(self, id_: str, data: End3TechCapability) -> End3TechCapability:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_end3_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=End3TechCapability,
        )

    def patch_tech_data_end3(self, id_: str, data: End3TechCapability) -> End3TechCapability:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_end3_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=End3TechCapability,
        )

    def delete_tech_data_end3(self, id_: str) -> None:
        """
        :param id_: (обязательный, path).

        operationId: gpon_tech-data_end3_delete.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "DELETE",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def get_tech_data_house_olt_state(self, id_: str) -> StructuresHouseOLTState:
        """
        :param id_: (обязательный, path).

        operationId: gpon_tech-data_house-olt-state_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/tech-data/house-olt-state/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=StructuresHouseOLTState,
        )

    def update_tech_data_house_olt_state(self, id_: str, data: UpdateHouseOLTState) -> UpdateHouseOLTState:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_house-olt-state_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/gpon/tech-data/house-olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateHouseOLTState,
        )

    def patch_tech_data_house_olt_state(self, id_: str, data: UpdateHouseOLTState) -> UpdateHouseOLTState:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_house-olt-state_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/gpon/tech-data/house-olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateHouseOLTState,
        )

    def get_tech_data_olt_state(self, id_: str) -> UpdateRetrieveOLTState:
        """
        :param id_: (обязательный, path).

        operationId: gpon_tech-data_olt-state_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/tech-data/olt-state/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=UpdateRetrieveOLTState,
        )

    def update_tech_data_olt_state(self, id_: str, data: UpdateRetrieveOLTState) -> UpdateRetrieveOLTState:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_olt-state_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/gpon/tech-data/olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateRetrieveOLTState,
        )

    def patch_tech_data_olt_state(self, id_: str, data: UpdateRetrieveOLTState) -> UpdateRetrieveOLTState:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_olt-state_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/gpon/tech-data/olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateRetrieveOLTState,
        )

    def get_tech_data_tech_capability(self, id_: str) -> TechCapability:
        """
        :param id_: (обязательный, path).

        operationId: gpon_tech-data_tech-capability_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET",
            "/gpon/tech-data/tech-capability/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=TechCapability,
        )

    def update_tech_data_tech_capability(self, id_: str, data: TechCapability) -> TechCapability:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_tech-capability_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT",
            "/gpon/tech-data/tech-capability/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=TechCapability,
        )

    def patch_tech_data_tech_capability(self, id_: str, data: TechCapability) -> TechCapability:
        """
        :param id_: (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: gpon_tech-data_tech-capability_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/gpon/tech-data/tech-capability/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=TechCapability,
        )

    def get_tech_data(self, device_name: str, *, port: str | None = None) -> ViewOLTStatesTechData:
        """
        :param device_name: (обязательный, path).
        :param port: (обязательный, query).

        operationId: gpon_tech-data_read.
        """

        path_params = {"device_name": device_name}
        query = {"port": port}
        return self._transport.request(
            "GET",
            "/gpon/tech-data/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=ViewOLTStatesTechData,
        )
