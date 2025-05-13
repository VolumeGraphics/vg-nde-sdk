"""Volume project generation."""

import os
import shutil
from pathlib import Path

import vg_nde_sdk as sdk  # noqa: E402

THIS_DIR = Path(__file__).parent


def main():
    """Generate a volume import project in the current directory."""
    targetXVGIFilepath = THIS_DIR / "engine_slices.xvgi"
    targetVGDataFolderPath = THIS_DIR / "[vg-data] engine_slices"

    targetVGDataFolderPath.mkdir(exist_ok=True)

    for file in Path(os.path.dirname(os.path.abspath(__file__)) + "/data/slices").glob(
        "*.raw"
    ):
        file_path = Path(file)
        destination = targetVGDataFolderPath / file_path.name
        shutil.copy(file_path, destination)

    project_desc = sdk.make_volume_project_from_slices(
        slice_size=sdk.Vector2i(256, 256),
        slices=sorted(targetVGDataFolderPath.glob("*.raw")),
        slice_format=sdk.VolumeFileFormat.Raw,
        volume_resolution=sdk.Vector3f(1, 1, 1),
        file_data_type=sdk.VolumeDataType.UInt8,
    )

    writer = sdk.xvgi.XVGIWriter()
    with open(targetXVGIFilepath, "w+") as output:
        writer.dump(project_desc, output)
    print(f"Successfully wrote {targetXVGIFilepath}")


if __name__ == "__main__":
    main()
