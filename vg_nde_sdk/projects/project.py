"""Volume project description."""

from dataclasses import dataclass, field

from vg_nde_sdk.sections import (
    MeshSectionHolder,
    ReconstructionSectionHolder,
    VersionSection,
    VolumeSectionHolder,
)


@dataclass
class ProjectDescription:
    """Mixed project description."""

    version: VersionSection = field(default_factory=VersionSection)
    volumes: VolumeSectionHolder = field(default_factory=VolumeSectionHolder)
    meshes: MeshSectionHolder = field(default_factory=MeshSectionHolder)
    reconstructions: ReconstructionSectionHolder = field(
        default_factory=ReconstructionSectionHolder
    )
