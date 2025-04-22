"""Reconstruction project generation."""

from pathlib import Path

import vg_nde_sdk as sdk  # noqa: E402

THIS_DIR = Path(__file__).parent


def main():
    """Generate a reconstruction project in the current directory."""
    project_desc = sdk.make_reconstruction_project_from_projections(
        volume_name="Reconstructed part",
        distance_source_object=434.07,
        distance_object_detector=1320,
        calibration_bright_file=Path("data/reco_dummy_bright_file.raw"),
        projection_file_number_of_pixels=sdk.Vector2i(128, 128),
        projection_file_physical_size=sdk.Vector2f(400, 400),
        reconstruction_base_filename="output/reco",
        roi_min=sdk.Vector3i(0, 0, 0),
        roi_max=sdk.Vector3i(128, 128, 128),
        projections=sorted(Path("data/reco_dummy").glob("*.raw")),
    )

    writer = sdk.xvgi.XVGIWriter()
    filename = THIS_DIR / "vgreco.xvgi"
    with open(filename, "w+") as output:
        writer.dump(project_desc, output)
    print(f"Wrote {filename}.")


if __name__ == "__main__":
    main()
