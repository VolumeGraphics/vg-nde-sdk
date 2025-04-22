"""Available description sections."""

from typing import Mapping, NewType, Union

from .component import ComponentInfoSection
from .manufacturer import ManufacturerInfoSection
from .mesh import MeshSection
from .mesh_enums import (
    MeshFormat,
    MeshUnit,
)
from .mesh_holder import MeshSectionHolder
from .reconstruction import (
    ReconstructionProjectionFileSection,
    ReconstructionROISection,
    ReconstructionSection,
)
from .reconstruction_enums import (
    ReconstructionAlgorithmicOptimizationMode,
    ReconstructionAlgorithmMode,
    ReconstructionBeamHardeningCorrectionMode,
    ReconstructionBeamHardeningCorrectionPresetMode,
    ReconstructionCalculationMode,
    ReconstructionCalibrationFilterMode,
    ReconstructionCalibrationMode,
    ReconstructionClampType,
    ReconstructionFieldOfViewExtensionMode,
    ReconstructionFilterMode,
    ReconstructionGeneralSystemGeometryMode,
    ReconstructionGeometricSetup,
    ReconstructionImportMode,
    ReconstructionInterpolationMode,
    ReconstructionMetalArtifactReductionMode,
    ReconstructionMetalArtifactReductionThresholdMode,
    ReconstructionMisalignmentCorrectionMode,
    ReconstructionMisalignmentOptimizationMode,
    ReconstructionMisalignmentSkipMode,
    ReconstructionMultipleROIPositioningMode,
    ReconstructionPreprocessingMode,
    ReconstructionProjectionDataType,
    ReconstructionProjectionFileEndian,
    ReconstructionProjectionFileFormat,
    ReconstructionProjectionOrientation,
    ReconstructionProjectionSmoothingMode,
    ReconstructionProjectionSorting,
    ReconstructionRadiationIntensityCompensationMode,
    ReconstructionResultDataType,
    ReconstructionResultImportMode,
    ReconstructionRingArtifactReductionMode,
    ReconstructionRotationDirection,
    ReconstructionSpeckleRemovalMode,
)
from .reconstruction_holder import ReconstructionSectionHolder
from .scan import ScanInfoSection
from .types import Vector2f, Vector2i, Vector3f, Vector3i, Vectorf
from .version import VersionSection
from .volume import VolumeFileSection, VolumeMetaInfoContainer, VolumeSection
from .volume_enums import (
    VolumeAxesSwapMode,
    VolumeDataMappingMode,
    VolumeDataType,
    VolumeEndian,
    VolumeFileFormat,
    VolumeSliceInterpolationMode,
)
from .volume_holder import VolumeSectionHolder

SectionType = Union[
    ComponentInfoSection,
    ManufacturerInfoSection,
    MeshSection,
    MeshSectionHolder,
    ReconstructionSectionHolder,
    ReconstructionROISection,
    ReconstructionProjectionFileSection,
    ReconstructionSection,
    ScanInfoSection,
    VersionSection,
    VolumeSectionHolder,
    VolumeSection,
    VolumeFileSection,
]
