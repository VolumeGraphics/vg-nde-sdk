"""Reconstruction project generation."""

import shutil
from pathlib import Path

import vg_nde_sdk as sdk  # noqa: E402

THIS_DIR = Path(__file__).parent


def main():
    """Generate a reconstruction project in the current directory."""
    targetXVGIFilepath = THIS_DIR / "reco_project.xvgi"
    targetVGDataFolderPath = THIS_DIR / "[vg-data] reco_project"

    shutil.copytree(THIS_DIR / "data", targetVGDataFolderPath, dirs_exist_ok=True)

    project_desc = sdk.make_reconstruction_project_from_projections(
        volume_name="Reconstructed part",
        distance_source_object=434.07,
        distance_object_detector=885.93,
        horizontal_detector_offset=-0.8,
        preprocessing_mode=sdk.sections.ReconstructionPreprocessingMode.CalibrateAndFilter,
        calibration_mode=sdk.sections.ReconstructionCalibrationMode.OnlyBright,
        calibration_bright_file=targetVGDataFolderPath / "bright.raw",
        projection_file_number_of_pixels=sdk.Vector2i(128, 128),
        projection_file_physical_size=sdk.Vector2f(409.6, 409.6),
        result_number_of_voxels=sdk.Vector3i(256, 256, 256),
        projection_file_endian=sdk.sections.ReconstructionProjectionFileEndian.Little,
        projection_file_format=sdk.sections.ReconstructionProjectionFileFormat.Raw,
        projection_file_data_type=sdk.sections.ReconstructionProjectionDataType.UInt16,
        reconstruction_base_filename=str(
            targetVGDataFolderPath / "reconstructed" / "volume"
        ),
        projections=sorted(targetVGDataFolderPath.glob("*.raw")),
    )

    writer = sdk.xvgi.XVGIWriter()
    filename = targetXVGIFilepath
    with open(targetXVGIFilepath, "wt+", encoding="utf-8") as output:
        writer.dump(project_desc, output)
    print(f"Wrote {filename}.")


if __name__ == "__main__":
    main()
