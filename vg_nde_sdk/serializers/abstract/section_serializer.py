"""Section serializer interface."""

from abc import ABC, abstractmethod
from typing import Mapping


class AbstractSectionSerializer(ABC):
    """Section serializer interface."""

    @abstractmethod
    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        pass  # pragma: no cover
