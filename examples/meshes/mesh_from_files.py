"""Volume project generation."""

import os
from pathlib import Path

import vg_nde_sdk as sdk  # noqa: E402

THIS_DIR = Path(__file__).parent


def main():
    """Generate a volume import project in the current directory."""
    path = Path(os.path.dirname(os.path.abspath(__file__)) + "\\data\\engine.stl")

    project_desc = sdk.make_mesh_project(
        mesh=path, mesh_format=sdk.MeshFormat.STL, mesh_unit=sdk.MeshUnit.Millimeter
    )

    targetFilepath = THIS_DIR / "engine_mesh.xvgi"

    writer = sdk.xvgi.XVGIWriter()
    with open(targetFilepath, "w+") as output:
        writer.dump(project_desc, output)
    print(f"Successfully wrote {targetFilepath}")


if __name__ == "__main__":
    main()
