"""Mesh serializers."""

from dataclasses import dataclass, field
from typing import Mapping

from .base import SectionSerializerBase


@dataclass
class MeshSectionSerializer(SectionSerializerBase):
    """Serializer for Mesh section."""

    attribute_renaming: Mapping[str, str] = field(default_factory=lambda: {})

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        section_data = dict(section_data)

        return super().serialize(section_name, section_data)
