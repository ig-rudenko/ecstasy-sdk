"""Общие модели SDK."""

from typing import Any

from ecstasy_sdk.models.base import EcstasyModel


class Page[T](EcstasyModel):
    """Страница результатов DRF pagination."""

    count: int
    next: str | None = None
    previous: str | None = None
    results: list[T]


class RawResponse(EcstasyModel):
    """Контейнер для неописанного swagger ответа."""

    data: dict[str, Any] | list[Any] | str | bytes | None = None


class EmptyResponse(EcstasyModel):
    """Пустой ответ API."""

    pass
