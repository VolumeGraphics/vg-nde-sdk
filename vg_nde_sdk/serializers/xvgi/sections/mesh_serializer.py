"""Mesh serializers."""

from dataclasses import dataclass, field
from typing import Mapping, cast

from vg_nde_sdk.sections.mesh import MeshMetaInfoContainer

from .base import SectionSerializerBase
from .component_serializer import ComponentInfoSectionSerializer


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

        result = super().serialize(section_name, section_data)

        metaData = cast(
            MeshMetaInfoContainer,
            section_data.pop("MetaInfo", MeshMetaInfoContainer()),
        )

        result += ComponentInfoSectionSerializer().serialize(
            f"{section_name}_ComponentInfoSection", vars(metaData.ComponentInfo)
        )

        return result
