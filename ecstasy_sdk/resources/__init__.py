"""Синхронные ресурсные клиенты SDK."""

from ecstasy_sdk.resources.accounts import AccountsResource
from ecstasy_sdk.resources.devices import DevicesResource
from ecstasy_sdk.resources.gather import GatherResource
from ecstasy_sdk.resources.gpon import GponResource
from ecstasy_sdk.resources.maps import MapsResource
from ecstasy_sdk.resources.ring_manager import RingManagerResource
from ecstasy_sdk.resources.tools import ToolsResource

__all__ = [
    "AccountsResource",
    "DevicesResource",
    "GponResource",
    "GatherResource",
    "MapsResource",
    "RingManagerResource",
    "ToolsResource",
]
