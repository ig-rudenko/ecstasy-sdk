from __future__ import annotations

from builtins import list as _list
from typing import Any

from ecstasy_sdk.models import (
    AddEnd3ToHouseOLTState,
    BuildingAddress,
    CommonCustomerSerializer,
    CreateTechData,
    CustomerDetail,
    End3,
    End3TechCapability,
    OLTSubscriber,
    Page,
    StructuresHouseOLTState,
    SubscriberData,
    TechCapability,
    UpdateHouseOLTState,
    UpdateRetrieveOLTState,
    UpdateSubscriberData,
    ViewHouseBTechData,
    ViewOLTStatesTechData,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncGponResource:
    """Ресурсный клиент Ecstasy API для группы `GPON`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def list_addresses_buildings(self) -> _list[BuildingAddress]:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_addresses_buildings_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/addresses/buildings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[BuildingAddress],
        )

    async def list_addresses_end3(self) -> _list[End3]:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_addresses_end3_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/addresses/end3",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[End3],
        )

    async def list_customers(self) -> _list[CommonCustomerSerializer]:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_customers_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/customers",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[CommonCustomerSerializer],
        )

    async def get_customers(self, id_: str) -> CustomerDetail:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_customers_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=CustomerDetail,
        )

    async def update_customers(self, id_: str, data: CustomerDetail) -> CustomerDetail:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_customers_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CustomerDetail,
        )

    async def patch_customers(self, id_: str, data: CustomerDetail) -> CustomerDetail:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_customers_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CustomerDetail,
        )

    async def delete_customers(self, id_: str) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_customers_delete.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "DELETE",
            "/gpon/customers/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_devices_names(self) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_devices-names_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET", "/gpon/devices-names", path_params=path_params, query=query, body=None, response_model=None
        )

    async def list_permissions(self) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_permissions_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET", "/gpon/permissions", path_params=path_params, query=query, body=None, response_model=None
        )

    async def get_ports_names(self, device_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_ports-names_read.
        """

        path_params = {"device_name": device_name}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/ports-names/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_statistic_subscribers_count(self, device_name: str) -> _list[OLTSubscriber]:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_statistic_subscribers-count_list.
        """

        path_params = {"device_name": device_name}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/statistic/subscribers-count/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[OLTSubscriber],
        )

    async def get_subscriber_connection(self, id_: int) -> UpdateSubscriberData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscriber-connection_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=UpdateSubscriberData,
        )

    async def update_subscriber_connection(
        self, id_: int, data: UpdateSubscriberData
    ) -> UpdateSubscriberData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscriber-connection_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateSubscriberData,
        )

    async def patch_subscriber_connection(self, id_: int, data: UpdateSubscriberData) -> UpdateSubscriberData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscriber-connection_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateSubscriberData,
        )

    async def delete_subscriber_connection(self, id_: int) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscriber-connection_delete.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "DELETE",
            "/gpon/subscriber-connection/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_subscriber_data(self) -> _list[SubscriberData]:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscriber-data_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/subscriber-data",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[SubscriberData],
        )

    async def create_subscriber_data(self, data: SubscriberData) -> SubscriberData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscriber-data_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST",
            "/gpon/subscriber-data",
            path_params=path_params,
            query=query,
            body=data,
            response_model=SubscriberData,
        )

    async def get_subscribers_on_device(self, device_name: str) -> Any:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_subscribers-on-device_read.
        """

        path_params = {"device_name": device_name}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/subscribers-on-device/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def list_tech_data(self) -> _list[CreateTechData]:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[CreateTechData],
        )

    async def create_tech_data(self, data: CreateTechData) -> CreateTechData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST",
            "/gpon/tech-data",
            path_params=path_params,
            query=query,
            body=data,
            response_model=CreateTechData,
        )

    async def get_tech_data_building(self, id_: str) -> ViewHouseBTechData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_building_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/building/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=ViewHouseBTechData,
        )

    async def list_tech_data_end3(
        self,
        *,
        house: str | None = None,
        block: str | None = None,
        tech_capability_status: str | None = None,
        street: str | None = None,
        page: int | None = None,
    ) -> Page[End3TechCapability]:
        """Выполняет операцию Ecstasy API.

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
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/end3",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[End3TechCapability],
        )

    async def create_tech_data_end3(self, data: AddEnd3ToHouseOLTState) -> AddEnd3ToHouseOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_end3_create.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "POST",
            "/gpon/tech-data/end3",
            path_params=path_params,
            query=query,
            body=data,
            response_model=AddEnd3ToHouseOLTState,
        )

    async def get_tech_data_end3(self, id_: str) -> End3TechCapability:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_end3_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=End3TechCapability,
        )

    async def update_tech_data_end3(self, id_: str, data: End3TechCapability) -> End3TechCapability:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_end3_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=End3TechCapability,
        )

    async def patch_tech_data_end3(self, id_: str, data: End3TechCapability) -> End3TechCapability:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_end3_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=End3TechCapability,
        )

    async def delete_tech_data_end3(self, id_: str) -> None:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_end3_delete.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "DELETE",
            "/gpon/tech-data/end3/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def get_tech_data_house_olt_state(self, id_: str) -> StructuresHouseOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_house-olt-state_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/house-olt-state/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=StructuresHouseOLTState,
        )

    async def update_tech_data_house_olt_state(
        self, id_: str, data: UpdateHouseOLTState
    ) -> UpdateHouseOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_house-olt-state_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/gpon/tech-data/house-olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateHouseOLTState,
        )

    async def patch_tech_data_house_olt_state(
        self, id_: str, data: UpdateHouseOLTState
    ) -> UpdateHouseOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_house-olt-state_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/gpon/tech-data/house-olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateHouseOLTState,
        )

    async def get_tech_data_olt_state(self, id_: str) -> UpdateRetrieveOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_olt-state_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/olt-state/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=UpdateRetrieveOLTState,
        )

    async def update_tech_data_olt_state(
        self, id_: str, data: UpdateRetrieveOLTState
    ) -> UpdateRetrieveOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_olt-state_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/gpon/tech-data/olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateRetrieveOLTState,
        )

    async def patch_tech_data_olt_state(
        self, id_: str, data: UpdateRetrieveOLTState
    ) -> UpdateRetrieveOLTState:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_olt-state_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/gpon/tech-data/olt-state/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=UpdateRetrieveOLTState,
        )

    async def get_tech_data_tech_capability(self, id_: str) -> TechCapability:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_tech-capability_read.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/tech-capability/{id}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=TechCapability,
        )

    async def update_tech_data_tech_capability(self, id_: str, data: TechCapability) -> TechCapability:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_tech-capability_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PUT",
            "/gpon/tech-data/tech-capability/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=TechCapability,
        )

    async def patch_tech_data_tech_capability(self, id_: str, data: TechCapability) -> TechCapability:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_tech-capability_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return await self._transport.request(
            "PATCH",
            "/gpon/tech-data/tech-capability/{id}",
            path_params=path_params,
            query=query,
            body=data,
            response_model=TechCapability,
        )

    async def get_tech_data(self, device_name: str) -> ViewOLTStatesTechData:
        """Выполняет операцию Ecstasy API.

        operationId: gpon_tech-data_read.
        """

        path_params = {"device_name": device_name}
        query = None
        return await self._transport.request(
            "GET",
            "/gpon/tech-data/{device_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=ViewOLTStatesTechData,
        )
