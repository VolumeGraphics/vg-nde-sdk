"""Volume project description."""

from dataclasses import dataclass, field
from pathlib import Path

from vg_nde_sdk.sections import (
    MeshFormat,
    MeshSection,
    MeshSectionHolder,
    MeshUnit,
    Vector3f,
    VersionSection,
)


@dataclass
class MeshProjectDescription:
    """Volume project description."""

    version: VersionSection = field(default_factory=VersionSection)
    meshes: MeshSectionHolder = field(default_factory=MeshSectionHolder)


def make_mesh_project(
    mesh: Path,
    mesh_format: MeshFormat,
    mesh_unit: MeshUnit,
    mesh_translation: Vector3f = Vector3f(0, 0, 0),  # noqa: B008
    mesh_rotation: Vector3f = Vector3f(0, 0, 0),  # noqa: B008
) -> MeshProjectDescription:
    """Generate minimal volume project description for a slice stack."""
    project = MeshProjectDescription(
        meshes=MeshSectionHolder(
            [
                MeshSection(
                    FileName=mesh.absolute(),
                    MeshFormat=mesh_format,
                    MeshRotation=mesh_rotation,
                    MeshTranslation=mesh_translation,
                    MeshUnit=mesh_unit,
                )
            ]
        ),
    )
    return project
