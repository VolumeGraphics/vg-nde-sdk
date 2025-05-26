"""Reconstruction project description."""

from pathlib import Path
from typing import Optional, Sequence

from vg_nde_sdk.projects import ProjectDescription
from vg_nde_sdk.sections import (
    ReconstructionCalibrationMode,
    ReconstructionClampType,
    ReconstructionPreprocessingMode,
    ReconstructionProjectionDataType,
    ReconstructionProjectionFileEndian,
    ReconstructionProjectionFileFormat,
    ReconstructionProjectionFileSection,
    ReconstructionProjectionSorting,
    ReconstructionSection,
    ReconstructionSectionHolder,
    Vector2f,
    Vector2i,
    Vector3i,
)


def make_reconstruction_project_from_projections(
    distance_source_object: float,
    distance_object_detector: float,
    projection_file_number_of_pixels: Vector2i,
    projection_file_physical_size: Vector2f,
    result_number_of_voxels: Vector3i,
    reconstruction_base_filename: str,
    projections: Sequence[Path],
    volume_name: str = "",
    preprocessing_mode: ReconstructionPreprocessingMode = ReconstructionPreprocessingMode.Filter,
    calibration_mode: ReconstructionCalibrationMode = ReconstructionCalibrationMode.No,
    calibration_bright_file: Optional[Path] = None,
    calibration_dark_file: Optional[Path] = None,
    projection_file_endian: ReconstructionProjectionFileEndian = ReconstructionProjectionFileEndian.Little,
    projection_file_format: ReconstructionProjectionFileFormat = ReconstructionProjectionFileFormat.Raw,
    projection_file_data_type: ReconstructionProjectionDataType = ReconstructionProjectionDataType.UInt16,
    projection_file_sorting: ReconstructionProjectionSorting = ReconstructionProjectionSorting.NumbersUp,
    reconstruction_angular_offset: float = 0,
    reconstruction_angular_section: float = 360,
    horizontal_detector_offset: float = 0,
    clamp_low_mode: bool = False,
    clamp_low_type: ReconstructionClampType = ReconstructionClampType.AbsoluteClamping,
    clamp_low_value: float = 0,
) -> ProjectDescription:
    """Create a reconstruction project out of projections."""
    angle_step = (reconstruction_angular_section - reconstruction_angular_offset) / len(
        projections
    )
    angles = (x * angle_step for x in range(len(projections)))

    return ProjectDescription(
        reconstructions=ReconstructionSectionHolder(
            [
                ReconstructionSection(
                    ObjectNameInScene=volume_name,
                    ReconstructionDistanceSourceObject=distance_source_object,
                    ReconstructionDistanceObjectDetector=distance_object_detector,
                    ReconstructionHorizontalDetectorOffset=horizontal_detector_offset,
                    ReconstructionPreprocessingMode=preprocessing_mode,
                    ReconstructionCalibrationMode=calibration_mode,
                    ReconstructionCalibrationBrightFile=calibration_bright_file,
                    ReconstructionCalibrationDarkFile=calibration_dark_file,
                    ReconstructionProjectionNumberOfPixels=projection_file_number_of_pixels,
                    ReconstructionProjectionPhysicalSize=projection_file_physical_size,
                    ReconstructionResultNumberOfVoxels=result_number_of_voxels,
                    ReconstructionResultBaseFileName=reconstruction_base_filename,
                    ReconstructionProjectionFileEndian=projection_file_endian,
                    ReconstructionProjectionFileFormat=projection_file_format,
                    ReconstructionProjectionDataType=projection_file_data_type,
                    ReconstructionProjectionSorting=projection_file_sorting,
                    ReconstructionAngularOffset=reconstruction_angular_offset,
                    ReconstructionAngularSection=reconstruction_angular_section,
                    ProjectionFiles=[
                        ReconstructionProjectionFileSection(
                            ReconstructionProjectionInfoFileName=f,
                            ReconstructionProjectionInfoValue=angle,
                            ReconstructionProjectionInfoOption=False,
                        )
                        # compatibility with Python 3.9
                        for angle, f in zip(angles, projections)  # noqa: B905
                    ],
                    ReconstructionClampLowMode=clamp_low_mode,
                    ReconstructionClampLowType=clamp_low_type,
                    ReconstructionClampLowValue=clamp_low_value,
                )
            ]
        )
    )
