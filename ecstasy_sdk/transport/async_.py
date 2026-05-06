"""Асинхронный HTTP-транспорт."""

from collections.abc import Mapping
from typing import Any

import httpx
from pydantic import BaseModel

from ecstasy_sdk.config import EcstasyConfig
from ecstasy_sdk.exceptions import EcstasyTimeoutError, EcstasyTransportError
from ecstasy_sdk.transport.base import BaseTransport


class AsyncTransport(BaseTransport):
    """Асинхронный транспорт Ecstasy API."""

    def __init__(self, config: EcstasyConfig, client: httpx.AsyncClient | None = None) -> None:
        """Создает асинхронный HTTP-клиент."""

        super().__init__(config)
        self.client = client or httpx.AsyncClient(
            timeout=config.timeout,
            verify=config.verify,
            follow_redirects=config.follow_redirects,
            headers=self.headers,
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        query: Mapping[str, Any] | BaseModel | None = None,
        body: BaseModel | Mapping[str, Any] | None = None,
        response_model: Any = None,
    ) -> Any:
        """Выполняет асинхронный HTTP-запрос к Ecstasy API."""

        url = self.build_url(path, path_params)
        try:
            response = await self.client.request(
                method,
                url,
                headers=self.headers,
                params=self.serialize_query(query),
                json=self.serialize_body(body) if body is not None else None,
            )
        except httpx.TimeoutException as exc:
            raise EcstasyTimeoutError(str(exc)) from exc
        except httpx.RequestError as exc:
            raise EcstasyTransportError(str(exc)) from exc
        self.raise_for_status(response)
        return self.parse_response(response, response_model)

    async def aclose(self) -> None:
        """Закрывает HTTP-клиент."""

        await self.client.aclose()
