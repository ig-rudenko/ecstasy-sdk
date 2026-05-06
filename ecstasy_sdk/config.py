"""Конфигурация клиента Ecstasy API."""

from typing import Any

import httpx
from pydantic import BaseModel, ConfigDict, SecretStr, field_validator


class EcstasyConfig(BaseModel):
    """Конфигурация клиента Ecstasy API."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    base_url: str
    token: SecretStr
    api_base_path: str = "/api/v1"
    timeout: float | httpx.Timeout = 30.0
    verify: bool = True
    follow_redirects: bool = False
    user_agent: str = "ecstasy-sdk"

    @field_validator("base_url")
    @classmethod
    def normalize_base_url(cls, value: Any) -> str:
        """Нормализует базовый URL без завершающего слеша."""

        return str(value).rstrip("/")

    @field_validator("api_base_path")
    @classmethod
    def normalize_api_base_path(cls, value: str) -> str:
        """Нормализует базовый путь API."""

        value = value.strip() or "/api/v1"
        if not value.startswith("/"):
            value = f"/{value}"
        return value.rstrip("/")

    @property
    def authorization_header(self) -> str:
        """Возвращает значение заголовка Authorization."""

        return self.token.get_secret_value()
