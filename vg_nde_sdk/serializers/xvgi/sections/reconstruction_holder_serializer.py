"""Reconstruction holder serializer."""

from dataclasses import dataclass
from typing import Mapping, Sequence, cast

from .base import SectionSerializerBase
from .reconstruction_serializer import ReconstructionSectionSerializer


@dataclass
class ReconstructionHolderSerializer(SectionSerializerBase):
    """Serializer for reconstruction holder."""

    current_reconstruction_index: int = 0

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        reconstruction_serializer = ReconstructionSectionSerializer()
        reconstructions = cast(Sequence, section_data.get("reconstructions", ()))
        result = ""
        for reco in reconstructions:
            name = f"ReconstructionSection{self.current_reconstruction_index}"
            self.current_reconstruction_index += 1
            result += reconstruction_serializer.serialize(name, vars(reco))
        return result
