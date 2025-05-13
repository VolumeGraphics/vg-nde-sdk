"""Volume project generation."""

import os
import shutil
from pathlib import Path

import vg_nde_sdk as sdk  # noqa: E402
from vg_nde_sdk.sections import ComponentInfoSection

THIS_DIR = Path(__file__).parent


def main():
    """Generate a mesh import project in the current directory."""
    targetXVGIFilepath = THIS_DIR / "engine_mesh.xvgi"
    targetVGDataFolderPath = THIS_DIR / "[vg-data] engine_mesh"

    targetVGDataFolderPath.mkdir(exist_ok=True)

    meshFilePath = targetVGDataFolderPath / "engine.stl"
    shutil.copy(
        os.path.dirname(os.path.abspath(__file__)) + "\\data\\engine.stl", meshFilePath
    )

    meta_infos = ComponentInfoSection(
        CavityNumber="123",
        Description="Engine",
        LotNumber="456",
        ProductionDateTime="06.12.2018 20:01:02",
        SerialNumber="1234",
        Metadata={"myNewTag": "My new tag description"},
    )

    project_desc = sdk.make_mesh_project(
        mesh=meshFilePath,
        mesh_format=sdk.MeshFormat.STL,
        mesh_unit=sdk.MeshUnit.Millimeter,
        mesh_info=meta_infos,
    )

    writer = sdk.xvgi.XVGIWriter()
    with open(targetXVGIFilepath, "wt+", encoding="utf-8") as output:
        writer.dump(project_desc, output)
    print(f"Successfully wrote {targetXVGIFilepath}")


if __name__ == "__main__":
    main()
