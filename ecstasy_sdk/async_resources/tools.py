from __future__ import annotations

from typing import Any

from ecstasy_sdk.models import (
    GetVendor,
    GetVlanDesc,
    SearchInterfaceByDescResult,
    VlanTraceroute,
)
from ecstasy_sdk.transport.async_ import AsyncTransport


class AsyncToolsResource:
    """Ресурсный клиент Ecstasy API для группы `Tools`."""

    def __init__(self, transport: AsyncTransport) -> None:
        """Сохраняет транспорт ресурса."""

        self._transport = transport

    async def get_find_by_desc(
        self, *, is_regex: bool | None = None, pattern: str | None = None
    ) -> SearchInterfaceByDescResult:
        """## Поиск портов по описанию и комментариям.

        :param is_regex: (необязательный, query).
        :param pattern: (обязательный, query).

        operationId: tools_find-by-desc_list.
        """

        path_params = None
        query = {"is_regex": is_regex, "pattern": pattern}
        return await self._transport.request(
            "GET",
            "/tools/find-by-desc",
            path_params=path_params,
            query=query,
            body=None,
            response_model=SearchInterfaceByDescResult,
        )

    async def get_ip_mac_info(self, ip_or_mac: str) -> Any:
        """Считывает из БД таблицу с оборудованием, на которых необходимо искать MAC через таблицу arp

        В многопоточном режиме собирает данные ip, mac, vlan, agent-remote-id, agent-circuit-id из оборудования и проверяет, есть ли в Zabbix узел сети с таким IP и добавляет имя и hostid

        :param ip_or_mac: (обязательный, path).

        operationId: tools_ip-mac-info_read.
        """

        path_params = {"ip_or_mac": ip_or_mac}
        query = None
        return await self._transport.request(
            "GET",
            "/tools/ip-mac-info/{ip_or_mac}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )

    async def get_mac_vendor(self, mac: str) -> GetVendor:
        """Определяет производителя по MAC адресу

        :param mac: (обязательный, path).

        operationId: tools_mac-vendor_read.
        """

        path_params = {"mac": mac}
        query = None
        return await self._transport.request(
            "GET",
            "/tools/mac-vendor/{mac}",
            path_params=path_params,
            query=query,
            body=None,
            response_model=GetVendor,
        )

    async def get_vlan_desc(self, *, vlan: int | None = None) -> GetVlanDesc:
        """## Возвращаем имя VLAN, который был передан в HTTP запросе

        :param vlan: (обязательный, query).

        operationId: tools_vlan-desc_list.
        """

        path_params = None
        query = {"vlan": vlan}
        return await self._transport.request(
            "GET",
            "/tools/vlan-desc",
            path_params=path_params,
            query=query,
            body=None,
            response_model=GetVlanDesc,
        )

    async def get_vlan_traceroute(
        self,
        *,
        vlan: int | None = None,
        ep: bool | None = None,
        ad: bool | None = None,
        double_check: bool | None = None,
        graph_min_length: int | None = None,
    ) -> VlanTraceroute:
        """## Трассировка VLAN и отправка карты

        Эта функция обрабатывает GET-запрос для трассировки VLAN. Она использует декоратор @login_required для проверки авторизации пользователя. Если в запросе не содержится параметр vlan, функция возвращает пустой JSON объект. Затем, используя метод load() класса VlanTracerouteConfig, загружает настройки трассировки VLAN из базы данных. Функция также идентифицирует список устройств, откуда будет начинаться трассировка VLAN, и определяет паттерн для поиска интерфейсов. Далее функция использует цикл for для перебора списка устройств, используемых для запуска трассировки VLAN. Для каждого устройства функция вызывает функцию find_vlan(), которая ищет VLAN с помощью рекурсивного алгоритма и возвращает список узлов сети, соседей и линий связи для визуализации. Если функция find_vlan() вращает результат, то цикл завершается. Если же результат не был найден ни для одного устройства из списка, функция возвращает HttpResponse "empty". Если результат был найден, функция создаёт экземпляр класса Network и добавляет к нему узлы сети, соседей и линии связи из результата. Затем функция отправляет карту в виде JSON-объекта как ответ на запрос.

        :param vlan: (обязательный, query).
        :param ep: Показывать пустые порты (необязательный, query).
        :param ad: Указывать выключенные порты (необязательный, query).
        :param double_check: Двухстороннее соответствие VLAN на соседних портах (необязательный, query).
        :param graph_min_length: Минимальное количество узлов в одном графе (необязательный, query).

        operationId: tools_vlan-traceroute_list.
        """

        path_params = None
        query = {
            "vlan": vlan,
            "ep": ep,
            "ad": ad,
            "double_check": double_check,
            "graph_min_length": graph_min_length,
        }
        return await self._transport.request(
            "GET",
            "/tools/vlan-traceroute",
            path_params=path_params,
            query=query,
            body=None,
            response_model=VlanTraceroute,
        )

    async def get_vlans_scan_check(self) -> Any:
        """
        operationId: tools_vlans-scan_check_list.
        """

        path_params = None
        query = None
        return await self._transport.request(
            "GET",
            "/tools/vlans-scan/check",
            path_params=path_params,
            query=query,
            body=None,
            response_model=None,
        )
