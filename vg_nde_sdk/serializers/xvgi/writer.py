"""XVGI format serializer."""

from dataclasses import dataclass, field
from typing import Callable, Mapping, TextIO, Union

from vg_nde_sdk.projects import (
    MeshProjectDescription,
    ReconstructionProjectDescription,
    VolumeProjectDescription,
)
from vg_nde_sdk.serializers.xvgi import (
    MeshHolderSerializer,
    ReconstructionHolderSerializer,
    SectionSerializerBase,
    VolumeHolderSerializer,
)


@dataclass
class XVGIWriter:
    """XVGI format writer."""

    section_serializers: Mapping[str, Callable] = field(
        default_factory=lambda: {
            "MeshSectionHolder": MeshHolderSerializer,
            "VolumeSectionHolder": VolumeHolderSerializer,
            "ReconstructionSectionHolder": ReconstructionHolderSerializer,
        }
    )
    """ Maps sections to their according serializer class """

    def dumps(
        self,
        project_description: Union[
            MeshProjectDescription,
            ReconstructionProjectDescription,
            VolumeProjectDescription,
        ],
    ) -> str:
        """Write out the XVGI serialization."""
        result = ""

        for section in vars(project_description).values():
            section_name = type(section).__name__
            serializer_cls = self.section_serializers.get(
                section_name, SectionSerializerBase
            )
            serializer = serializer_cls()
            result += serializer.serialize(section_name, vars(section))

        return result

    def dump(
        self,
        project_description: Union[
            ReconstructionProjectDescription,
            MeshProjectDescription,
            VolumeProjectDescription,
        ],
        file: TextIO,
    ):
        """Write out the XVGI serialization into a provided file."""
        file.write(self.dumps(project_description))
