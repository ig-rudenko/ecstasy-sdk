from __future__ import annotations

from builtins import list as _list
from typing import Any

from ecstasy_sdk.models import (
    AccessRing,
    TransportRing,
)
from ecstasy_sdk.transport.sync import SyncTransport


class RingManagerResource:
    """Ресурсный клиент Ecstasy API для группы `Ring Manager`."""

    def __init__(self, transport: SyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    def get_access_ring(self, head_name: str) -> Any:
        """Эта функция извлекает объект транспортного кольца, нормализует его, собирает все интерфейсы из его истории, находит связь между устройствами и возвращает сериализованный ответ данных устройств кольца.

        :param head_name: (обязательный, path).

        operationId: ring-manager_access-ring_read.
        """

        path_params = {"head_name": head_name}
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/access-ring/{head_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_access_rings(self) -> _list[AccessRing]:
        """
        operationId: ring-manager_access-rings_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/access-rings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[AccessRing],
        )

    def get_transport_ring(self, ring_name: str) -> Any:
        """Эта функция извлекает объект транспортного кольца, нормализует его, собирает все интерфейсы из его истории, находит связь между устройствами и возвращает сериализованный ответ данных устройств кольца.

        :param ring_name: (обязательный, path).

        operationId: ring-manager_transport-ring_read.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def get_transport_ring_solutions(self, ring_name: str) -> Any:
        """Эта функция извлекает информацию о транспортном кольце, проверяет доступность устройств, собирает интерфейсы, находит связи между устройствами и возвращает points и решения `solutions`, которые можно будет применить, чтобы перевести кольцо в оптимальное состояние.

        :param ring_name: (обязательный, path).

        operationId: ring-manager_transport-ring_solutions_list.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}/solutions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def create_transport_ring_solutions(self, ring_name: str) -> Any:
        """Эта функция выполняет набор действий над объектом транспортного кольца и возвращает выполненные действия, а также их статус

        :param ring_name: (обязательный, path).

        operationId: ring-manager_transport-ring_solutions_create.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return self._transport.request(
            "POST",
            "/ring-manager/transport-ring/{ring_name}/solutions",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def get_transport_ring_solutions_last(self, ring_name: str) -> Any:
        """
        :param ring_name: (обязательный, path).

        operationId: ring-manager_transport-ring_solutions_last_list.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}/solutions/last",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def get_transport_ring_status(self, ring_name: str) -> Any:
        """Эта функция извлекает состояние транспортного кольца и возвращает информацию о том, активно ли оно и разворачивается ли в данный момент.

        :param ring_name: (обязательный, path).

        operationId: ring-manager_transport-ring_status_list.
        """

        path_params = {"ring_name": ring_name}
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/transport-ring/{ring_name}/status",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    def list_transport_rings(self) -> _list[TransportRing]:
        """Это класс, который возвращает набор запросов объектов TransportRing, отфильтрованных текущим пользователем и упорядоченных по имени.

        operationId: ring-manager_transport-rings_list.
        """

        path_params = None
        query = None
        return self._transport.request(
            "GET",
            "/ring-manager/transport-rings",
            path_params=path_params,
            query=query,
            body=None,
            response_model=_list[TransportRing],
        )
