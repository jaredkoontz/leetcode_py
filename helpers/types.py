from __future__ import annotations

from abc import abstractmethod
from typing import Protocol
from typing import TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: CT, other: CT) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)
