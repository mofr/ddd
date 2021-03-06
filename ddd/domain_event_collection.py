import collections
from typing import Iterator
from typing import List

from .domain_event import DomainEvent


class DomainEventCollection(collections.abc.Collection):
    def __init__(self):
        self._events: List[DomainEvent] = []

    def register(self, event: DomainEvent):
        self._events.append(event)

    def clear(self) -> None:
        self._events.clear()

    def __contains__(self, event: DomainEvent) -> bool:
        return event in self._events

    def __iter__(self) -> Iterator[DomainEvent]:
        return iter(self._events)

    def __len__(self) -> int:
        return len(self._events)
