"""Reconstruction project description."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from vg_nde_sdk.sections import (
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
    VersionSection,
)


@dataclass
class ReconstructionProjectDescription:
    """Reconstruction project description."""

    version: VersionSection = field(default_factory=VersionSection)
    reconstructions: ReconstructionSectionHolder = field(
        default_factory=ReconstructionSectionHolder
    )


def make_reconstruction_project_from_projections(
    distance_source_object: float,
    distance_object_detector: float,
    calibration_bright_file: Path,
    projection_file_number_of_pixels: Vector2i,
    projection_file_physical_size: Vector2f,
    reconstruction_base_filename: str,
    roi_min: Vector3i,
    roi_max: Vector3i,
    projections: Sequence[Path],
    volume_name: str = "Reconstructed volume",
    projection_file_endian: ReconstructionProjectionFileEndian = ReconstructionProjectionFileEndian.Little,
    projection_file_format: ReconstructionProjectionFileFormat = ReconstructionProjectionFileFormat.Raw,
    projection_file_data_type: ReconstructionProjectionDataType = ReconstructionProjectionDataType.UInt16,
    projection_file_sorting: ReconstructionProjectionSorting = ReconstructionProjectionSorting.NumbersUp,
    reconstruction_angular_offset: float = 0,
    reconstruction_angular_section: float = 360,
) -> ReconstructionProjectDescription:
    """Create a reconstruction project out of projections."""
    angle_step = (reconstruction_angular_section - reconstruction_angular_offset) / len(
        projections
    )
    angles = (x * angle_step for x in range(len(projections)))

    return ReconstructionProjectDescription(
        reconstructions=ReconstructionSectionHolder(
            [
                ReconstructionSection(
                    ObjectNameInScene=volume_name,
                    ReconstructionDistanceSourceObject=distance_source_object,
                    ReconstructionDistanceObjectDetector=distance_object_detector,
                    ReconstructionCalibrationBrightFile=calibration_bright_file,
                    ReconstructionProjectionNumberOfPixels=projection_file_number_of_pixels,
                    ReconstructionProjectionPhysicalSize=projection_file_physical_size,
                    ReconstructionResultBaseFileName=reconstruction_base_filename,
                    ReconstructionProjectionFileEndian=projection_file_endian,
                    ReconstructionProjectionFileFormat=projection_file_format,
                    ReconstructionProjectionDataType=projection_file_data_type,
                    ReconstructionProjectionSorting=projection_file_sorting,
                    ReconstructionAngularOffset=reconstruction_angular_offset,
                    ReconstructionAngularSection=reconstruction_angular_section,
                    ReconstructionRegionOfInterestMin=roi_min,
                    ReconstructionRegionOfInterestMax=roi_max,
                    ProjectionFiles=[
                        ReconstructionProjectionFileSection(
                            ReconstructionProjectionInfoFileName=f,
                            ReconstructionProjectionInfoValue=angle,
                            ReconstructionProjectionInfoOption=False,
                        )
                        # compatibility with Python 3.9
                        for angle, f in zip(angles, projections)  # noqa: B905
                    ],
                )
            ]
        )
    )
