"""Scan info serializers."""

from dataclasses import dataclass, field
from typing import Mapping, cast

from .base import SectionSerializerBase


@dataclass
class ScanInfoSectionSerializer(SectionSerializerBase):
    """Serializer for scan info section."""

    attribute_renaming: Mapping[str, str] = field(
        default_factory=lambda: {
            "TubeVoltage": "Tube voltage",
            "TubeCurrent": "Tube current",
            "ScanTime": "Scan time",
            "ReconstructionTime": "Reconstruction time",
            "TotalProcessTime": "Total process time",
            "ScanMethod": "Scan method",
            "IntegrationTime": "Integration time",
            "NumberOfProjections": "Number of projections",
            "DateTime": "Date time",
        }
    )

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        section_data = dict(section_data)
        metadata = cast(Mapping[str, str], section_data.pop("Metadata", {}))

        result = super().serialize_with_renaming_meta(
            section_name,
            section_data,
            self.attribute_renaming,
            metadata,
        )

        return result
