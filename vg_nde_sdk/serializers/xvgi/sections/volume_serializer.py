"""Volume serializers."""

from dataclasses import dataclass, field
from typing import Mapping, Sequence, cast

from vg_nde_sdk.sections.volume import VolumeFileSection, VolumeMetaInfoContainer

from .base import SectionSerializerBase
from .component_serializer import ComponentInfoSectionSerializer
from .manufacturer_serializer import ManufacturerInfoSectionSerializer
from .scan_serializer import ScanInfoSectionSerializer


@dataclass
class VolumeSectionSerializer(SectionSerializerBase):
    """Serializer for volume section."""

    attribute_renaming: Mapping[str, str] = field(default_factory=lambda: {})

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        section_data = dict(section_data)

        projections = cast(
            Sequence[VolumeFileSection], section_data.pop("VolumeProjections", ())
        )

        metaData = cast(
            VolumeMetaInfoContainer,
            section_data.pop("VolumeMetaInfo", VolumeMetaInfoContainer()),
        )

        result = super().serialize_with_renaming_meta(
            section_name, section_data, self.attribute_renaming, {}
        )

        for i, p in enumerate(projections):
            file_section_name = f"{section_name}_FileSection{i}"
            result += super().serialize_with_renaming_meta(
                file_section_name, vars(p), self.attribute_renaming, {}
            )

        result += ManufacturerInfoSectionSerializer().serialize(
            f"{section_name}_ManufacturerInfoSection", vars(metaData.ManufacturerInfo)
        )
        result += ScanInfoSectionSerializer().serialize(
            f"{section_name}_ScanInfoSection", vars(metaData.ScanInfo)
        )
        result += ComponentInfoSectionSerializer().serialize(
            f"{section_name}_ComponentInfoSection", vars(metaData.ComponentInfo)
        )

        return result
