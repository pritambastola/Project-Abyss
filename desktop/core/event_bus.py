"""
Project-Abyss Event Bus
"""

from collections import defaultdict
from typing import Any, Callable


class EventBus:
    def __init__(self):
        self._listeners: dict[str, list[Callable[..., Any]]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable[..., Any]) -> None:
        """Subscribe a callback to an event."""
        self._listeners[event].append(callback)

    def unsubscribe(self, event: str, callback: Callable[..., Any]) -> None:
        """Remove a callback from an event."""
        if callback in self._listeners[event]:
            self._listeners[event].remove(callback)

    def publish(self, event: str, *args, **kwargs) -> None:
        """Publish an event to all subscribers."""
        for callback in self._listeners[event]:
            callback(*args, **kwargs)