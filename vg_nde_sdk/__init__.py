"""Project generation SDK."""

from .projects import ProjectDescription
from .projecttools import (
    make_mesh_project,
    make_reconstruction_project_from_projections,
    make_volume_project_from_block,
    make_volume_project_from_slices,
)
from .sections import (
    ComponentInfoSection,
    ManufacturerInfoSection,
    MeshFormat,
    MeshSection,
    MeshSectionHolder,
    MeshUnit,
    ScanInfoSection,
    Vector2f,
    Vector2i,
    Vector3f,
    Vector3i,
    Vectorf,
    VolumeAxesSwapMode,
    VolumeDataMappingMode,
    VolumeDataType,
    VolumeEndian,
    VolumeFileFormat,
    VolumeFileSection,
    VolumeSection,
    VolumeSectionHolder,
    VolumeSliceInterpolationMode,
)
from .serializers import xvgi

__version__ = "2025.5.27"
