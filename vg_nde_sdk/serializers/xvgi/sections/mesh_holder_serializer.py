"""Mesh holder serializer."""

from dataclasses import dataclass
from typing import Mapping, Sequence, cast

from .base import SectionSerializerBase
from .mesh_serializer import MeshSectionSerializer


@dataclass
class MeshHolderSerializer(SectionSerializerBase):
    """Serializer for Mesh holder."""

    current_mesh_index: int = 0

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        mesh_serializer = MeshSectionSerializer()
        meshes = cast(Sequence, section_data.get("meshes", ()))
        result = ""
        for mesh in meshes:
            name = f"MeshSection{self.current_mesh_index}"
            self.current_mesh_index += 1
            result += mesh_serializer.serialize(name, vars(mesh))
        return result
