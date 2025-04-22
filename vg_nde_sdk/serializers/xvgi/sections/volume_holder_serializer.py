"""Volume holder serializer."""

from dataclasses import dataclass
from typing import Mapping, Sequence, cast

from .base import SectionSerializerBase
from .volume_serializer import VolumeSectionSerializer


@dataclass
class VolumeHolderSerializer(SectionSerializerBase):
    """Serializer for volume holder."""

    current_volume_index: int = 0

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        volume_serializer = VolumeSectionSerializer()
        volumes = cast(Sequence, section_data.get("volumes", ()))
        result = ""
        for volume in volumes:
            name = f"VolumeSection{self.current_volume_index}"
            self.current_volume_index += 1
            result += volume_serializer.serialize(name, vars(volume))
        return result
