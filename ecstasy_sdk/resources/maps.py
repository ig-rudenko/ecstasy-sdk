from __future__ import annotations

from ecstasy_sdk.models import (
    Layer,
    Map,
    MapDetail,
    MapLayer,
    MapLayerRender,
    MapUpdateLayers,
    Page,
)
from ecstasy_sdk.transport.sync import SyncTransport


class MapsResource:
    """Ресурсный клиент Ecstasy API для группы `Maps`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def list(self, *, page: int | None = None) -> Page[Map]:
        """
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: maps_list.
        """

        path_params = None
        query = {"page": page}
        return self._transport.request(
            "GET", "/maps/", path_params=path_params, query=query, body=None, response_model=Page[Map]
        )

    def list_layers(
        self, *, id_: str | None = None, name: str | None = None, page: int | None = None
    ) -> Page[Layer]:
        """
        :param id_: (необязательный, query).
        :param name: (необязательный, query).
        :param page: A page number within the paginated result set. (необязательный, query).

        operationId: maps_layers_list.
        """

        path_params = None
        query = {"id": id_, "name": name, "page": page}
        return self._transport.request(
            "GET",
            "/maps/layers/",
            path_params=path_params,
            query=query,
            body=None,
            response_model=Page[Layer],
        )

    def update_layers(self, id_: int, data: Layer) -> Layer:
        """
        :param id_: A unique integer value identifying this Слой. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: maps_layers_update.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "PUT", "/maps/layers/{id}/", path_params=path_params, query=query, body=data, response_model=Layer
        )

    def patch_layers(self, id_: int, data: Layer) -> Layer:
        """
        :param id_: A unique integer value identifying this Слой. (обязательный, path).
        :param data: Тело запроса. (обязательный, body).

        operationId: maps_layers_partial_update.
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
        """
        :param id_: A unique integer value identifying this Карту. (обязательный, path).

        operationId: maps_read.
        """

        path_params = {"id": id_}
        query = None
        return self._transport.request(
            "GET", "/maps/{id}", path_params=path_params, query=query, body=None, response_model=MapDetail
        )

    def get_layers(self, map_id: str) -> MapLayer:
        """
        :param map_id: (обязательный, path).

        operationId: maps_layers_read.
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

    def get_render(self, map_id: str) -> MapLayerRender:
        """Эта функция извлекает данные из слоев объекта карты и возвращает их в формате списка.

        :param map_id: (обязательный, path).

        operationId: maps_render_read.
        """

        path_params = {"map_id": map_id}
        query = None
        return self._transport.request(
            "GET",
            "/maps/{map_id}/render",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MapLayerRender,
        )

    def get_update(self, map_id: str) -> MapUpdateLayers:
        """# Проверяем какие из узлов сети недоступны на интерактивной карте с заданным идентификатором

        Возвращаем JSON ответ с проблемными узлами сети и подтверждение проблем (если они есть в Zabbix): { "problems": [ {"id": "host_id", "acknowledges": [["text", "datetime"], ... ]}, {"id": "host_id", "acknowledges": [["text", "datetime"], ... ]}, ... ] }

        :param map_id: (обязательный, path).

        operationId: maps_update_read.
        """

        path_params = {"map_id": map_id}
        query = None
        return self._transport.request(
            "GET",
            "/maps/{map_id}/update",
            path_params=path_params,
            query=query,
            body=None,
            response_model=MapUpdateLayers,
        )
