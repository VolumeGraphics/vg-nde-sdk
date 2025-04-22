"""Volume project generation."""

import os
from pathlib import Path

import vg_nde_sdk as sdk

THIS_DIR = Path(__file__).parent


def main():
    """Generate a volume import project in the current directory."""
    project_desc = sdk.make_volume_project_from_block(
        block=Path(os.path.dirname(os.path.abspath(__file__)) + "\\data\\engine.gz"),
        block_size=sdk.Vector3i(256, 256, 110),
        block_format=sdk.VolumeFileFormat.Gzip,
        volume_resolution=sdk.Vector3f(1, 1, 1),
        file_data_type=sdk.VolumeDataType.UInt8,
    )

    targetFilepath = THIS_DIR / "engine_block.xvgi"

    writer = sdk.xvgi.XVGIWriter()
    with open(targetFilepath, "w+") as output:
        writer.dump(project_desc, output)
    print(f"Successfully wrote {targetFilepath}")


if __name__ == "__main__":
    main()
