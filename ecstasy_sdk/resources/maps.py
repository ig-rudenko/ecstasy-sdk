from __future__ import annotations

from builtins import list as _list
from typing import Any

from ecstasy_sdk.models import (
    Layer,
    Map,
    MapDetail,
    MapLayer,
    Page,
)
from ecstasy_sdk.transport.sync import SyncTransport


class MapsResource:
    """Ресурсный клиент Ecstasy API для группы `Maps`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def list(self, *, page: int | None = None) -> Page[Map]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_list.
        """

        path_params = None
        query = {"page": page}
        return self._transport.request(
            "GET", "/maps/", path_params=path_params, query=query, body=None, response_model=Page[Map]
        )

    def list_layers(self, *, id_: str | None = None, name: str | None = None) -> _list[Layer]:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_layers_list.
        """

        path_params = None
        query = {"id": id_, "name": name}
        return self._transport.request(
            "GET",
            "/maps/layers/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[Layer],
        )

    def update_layers(self, id_: int, data: Layer) -> Layer:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_layers_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT", "/maps/layers/{id}/", path_params=path_params, query=query, body=data, response_model=Layer
        )

    def patch_layers(self, id_: int, data: Layer) -> Layer:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_layers_partial_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PATCH",
            "/maps/layers/{id}/",
            path_params=path_params,
            query=query,
            body=data,
            response_model=Layer,
        )

    def get(self, id_: int) -> MapDetail:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET", "/maps/{id}", path_params=path_params, query=query, body=None, response_model=MapDetail
        )

    def get_layers(self, map_id: str) -> MapLayer:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_layers_read.
        """

        path_params = {"map_id": map_id}
        query = None
        return self._transport.request(
            "GET",
            "/maps/{map_id}/layers",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MapLayer,
        )

    def get_render(self, map_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_render_read.
        """

        path_params = {"map_id": map_id}
        query = None
        return self._transport.request(
            "GET",
            "/maps/{map_id}/render",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def get_update(self, map_id: str) -> Any:
        """Выполняет операцию Ecstasy API.

        Swagger operationId: maps_update_read.
        """

        path_params = {"map_id": map_id}
        query = None
        return self._transport.request(
            "GET",
            "/maps/{map_id}/update",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )
