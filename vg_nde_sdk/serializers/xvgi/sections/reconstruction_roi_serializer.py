"""Reconstrution ROI serializer."""

from dataclasses import dataclass
from typing import Mapping

from .base import SectionSerializerBase


@dataclass
class ReconstructionROISerializer(SectionSerializerBase):
    """Serializer for reconstruction ROI section."""

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        section_data = dict(section_data)
        result = super().serialize_with_renaming_meta(
            section_name,
            section_data,
            {},
            {},
        )
        return result
