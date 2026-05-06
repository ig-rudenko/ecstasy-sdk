"""Базовые Pydantic-модели SDK."""

from pydantic import BaseModel, ConfigDict


class EcstasyModel(BaseModel):
    """Базовая модель SDK с мягкой совместимостью со swagger."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        arbitrary_types_allowed=True,
    )
