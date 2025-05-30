"""Volume project description."""

from pathlib import Path
from typing import Sequence

from vg_nde_sdk.projects import ProjectDescription
from vg_nde_sdk.sections import (
    Vector2i,
    Vector3f,
    Vector3i,
    VolumeDataType,
    VolumeEndian,
    VolumeFileFormat,
    VolumeFileSection,
    VolumeSection,
    VolumeSectionHolder,
)


def make_volume_project_from_slices(
    slice_size: Vector2i,
    slices: Sequence[Path],
    slice_format: VolumeFileFormat,
    volume_resolution: Vector3f,
    file_data_type: VolumeDataType,
    file_data_endian: VolumeEndian = VolumeEndian.Little,
) -> ProjectDescription:
    """Generate minimal volume project description for a slice stack."""
    slice_sections = [
        VolumeFileSection(
            FileName=s,
            FileFileFormat=slice_format,
            FileEndian=file_data_endian,
            FileSize=Vector3i(slice_size[0], slice_size[1], 1),
            FileDataType=file_data_type,
        )
        for s in slices
    ]

    project = ProjectDescription(
        volumes=VolumeSectionHolder(
            [
                VolumeSection(
                    VolumeDestinationDataType=file_data_type,
                    VolumeResolution=volume_resolution,
                    VolumeProjections=slice_sections,
                )
            ]
        ),
    )
    return project


def make_volume_project_from_block(
    block_size: Vector3i,
    block: Path,
    block_format: VolumeFileFormat,
    volume_resolution: Vector3f,
    file_data_type: VolumeDataType,
    file_data_endian: VolumeEndian = VolumeEndian.Little,
) -> ProjectDescription:
    """Generate minimal volume project description for a single block file."""
    block_section = VolumeFileSection(
        FileName=block,
        FileFileFormat=block_format,
        FileEndian=file_data_endian,
        FileSize=block_size,
        FileDataType=file_data_type,
    )

    project = ProjectDescription(
        volumes=VolumeSectionHolder(
            [
                VolumeSection(
                    VolumeDestinationDataType=file_data_type,
                    VolumeResolution=volume_resolution,
                    VolumeProjections=[block_section],
                )
            ]
        ),
    )
    return project
