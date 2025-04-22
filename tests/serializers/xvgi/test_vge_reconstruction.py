"""XVGI reconstruction project tests."""

from pathlib import Path

import pytest

from vg_nde_sdk.projects import ReconstructionProjectDescription
from vg_nde_sdk.sections import (
    ComponentInfoSection,
    ManufacturerInfoSection,
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
    ReconstructionProjectionFileSection,
    ReconstructionProjectionOrientation,
    ReconstructionProjectionSmoothingMode,
    ReconstructionProjectionSorting,
    ReconstructionRadiationIntensityCompensationMode,
    ReconstructionResultDataType,
    ReconstructionResultImportMode,
    ReconstructionRingArtifactReductionMode,
    ReconstructionROISection,
    ReconstructionRotationDirection,
    ReconstructionSection,
    ReconstructionSectionHolder,
    ReconstructionSpeckleRemovalMode,
    ScanInfoSection,
    Vector2f,
    Vector2i,
    Vector3f,
    Vector3i,
    VolumeMetaInfoContainer,
)
from vg_nde_sdk.serializers.xvgi import XVGIWriter


@pytest.fixture()
def reconstruction_project_description(
    tmpdir: Path,
) -> ReconstructionProjectDescription:
    project = ReconstructionProjectDescription(
        reconstructions=ReconstructionSectionHolder(
            reconstructions=[
                ReconstructionSection(
                    ObjectNameInScene="My first volume",
                    ReconstructionAlgorithmMode=ReconstructionAlgorithmMode.FBP,
                    ReconstructionAlgorithmicOptimizationMode=ReconstructionAlgorithmicOptimizationMode.Quality,
                    ReconstructionAngularDifferenceCorrection=0,
                    ReconstructionAngularOffset=0,
                    ReconstructionAngularSection=360,
                    ReconstructionArtNumberOfIterations=1,
                    ReconstructionArtRelaxationFactor=0.1,
                    ReconstructionAutoRegionOfInterestMode=False,
                    ReconstructionAutomaticAdaptiveDetectorBinning=False,
                    ReconstructionBeamHardeningCorrectionMode=ReconstructionBeamHardeningCorrectionMode.Off,
                    ReconstructionBeamHardeningCorrectionPreset="",
                    ReconstructionBeamHardeningCorrectionPresetMode=ReconstructionBeamHardeningCorrectionPresetMode.Automatic,
                    ReconstructionBeamHardeningCorrectionPresetValueRange=Vector2f(
                        0, 0
                    ),
                    ReconstructionCalculationMode=ReconstructionCalculationMode.OpenCL,
                    ReconstructionCalibrationBrightFile=Path("/foo/bar/bright.raw"),
                    ReconstructionCalibrationDarkFile=None,
                    ReconstructionCalibrationFilterMode=ReconstructionCalibrationFilterMode.Off,
                    ReconstructionCalibrationMode=ReconstructionCalibrationMode.OnlyBright,
                    ReconstructionClampHighMode=False,
                    ReconstructionClampHighType=ReconstructionClampType.AbsoluteClamping,
                    ReconstructionClampHighValue=3.4028235e38,
                    ReconstructionClampLowMode=True,
                    ReconstructionClampLowType=ReconstructionClampType.AbsoluteClamping,
                    ReconstructionClampLowValue=0.0,
                    ReconstructionDistanceObjectDetector=1320,
                    ReconstructionDistanceSourceObject=434.07001,
                    ReconstructionEnsureIsotropicVoxelSize=False,
                    ReconstructionFieldOfViewExtensionMode=ReconstructionFieldOfViewExtensionMode.No,
                    ReconstructionFieldOfViewExtensionShift=0.0000000,
                    ReconstructionFilterMode=ReconstructionFilterMode.SheppLogan,
                    ReconstructionGeneralSystemGeometryMode=ReconstructionGeneralSystemGeometryMode.ConeBeamCT,
                    ReconstructionGeometricSetup=ReconstructionGeometricSetup.RotateFrustum,
                    ReconstructionHorizontalDetectorOffset=0.0000000,
                    ReconstructionHorizontalDetectorOffsetPosition=0.50000000,
                    ReconstructionHorizontalRotationAxisOffset=0.0000000,
                    ReconstructionIgnoreBorderPixels=0,
                    ReconstructionIntensityCorrectionBias=0.0000000,
                    ReconstructionInterpolationMode=ReconstructionInterpolationMode.Linear,
                    ReconstructionLaminographyAngle=0.0000000,
                    ReconstructionLiftingAxisTiltCorrection=0.0000000,
                    ReconstructionManualResultVolumeSpecificationMode=False,
                    ReconstructionMetalArtifactReductionMode=ReconstructionMetalArtifactReductionMode.Off,
                    ReconstructionMetalArtifactReductionStrength=0.0000000,
                    ReconstructionMetalArtifactReductionThreshold=0.0000000,
                    ReconstructionMetalArtifactReductionThresholdMode=ReconstructionMetalArtifactReductionThresholdMode.Relative,
                    ReconstructionMisalignmentCorrectionMode=ReconstructionMisalignmentCorrectionMode.Off,
                    ReconstructionMisalignmentOptimizationMode=ReconstructionMisalignmentOptimizationMode.FullScan,
                    ReconstructionMisalignmentSkip=0,
                    ReconstructionMisalignmentSkipMode=ReconstructionMisalignmentSkipMode.Auto,
                    ReconstructionMultipleROIPositioningMode=ReconstructionMultipleROIPositioningMode.KeepOrientation,
                    ReconstructionPreprocessingMode=ReconstructionPreprocessingMode.CalibrateAndFilter,
                    ReconstructionProjectionCompletionTimeout=30.000000,
                    ReconstructionProjectionDataType=ReconstructionProjectionDataType.UInt16,
                    ReconstructionProjectionFileEndian=ReconstructionProjectionFileEndian.Little,
                    ReconstructionProjectionFileFormat=ReconstructionProjectionFileFormat.Raw,
                    ReconstructionProjectionHeaderSkip=0,
                    ReconstructionProjectionMirrorAxisY=False,
                    ReconstructionProjectionMirrorAxisZ=False,
                    ReconstructionProjectionMirrorBrightness=False,
                    ReconstructionProjectionNumberOfPixels=Vector2i(128, 128),
                    ReconstructionProjectionOrientation=ReconstructionProjectionOrientation.YZ,
                    ReconstructionProjectionPhysicalSize=Vector2f(409.60001, 409.60001),
                    ReconstructionProjectionReadTimeout=7200.0000,
                    ReconstructionProjectionSkip=Vector2i(0, 0),
                    ReconstructionProjectionSkipAngle=0,
                    ReconstructionProjectionSmoothingMode=ReconstructionProjectionSmoothingMode.Off,
                    ReconstructionProjectionSorting=ReconstructionProjectionSorting.NumbersUp,
                    ReconstructionRadiationIntensityCompensationFixedValueI0=0.0000000,
                    ReconstructionRadiationIntensityCompensationMode=ReconstructionRadiationIntensityCompensationMode.ProjectionPeak,
                    ReconstructionRegionOfInterestMax=Vector3i(255, 255, 90),
                    ReconstructionRegionOfInterestMin=Vector3i(0, 0, 60),
                    ReconstructionResultBaseFileName="/foo/bar/reconstruction_output/zw-reconstructed",
                    ReconstructionResultDataType=ReconstructionResultDataType.UInt16,
                    ReconstructionResultFileSuffix=".raw",
                    ReconstructionResultImportMode=ReconstructionResultImportMode.WriteToDiskAndImport,
                    ReconstructionResultNumberOfVoxels=Vector3i(256, 256, 256),
                    ReconstructionResultOffset=Vector3f(
                        0.0000000, 0.0000000, 0.0000000
                    ),
                    ReconstructionResultPhysicalSize=Vector3f(
                        0.0000000, 0.0000000, 0.0000000
                    ),
                    ReconstructionRingArtifactReductionMode=ReconstructionRingArtifactReductionMode.Off,
                    ReconstructionRotationAxisTiltXZCorrection=0.0000000,
                    ReconstructionRotationAxisTiltXZCorrectionPosition=Vector2f(
                        0.0000000, 0.0000000
                    ),
                    ReconstructionRotationDirection=ReconstructionRotationDirection.CounterClockwise,
                    ReconstructionSkip=Vector3i(0, 0, 0),
                    ReconstructionSpeckleRemovalMode=ReconstructionSpeckleRemovalMode.MultiPixel,
                    ReconstructionTableFeed360Deg=0.0000000,
                    ReconstructionVerticalDetectorOffset=0.0000000,
                    VolumeRotation=Vector3f(15.000000, 5.0000000, -45.000000),
                    VolumeTranslation=Vector3f(-154.53000, 20.000000, -1.0000000),
                    AxisAlignedRois=[
                        ReconstructionROISection(
                            ReconstructionRegionOfInterestListMinPosition=Vector3i(
                                2, 3, 4
                            ),
                            ReconstructionRegionOfInterestListMaxPosition=Vector3i(
                                200, 15, 35
                            ),
                            ReconstructionRegionOfInterestListCustomName="My multiple ROI 1",
                        ),
                        ReconstructionROISection(
                            ReconstructionRegionOfInterestListMinPosition=Vector3i(
                                201, 240, 249
                            ),
                            ReconstructionRegionOfInterestListMaxPosition=Vector3i(
                                255, 254, 253
                            ),
                            ReconstructionRegionOfInterestListCustomName="My multiple ROI 2",
                        ),
                        ReconstructionROISection(
                            ReconstructionRegionOfInterestListMinPosition=Vector3i(
                                5, 5, 5
                            ),
                            ReconstructionRegionOfInterestListMaxPosition=Vector3i(
                                250, 250, 250
                            ),
                        ),
                    ],
                    ProjectionFiles=[
                        ReconstructionProjectionFileSection(
                            ReconstructionProjectionInfoFileName=Path(
                                "/foo/bar/projections/p000.raw"
                            ),
                            ReconstructionProjectionInfoValue=0,
                            ReconstructionProjectionInfoOption=False,
                        ),
                        ReconstructionProjectionFileSection(
                            ReconstructionProjectionInfoFileName=Path(
                                "/foo/bar/projections/p001.raw"
                            ),
                            ReconstructionProjectionInfoValue=1,
                            ReconstructionProjectionInfoOption=True,
                        ),
                        ReconstructionProjectionFileSection(
                            ReconstructionProjectionInfoFileName=Path(
                                "/foo/bar/projections/p010.raw"
                            ),
                            ReconstructionProjectionInfoValue=10,
                            ReconstructionProjectionInfoOption=False,
                        ),
                        ReconstructionProjectionFileSection(
                            ReconstructionProjectionInfoFileName=Path(
                                "/foo/bar/projections/p100.raw"
                            ),
                            ReconstructionProjectionInfoValue=100,
                            ReconstructionProjectionInfoOption=False,
                        ),
                    ],
                    VolumeMetaInfo=VolumeMetaInfoContainer(
                        ComponentInfoSection(
                            CavityNumber="3",
                            Description="Engine",
                            LotNumber="",
                            ProductionDateTime="06.12.2018 20:01:02",
                            SerialNumber="1234",
                            Metadata={"myNewTag": "My new tag description"},
                        ),
                        ManufacturerInfoSection(
                            Name="My company", Metadata={"someTag": "Some tag content"}
                        ),
                        ScanInfoSection(),
                    ),
                )
            ]
        ),
    )

    return project


def test_serialize_reconstruction_project(
    reconstruction_project_description: ReconstructionProjectDescription, tmpdir: Path
):
    # GIVEN a project and a serializer
    writer = XVGIWriter()

    # WHEN I serialize the project
    serialized = writer.dumps(reconstruction_project_description)

    # THEN the data has been exported
    assert len(serialized) > 0


def test_serialize_reconstruction_project_to_file(
    reconstruction_project_description: ReconstructionProjectDescription, tmpdir: Path
):
    # GIVEN a project and a serializer
    output_dir = Path(tmpdir, "output")
    output_dir.mkdir(parents=True)

    output_file_name = Path(output_dir, "reconstruction.xvgi")
    writer = XVGIWriter()

    # WHEN I serialize the project
    with open(output_file_name, "w+") as output_file:
        writer.dump(reconstruction_project_description, output_file)

    # THEN the data has been exported
    assert output_file_name.exists()
    serialized = output_file_name.read_text()
    assert len(serialized) > 0
    print(serialized)
