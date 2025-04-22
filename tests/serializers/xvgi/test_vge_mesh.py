"""XVGI mesh project tests."""

from pathlib import Path

import pytest

from vg_nde_sdk.projects import MeshProjectDescription
from vg_nde_sdk.sections import (
    MeshFormat,
    MeshSection,
    MeshSectionHolder,
    MeshUnit,
    Vector3f,
)
from vg_nde_sdk.serializers.xvgi import XVGIWriter


@pytest.fixture()
def mesh_project_description(tmpdir: Path) -> MeshProjectDescription:
    return MeshProjectDescription(
        meshes=MeshSectionHolder(
            [
                MeshSection(FileName=Path("data/vgcube/cubeMesh.stl")),
                MeshSection(
                    FileName=Path("data/vgcube/cubeMesh.ply"),
                    MeshFormat=MeshFormat.PLY,
                    MeshUnit=MeshUnit.Nanometer,
                    ObjectNameInScene="N",
                ),
                MeshSection(
                    FileName=Path("data/vgcube/cubeMesh.obj"),
                    MeshFormat=MeshFormat.OBJ,
                    MeshRotation=Vector3f(45, 90, 45),
                    MeshTranslation=Vector3f(15, 0, 0),
                    MeshUnit=MeshUnit.Centimeter,
                    ObjectNameInScene="a",
                ),
            ]
        ),
    )


def test_serialize_mesh_project(
    mesh_project_description: MeshProjectDescription, tmpdir: Path
):
    # GIVEN a mesh and a serializer
    writer = XVGIWriter()

    # WHEN I serialize the project
    serialized = writer.dumps(mesh_project_description)

    # THEN the data has been exported correctly
    assert len(serialized) > 0


def test_serialize_mesh_project_to_file(
    mesh_project_description: MeshProjectDescription, tmpdir: Path
):
    # GIVEN a mesh and a serializer
    output_dir = Path(tmpdir, "output")
    output_dir.mkdir(parents=True)

    output_file_name = Path(output_dir, "mesh.xvgi")
    writer = XVGIWriter()

    # WHEN I serialize the project
    with open(output_file_name, "w+") as output_file:
        writer.dump(mesh_project_description, output_file)

    # THEN the data has been exported
    assert output_file_name.exists()
    serialized = output_file_name.read_text()
    assert len(serialized) > 0
