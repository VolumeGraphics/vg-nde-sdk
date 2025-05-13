"""Volume project generation."""

import os
import shutil
from pathlib import Path

import vg_nde_sdk as sdk

THIS_DIR = Path(__file__).parent


def main():
    """Generate a volume import project in the current directory."""
    targetXVGIFilepath = THIS_DIR / "engine_block.xvgi"
    targetVGDataFolderPath = THIS_DIR / "[vg-data] engine_block"

    targetVGDataFolderPath.mkdir(exist_ok=True)

    volumeFilePath = targetVGDataFolderPath / "engine.gz"
    shutil.copy(
        os.path.dirname(os.path.abspath(__file__)) + "\\data\\engine.gz", volumeFilePath
    )
    project_desc = sdk.make_volume_project_from_block(
        block=volumeFilePath,
        block_size=sdk.Vector3i(256, 256, 110),
        block_format=sdk.VolumeFileFormat.Gzip,
        volume_resolution=sdk.Vector3f(1, 1, 1),
        file_data_type=sdk.VolumeDataType.UInt8,
    )

    writer = sdk.xvgi.XVGIWriter()
    with open(targetXVGIFilepath, "wt+", encoding="utf-8") as output:
        writer.dump(project_desc, output)
    print(f"Successfully wrote {targetXVGIFilepath}")


if __name__ == "__main__":
    main()
