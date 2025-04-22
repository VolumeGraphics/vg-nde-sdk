"""Reconstruction descriptor."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Sequence

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
from .types import Vector2f, Vector2i, Vector3f, Vector3i, Vectorf
from .volume import VolumeMetaInfoContainer


@dataclass
class ReconstructionROISection:
    """Stores the extent of the aligned bounding box as two positions.

    Given values are voxel indices, which means they have to lie along each axis
    in the range of:
        .. math:: 0 ≤ value.x < totalVoxelCount
    The upper boundary must not be smaller than the lower boundary.
    Optionally also stores a custom name that is used when naming the resulting
    volume in the scene.

    :Important:
    Names are used to find appropriate objects during macro playback. If you
    plan on using your created projects in automation scenarios, it is advised
    to stick with the default names.
    """

    ReconstructionRegionOfInterestListMinPosition: Vector3i = Vector3i(0, 0, 0)
    """ The lower boundary of the bounding box. """

    ReconstructionRegionOfInterestListMaxPosition: Vector3i = Vector3i(0, 0, 0)
    """ The upper boundary of the bounding box. """

    ReconstructionRegionOfInterestListCustomName: str = ""
    """ The name for the region described by the bounding box. """


@dataclass
class ReconstructionProjectionFileSection:
    """For defining one projection angle."""

    ReconstructionProjectionInfoFileName: Path
    """ UTF8 encoded absolute file path name to projection. """

    ReconstructionProjectionInfoValue: float = 0
    """ Correlated angle of projection file in either Radian or Degree. """

    ReconstructionProjectionInfoOption: bool = False
    """ Whether to ignore this angle or not. """


@dataclass
class ReconstructionSection:
    """Class to completely define a scan setup and reconstruction process.

    Use this class to define a CT-reconstruction process to be carried out by a
    locally or remotely available VG-product. After reconstruction, you will
    always have to initialize at least a subset of parameters in order to obtain
    a valid reconstruction setup. Other parameters are optional.

    Geometry and coordinate system conventions
    =============
    The axes referred to in this documentation are as follows: the Z-axis is the
    "vertical" axis, i.e. the upwards direction of the (ideal) rotation-axis.
    The X-axis is perpendicular to the detector plane, going from x-ray source
    to detector. The Y-axis is, therefore, the "horizontal" detector axis.

    Basic reconstruction workflow
    =============
    The reconstruction process expects projection data as a list of separate
    image files on an accessible filesystem location. Depending on system memory
    and reconstruction size, it may need free temporary space on disk. It will
    save the reconstruction result on disk as a list of separate raw slice files.
    """

    ObjectNameInScene: str = ""
    """
    Controls the name of the object in the scene.

    Controls the name of the volume object in the scene of the saved vg project.
    By default, this name is automatically created (e.g. "Volume 1").
    If you set a custom name and it conflicts with the name of another object in
    the scene, it is possible that the application will append something to the
    name to make it unique (similar to renaming in VGSTUDIO (MAX) itself).

    :Important:
    Names are used to find appropriate objects during macro playback. If you
    plan on using your created projects in automation scenarios, it is advised
    to stick with the default names.

    :Hint:
    Optional. If you do not set anything or set the empty string, the name will
    be automatically created.
    """

    VolumeMetaInfo: VolumeMetaInfoContainer = field(
        default_factory=VolumeMetaInfoContainer
    )
    """
    Sets the meta information of the volume.

    Volume objects can have associated meta information, like a serial number
    or production date time. This meta information can be used in various ways
    in VG software, for example in reports.

    :Hint:
    Optional. If you do not set anything here, the meta information that was
    defined at the project level will be used.
    """

    VolumeRotation: Vector3f = Vector3f(0, 0, 0)
    """
    Controls the rotation of the reconstructed volume in the scene.

    This may be used to change the orientation of the volume in the scene.
    The x-, y- and z-component of the vector contain the angle of
    rotation (in degree) for heading, elevation and bank (euler angles),
    respectively. For a definition of euler angles, see:
        http://en.wikipedia.org/wiki/Euler_Angles

    :Hint:
    Optional. If you do not set this, the axes of the volume will be aligned to
    the ones of the scene coordinate system.
    """

    VolumeTranslation: Vector3f = Vector3f(0, 0, 0)
    """
    Controls the position of the reconstructed volume in the scene.

    This translation vector may be used to change the position of the volume in
    the scene. The origin (which is the center of the volume) will be translated
    according to the supplied vector.

    :Hint:
    Optional. If you do not call this method, the origin of the volume will lie
    in the origin of the scene.
    """

    ReconstructionGeneralSystemGeometryMode: ReconstructionGeneralSystemGeometryMode = (
        ReconstructionGeneralSystemGeometryMode.ConeBeamCT
    )
    """
    General system geometry that will be used to reconstruct the projection files.

    When reconstructing projection files, the CT setup used to create these
    files has to be taken into account. According to this setup, one of the
    supported reconstruction modes has to be chosen and set.

    :Important:
    Depending on the selected reconstruction mode, some parameters of the
    ReconstructionDescriptor may be disregarded.
    See "Create a projection file based VG project" section of the documentation.

    :Hint:
    Optional definition. The default value is ConeBeamCT, for the standard cone
    beam setup.
    """

    ReconstructionAlgorithmicOptimizationMode: (
        ReconstructionAlgorithmicOptimizationMode
    ) = ReconstructionAlgorithmicOptimizationMode.Quality
    """
    Controls the behaviour of the reconstruction algorithm.

    The reconstruction can either aim for quality or performance. If Performance
    is chosen, these params will have no effect:

    * ``ReconstructionProjectionSkip``
    * ``ReconstructionSkip``

    :Hint:
    Optional definition.
    """

    ReconstructionTableFeed360Deg: float = 0
    """
    Defines the table feed per 360 degree scan range.

    This value can be positive or negative and defines the table feed used
    during the scan. The sign controls the direction.

    :Hint:
    Optional definition.
    """

    ReconstructionLiftingAxisTiltCorrection: float = 0
    """
    Sets a tilt value for the axis of the lifting axis in *deg*.

    Setting a correction angle allows to compensate for a skewed lift axis
    during scanning.

    :Important:
    The angle has to be in the interval: :math:`] -90°, 90°[`

    :Hint:
    Optional definition.
    """

    ReconstructionLineZPositionList: Vectorf = Vectorf()
    """
    Used to set the slice z-positions in the reconstructed volume.

    Used to set the z-positions of the slices in the reconstructed volume.
    By default, these slices are equidistant. This is signified by an empty list.
    The number of elements in a list used to define the z-positions must be the
    same as the z-component of the grid size.
    To get back to the default behavior, set an empty list.

    :Important:
    Each z-position has to be unique, the list can not contain a value multiple
    times.

    :Hint:
    Optional definition. The default value is an empty list (=equidistant slices).
    """

    ReconstructionLaminographyAngle: float = 0
    """
    Defines the tilt-angle of the frustum in *deg*.

    See *vg-reconstruction-planar.pdf* for details about planar CT setups.

    :Important:
    The angle has to be in the interval: :math:`] -90°, 90°[`

    :Hint:
    Optional definition.
    """

    ReconstructionGeometricSetup: ReconstructionGeometricSetup = (
        ReconstructionGeometricSetup.RotateFrustum
    )
    """
    Defines the setup that was used during the scan.

    The planar mode has to be set according to the setup that was used to create
    the projection files that will be reconstructed.
    See *vg-reconstruction-planar.pdf* for details about planar CT setups.

    :Hint:
    Optional definition.
    """

    ReconstructionRotationDirection: ReconstructionRotationDirection = (
        ReconstructionRotationDirection.CounterClockwise
    )
    """
    Defines the rotational direction of the reconstruction.

    Defines the direction in which the object was rotated while creating the
    scan.

    :Hint:
    Optional definition.
    """

    ReconstructionPreprocessingMode: ReconstructionPreprocessingMode = (
        ReconstructionPreprocessingMode.Filter
    )
    """
    Defines the mode of projection data preprocessing.

    Defines the mode of preprocessing according to the origin of the projection
    data. Possible values are:

    - ``Off``: Your projection files have already been completely
    preprocessed, even including the Feldkamp high pass filtering step. The
    projection data will be used "as is" for the back projection process.

    - ``Filter``: Your projection files have already been calibrated and
    logarithmized, but the reconstruction still needs to apply the Feldkamp
    highpass filter.

    - ``CalibrateAndFilter``: Your projection files originate directly from the
    CT-scanner. Most likely they contain 16-Bit detector intensities. Those
    files must be logarithmized, and can optionally be normalized using one or
    two additional calibration images. Afterwards, the data will be high pass
    filtered.

    :Hint:
    Optional definition. The default value is ``Filter``, i.e. no calibration
    is applied to the data.
    """

    ReconstructionProjectionSorting: ReconstructionProjectionSorting = (
        ReconstructionProjectionSorting.NumbersUp
    )
    """
    Defines projection sorting mode.

    Defines how the projection files set in addProjectionFileNameList() etc.
    are to be sorted.

    :Important:
    If param ``ProjectionFiles`` is set this projection sorting has no relevance.

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionDataType: ReconstructionProjectionDataType = (
        ReconstructionProjectionDataType.UInt16
    )
    """
    Defines projection file data type.

    Defines the type of the pixel values inside the projection file data.
    Only relevant for *Raw* or *Gzip* data.

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionOrientation: ReconstructionProjectionOrientation = (
        ReconstructionProjectionOrientation.YZ
    )
    """
    Defines projection orientation.

    Defines how rows and columns in the projection file map to the CT detector
    axes. Possible values are:
    - ``YZ``: file x to detector Y, file y to detector Z
    - ``ZY``: file x to detector Z, file y to detector Y.

    :Important:
    The number of pixels inside the projection files must comply with the
    detector pixel count defined in param
    ``ReconstructionProjectionNumberOfPixels``, considering the "swapped"
    orientation!

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionFileFormat: ReconstructionProjectionFileFormat = (
        ReconstructionProjectionFileFormat.Raw
    )
    """
    Defines projection file format.

    Defines the format of (all) projection files (including calibration files
    if present).

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionFileEndian: ReconstructionProjectionFileEndian = (
        ReconstructionProjectionFileEndian.Little
    )
    """
    Defines projection file endianness.

    Defines the endianness of the pixel values inside the projection file data.
    Only relevant for *Raw* or *Gzip* data with >8 bits per pixel.

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionHeaderSkip: int = 0
    """
    Defines projection file header size in bytes.

    Defines the number of bytes to be skipped at the beginning of projection
    files. Only relevant for *Raw* or *Gzip* data.

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionMirrorAxisY: bool = False
    """
    Toggles projection mirror mode (Y-axis).

    Toggles this setting to mirror projection data along the detector Y-axis
    (horizontal).

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionMirrorAxisZ: bool = False
    """
    Toggles projection mirror mode (Z-axis).

    Toggles this setting to mirror projection data along the detector Z-axis
    (vertical).

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionMirrorBrightness: bool = False
    """
    Toggles projection brightness (black is zero / white is zero).

    Toggles this setting to control projection brightness, i.e. how projection
    values are mapped to graylevels. Without brightness
    mirroring (``False``), zero is mapped to black.

    :Hint:
    Optional definition.
    """

    ReconstructionIgnoreBorderPixels: int = 0
    """
    Defines projection data border.

    Set this param to a value greater than zero to indicate that the given
    amount of pixel rows/columns at the border of each projection shall be
    ignored for back projection. Some CT-scanners tend to produce single rows
    of zero-valued pixels which are detrimental to the calibration and
    back projection procedure. Use the border pixel option if you experience
    artifacts with exceedingly high gray values in the reconstructed volume.

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionSmoothingMode: ReconstructionProjectionSmoothingMode = (
        ReconstructionProjectionSmoothingMode.Off
    )
    """
    Defines projection data smoothing mode using a Gauss-Filter.

    :Hint:
    Optional definition.
    """

    ReconstructionCalibrationMode: ReconstructionCalibrationMode = (
        ReconstructionCalibrationMode.No
    )
    """
    Defines the mode of calibrating projection data.

    The calibration file(s) must have the same format and data type as well as
    the same dimensions as all other projection files. Raw detector images must
    be logarithmized before being used for reconstruction. Before doing so, each
    projection image must be normalized to a gray value range of :math:`]0,1]`.
    If you do not supply special reference files, set calibration mode to ``No``
    and this normalization will be done by determining the maximum gray value of
    each image independently and normalizing the image accordingly. However, a
    common approach is to take one (mode ``OnlyBright``) or two (mode ``All``)
    reference images showing the detector levels with full, unabsorbed x-ray
    intensity (Calibration file "bright") and, additionally, no intensity at
    all (Calibration file "dark"). If you supply either the
    ``ReconstructionCalibrationBrightFile`` or both
    (including ``ReconstructionCalibrationDarkFile``) files, the projections are
    calibrated pixel by pixel using the zero-to-bright or dark-to-bright
    intensity range.

    :Hint:
    Optional definition.
    """

    ReconstructionCalibrationBrightFile: Optional[Path] = None
    """
    Defines the path to the "bright" calibration file.
    See ``ReconstructionCalibrationMode``.

    :Hint:
    Mandatory definition if calibration mode is ``All`` or ``OnlyBright``.
    """

    ReconstructionCalibrationDarkFile: Optional[Path] = None
    """
    Defines the path to the "dark" calibration file.
    See ``ReconstructionCalibrationMode``.

    :Hint:
    Mandatory definition if calibration mode is ``All``.
    """

    ReconstructionCalibrationFilterMode: ReconstructionCalibrationFilterMode = (
        ReconstructionCalibrationFilterMode.Off
    )
    """
    Defines the filter mode of calibrating projection data.

    Defines the mode of filtering the calibration projection data to reduce
    noise.

    :Hint:
    Optional definition.
    """

    ReconstructionResultNumberOfVoxels: Vector3i = Vector3i(0, 0, 0)
    """
    Defines the number of voxels of the complete reconstruction volume.

    Defines the desired number of voxels that the *complete
    reconstruction volume* should consist of.

    :Important:
    Changing the number of voxels will *always* result in the SlicePositionsList
    being reset to its default value.

    The voxel resolution of the resulting volume depends on the physical size
    of the reconstruction volume in *mm*, too. This size will be calculated
    automatically, based on the detector size and source-object-detector
    distances.

    The *final reconstruction volume* might be smaller than the
    *complete  reconstruction volume* defined here, if a region of interest is
    specified either manually (see params ``ReconstructionRegionOfInterestMin``
    and ``ReconstructionRegionOfInterestMax``) or automatically
    (see param ``ReconstructionAutoRegionOfInterestMode``).

    The automatic geometry correction is done in the XY-slice of the result
    volume.
    So, if one of this dimensions is too small the correction may fail.

    :Hint:
    Mandatory definition. The default value is ``Vector3i(0, 0, 0)``,
    i.e. an invalid voxel count.
    """

    ReconstructionProjectionNumberOfPixels: Vector2i = Vector2i(0, 0)
    """
    Defines the pixel count of the detector respectively the projection files.

    :Hint:
    Mandatory definition. The default value is ``Vector2i(0, 0)``, i.e. an
    invalid pixel count.
    """

    ReconstructionProjectionPhysicalSize: Vector2f = Vector2f(0, 0)
    """
    Defines the dimensions of the x-ray projection.

    Defines the horizontal and vertical size of the projection in *mm*. The
    first component of *size* denotes the horizontal size, i.e. the size along
    the Y-axis of the reconstruction coordinate system. The second component
    denotes the vertical size, i.e. the size along the Z-axis of the
    reconstruction coordinate system.

    :Hint:
    Mandatory definition. The default value is ``Vector2f(0, 0)``, i.e. an
    invalid detector size.
    """

    ReconstructionDistanceSourceObject: float = 0
    """
    Defines the distance between the x-ray source and the object-rotation-axis.

    Defines the distance between the (point-like) x-ray source and the
    rotation-axis of the scanned object, in *mm*.

    :Hint:
    Mandatory definition. The default value is ``0``, i.e. an invalid distance.
    """

    ReconstructionDistanceObjectDetector: float = 0
    """
    Defines the distance between the object-rotation-axis and the x-ray detector.

    Defines the perpendicular distance between the rotation-axis of the scanned
    object and the x-ray detector, in *mm*.

    :Hint:
    Mandatory definition. The default value is ``0``, i.e. an invalid distance.
    """

    ReconstructionHorizontalDetectorOffsetPosition: float = 0.5
    """
    Defines the relative position for detector offset calculation.

    When automatic correction of the horizontal detector offset is requested
    (see param ``ReconstructionMisalignmentCorrectionMode``), this value
    determines where the correction procedure (based on a
    single-slice-reconstruction) should take place. The given value
    (from *0.0f* to *1.0f*) is a relative vertical position on the detector.
    Generally, it needs only be changed from the default central position if it
    is to be expected that no material is found in the central region.

    :Important:
    The definition of the relative position is a starting value. The final
    height for the correction is calculated based on the intensities of the
    projections.

    Consider that using a relative value of *0.0f* and a positive value for the
    vertical detector shift can cause the height determination to reset the
    value to *0.5f*. The projected lower bound of the original detector is below
    the lower bound of the result volume in this case.

    :Hint:
    Optional definition. The default value is ``0.5f``, i.e. the detector center.
    """

    ReconstructionMisalignmentCorrectionMode: (
        ReconstructionMisalignmentCorrectionMode
    ) = ReconstructionMisalignmentCorrectionMode.Off
    """
    Defines desired mode of automatic geometry correction.

    The reconstruction process can automatically correct common deviations in
    the geometric scanner setup. This setting will determine the way the
    horizontal detector offset and the axis tilt correction values are used.

    * ``Off``: No correction is done. Detector offset and axis tilt correction
        values will be used exactly as set with the respective APIs.

    * ``HorizontalDetectorOffset``: The Y-offset between detector center and
        projected x-ray source is automatically determined, using the horizontal
        detector offset as starting point (if set). The axis tilt correction
        value will be used exactly as set.

    * ``RotationAxisTiltXZ``: A correction for a slightly non-perpendicular
        rotation axis can be requested. The calculated value will override the
        specified axis tilt correction value, if any. The horizontal detector
        offset value, if set, will be used to improve the calculation, but won't
        itself be changed.

    * ``All``:  Does the same as ``RotationAxisTiltXZ``, but additionally
        replaces the horizontal detector offset value with an automatically
        determined one.

    :Hint:
    Optional definition.
    """

    ReconstructionMisalignmentOptimizationMode: (
        ReconstructionMisalignmentOptimizationMode
    ) = ReconstructionMisalignmentOptimizationMode.FullScan
    """
    Selects if misalignment correction is optimized for short or for full scans.

    The various misalignment corrections (detector offset calculation etc.) can
    be either optimized for "short" scans that were created using an angular
    section around 180° or for full scans that were created using a large
    angular section.

    :Hint:
    Optional definition.
    """

    ReconstructionMisalignmentSkipMode: ReconstructionMisalignmentSkipMode = (
        ReconstructionMisalignmentSkipMode.Auto
    )
    """
    Defines the skip strategy mode for automatic geometry correction.

    When calculating the automatic geometry correction (see
    ``ReconstructionMisalignmentCorrectionMode``), a small number of result
    slices are actually reconstructed and analyzed. To speed up this
    process, the number of reconstructed voxels in each slice, as well as the
    number of detector pixels used for this back projection, can be reduced.
    The skip-mode defines the behavior of this reduction. Possible values are:

    * ``Off``: never skip
    * ``On``: always skip with the value defined by param
        ``ReconstructionMisalignmentSkip``
    * ``Auto``: skip/precision is automatically determined by the geometric
        setup → number of reconstruction voxels and number of detector pixels.

    :Hint:
    Optional definition.
    """

    ReconstructionMisalignmentSkip: int = 0
    """
    Defines the skip value for automatic geometry correction.

    This value is only used if the correction skip mode is set to ``On``
    (see param ``ReconstructionMisalignmentSkipMode``). In this case, manually
    define the desired skip to be used for the correction here. Skipping value
    has the same meaning as described in param ``ReconstructionSkip``.

    :Hint:
    Optional definition.
    """

    ReconstructionHorizontalDetectorOffset: float = 0
    """
    Defines the horizontal detector offset.

    Defines the horizontal detector offset (HDO, see Fig. 1) in *mm*.
    If automatic correction is requested (see
    ``ReconstructionMisalignmentCorrectionMode``), this value will be used as an
    initial start value, but finally replaced by the automatic correction result.

    :Hint:
    Optional definition. The default value is ``0``, i.e. no offset.
    """

    ReconstructionHorizontalRotationAxisOffset: float = 0
    """
    Defines the rotation axis horizontal offset value in *mm*.

    :Hint:
    Optional definition. The default value is ``0``, i.e. no correction.
    """

    ReconstructionRotationAxisTiltXZCorrection: float = 0
    """
    Defines angular axis tilt xz correction value.

    Defines, in *deg*, the desired tilt correction value for the rotation axis
    of the detector. Allowed values range from *-10.0* to *10.0f*. Also see
    param ``ReconstructionMisalignmentCorrectionMode``.

    :Hint:
    Optional definition. The default value is ``0``, i.e. no correction.
    """

    ReconstructionRotationAxisTiltXZCorrectionPosition: Vector2f = Vector2f(0, 0)
    """
    Defines the relative position for rotation axis tilt calculation.

    When automatic correction of the rotation axis tilt correction is requested
    (see param ReconstructionMisalignmentCorrectionMode), this value determines
    where the correction procedure (based on a single-slice-reconstruction)
    should take place. The given value (from *0.0f* to *1.0f*) is a relative
    vertical position on the detector. Generally, it needs only be changed from
    the default position if it is to be expected that no material is found in
    the default region.

    :Hint:
    Optional definition. The default value is ``Vector2f(0, 0)``, i.e. the used
    slices are determined automatically.
    """

    ReconstructionVerticalDetectorOffset: float = 0
    """
    Defines the vertical detector offset in *mm*.

    :Hint:
    Optional definition. The default value is ``0``, i.e. no offset.
    """

    ReconstructionAngularOffset: float = 0
    """
    Defines the starting angle.

    Defines the starting angle for the first projection file. This angle offset
    will alter the orientation of the result volume cube.

    :Important:
    The offset is overridden if ``ReconstructionAutoRegionOfInterestMode`` is
    turned on.

    :Hint:
    Optional definition. The default value is ``0``, i.e. the first projection
    is at zero angle.
    """

    ReconstructionAngularSection: float = 0
    """
    Defines the angular section that the given projections represent.

    Defines whether the given projection files represent a full-circle scan, or
    merely a portion. The given value must be in degrees.

    :Hint:
    Optional definition. The default value is ``360``, i.e. a full circle.
    """

    ReconstructionAngularDifferenceCorrection: float = 0
    """
    Defines the difference angle between the translation tables.

    Advanced planar CT is based on the translation movements of two separate
    tables. You can correct an angular misalignment between these two tables
    using the Angular difference correction.

    :Important:
    Even small angular changes (e.g., smaller than 1 degree) may have a strong
    impact on the misalignment correction.

    :Hint:
    Optional definition.
    """

    ReconstructionInterpolationMode: ReconstructionInterpolationMode = (
        ReconstructionInterpolationMode.Linear
    )
    """
    Defines the interpolation mode to be used during backprojection.

    When accessing 2D projection data during back projection, intensity values
    at arbitrary positions can be fetched either by choosing the nearest pixel
    neighbour (interpolation mode ``Off``; fast but not recommended) or by using
    bilinear interpolation between four neighboring pixels (interpolation mode
    ``Linear``; recommended).

    :Hint:
    Optional definition.
    """

    ReconstructionFilterMode: ReconstructionFilterMode = (
        ReconstructionFilterMode.SheppLogan
    )
    """
    Defines the filtering mode to be applied to the projection data.

    Prior to back projection, the Feldkamp reconstruction applies a line-wise
    high-pass filtering step to all 2D projections. There are two possible
    types of filters with slightly different frequency response patterns:
    * ``Ramp``: linearly amplifies high frequencies
    * ``SheppLogan``: partly attenuates highest frequencies.

    :Important:
    The filtering mode is irrelevant if filtering is actually turned off, see
    param ``ReconstructionPreprocessingMode``.

    :Hint:
    Optional definition.
    """

    ReconstructionSpeckleRemovalMode: ReconstructionSpeckleRemovalMode = (
        ReconstructionSpeckleRemovalMode.Off
    )
    """
    Controls the speckle removal method that is used.

    Projection data sometimes contains defective pixels with unusually low or
    high intensity values. Depending on the mode chosen here, the reconstruction
    will try to automatically detect and correct those pixels. Speckle removal
    can either be optimized for singular defective pixels, or for multiple
    defective pixels clustered together.

    :Hint:
    Optional definition.
    """

    ReconstructionCalculationMode: ReconstructionCalculationMode = (
        ReconstructionCalculationMode.OpenCL
    )
    """
    Defines CPU or OpenCL calculation.

    The reconstruction process supports acceleration by modern graphics cards.
    If calculation mode is set to ``OpenCL`` all OpenCL-enabled devices will be
    used, e.g. a GPU cluster. Otherwise (mode ``CPU``), no additional graphics
    hardware is needed/used.

    :Hint:
    Optional definition.
    """

    ReconstructionBeamHardeningCorrectionMode: (
        ReconstructionBeamHardeningCorrectionMode
    ) = ReconstructionBeamHardeningCorrectionMode.Off
    """
    Defines beam hardening correction mode.

    The reconstruction process can try to minimize beam-hardening artifacts
    using a defined "correction-lookup table". If set to ``Preset``, you will
    have to specify the name of the correction preset (see param
    ``ReconstructionBeamHardeningCorrectionPreset``), which will then be used to
    correct the projection data during the calibration process.

    :Hint:
    Optional definition.
    """

    ReconstructionBeamHardeningCorrectionPreset: str = ""
    """
    Defines beam hardening correction preset.

    If param ``ReconstructionBeamHardeningCorrectionMode`` is set to
    ``Preset``, you must specify the name of the correction preset to be used.
    A preset of this name must be present at the machine where the
    reconstruction process is run.

    :Important:
    The default presets ``Low``, ``Medium`` and ``High`` are always available.
    Set param ``ReconstructionBeamHardeningCorrectionPresetMode`` to ``Dynamic``
    as these default presets have no value range defined.

    :Hint:
    Mandatory definition if param ``ReconstructionBeamHardeningCorrectionMode``
    is set to Preset. The default value is "", i.e. no preset.
    """

    ReconstructionBeamHardeningCorrectionPresetMode: (
        ReconstructionBeamHardeningCorrectionPresetMode
    ) = ReconstructionBeamHardeningCorrectionPresetMode.Automatic
    """
    Defines beam hardening correction preset mode.

    If param ``ReconstructionBeamHardeningCorrectionMode`` is set to
    ``Preset``, you can define how the correction-lookup table from the chosen
    preset is to be applied.

    * ``Dynamic``:  The correction lookup table is scaled to the actual gray
        value range of the projection data to be corrected during the
        reconstruction.
    * ``Static``: The lookup table is scaled to the range specified inside the
        chosen preset.
    * ``Automatic``: ``Dynamic`` or ``Static`` is used in the user defined preset;
        ``Dynamic`` mode is set for predefined presets.
    * ``Explicit``: The range must be explicitly defined by
    ``ReconstructionBeamHardeningCorrectionPresetValueRange``.

    :Hint:
    Optional definition
    """

    ReconstructionBeamHardeningCorrectionPresetValueRange: Vector2f = Vector2f(0, 0)
    """
    Defines beam hardening lookup-table range.

    In the special case where ``ReconstructionBeamHardeningCorrectionMode`` is
    set to ``Preset`` and ``ReconstructionBeamHardeningCorrectionPresetMode`` is
    set to ``Explicit``, the correction lookup table is scaled to the given gray
    value range, not regarding the actual projections range or the original
    range stored in the preset.

    :Important:
    If ``ReconstructionBeamHardeningCorrectionPresetMode`` is set to
    ``Explicit``, this must be set to a valid range :math:`(x ≥ 0.0; y > x)`.

    :Hint:
    The default value is ``Vector2f(0, 0)``, an invalid range.
    """

    ReconstructionProjectionReadTimeout: float = 7200
    """
    Defines timeout for projection reads.

    During reconstruction, projection files are read from disk when needed.
    In case a needed projection file cannot be opened at once (e.g. because the
    scanning process is still in progress), the reconstruction will try again
    for the given time in *sec* until an error is indicated and the
    reconstruction fails.

    :Important:
    Keep in mind that detector geometry correction and the dynamic mode of the
    beam hardening correction needs projections too: It will block the
    reconstruction until all needed projections are available!

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionCompletionTimeout: float = 30
    """
    Defines timeout for projection file completion.

    During reconstruction, it may happen that the reconstruction process tries
    to read a file that is already existing but still being written, and thus
    not yet usable. This timeout determines the time the reconstruction process
    will wait for completion of the file. If the file is not completed after the
    wait, reconstruction will fail with an error.

    :Hint:
    Optional definition.
    """

    AxisAlignedRois: Sequence[ReconstructionROISection] = ()
    """
    Stores data that represents a single axis aligned bounding box(es) for use
    with multi-ROI reconstruction
    """

    ProjectionFiles: Sequence[ReconstructionProjectionFileSection] = ()
    """
    Set projection angular list.

    Setting the projection angles is completely orthogonal to all projection
    file name list functionality. Also projection sorting has no relevance here.
    All other projection related functionality is applicable however.

    :Important:
    If set, these ProjectionFiles are going to taken instead of projection file
    name list entries.

    The projection angular list does work only with the *OpenCL back projector*.
    *CPU* or *OpenGL* are not supported.

    The projection angular list does not support Fan beam geometry.

    The projection angular list supports ART for helix geometry only.
    FDK is not supported.


    :Hint:
    The angles (and correlated files) do not need to be ordered. All angle units
    have to be the same.
    """

    ReconstructionMultipleROIPositioningMode: (
        ReconstructionMultipleROIPositioningMode
    ) = ReconstructionMultipleROIPositioningMode.KeepOrientation
    """
    Determines the scene position of the reconstructed volumes defined with
    ``ReconstructionRegionOfInterestList``.

    Controls whether reconstructed ROI volumes will keep their relative
    orientations to each other, or be moved to the center of the scene.

    :Hint:
    If this is set to ``MoveToCenter``, params for translation and rotation
    settings of the will be ignored.
    """

    ReconstructionRegionOfInterestMin: Vector3i = Vector3i(0, 0, 0)
    """
    Defines the lower boundary of a region of interest on the reconstruction
    volume.

    The *complete reconstruction volume* is automatically calculated to cover
    the entire region that can theoretically reconstructed with the given
    geometric setup. However, most scanned objects will probably cover less
    space than this entire cube. Using this param and
    ``ReconstructionRegionOfInterestMax``, you can restrict the reconstructed
    volume. Given values are voxel indices, that means they have to lie in the
    range of :math:`0 ≤ value.x < ReconstructionResultNumberOfVoxels` along each
    axis. The upper boundary must not be smaller than the lower boundary except
    for the special pair ``(0, 0, 0); (-1, -1, -1)`` which denotes the
    full volume with no ROI.

    :Important:
    This setting will be ignored if auto-ROI mode is turned on (see
    param ``ReconstructionAutoRegionOfInterestMode``).

    :Hint:
    Optional definition. The default value is ``Vector3i(0, 0, 0)``,
    i.e.  the full volume (when param ``ReconstructionRegionOfInterestMax`` is
    ``Vector3i(-1, -1, -1)``).
    """

    ReconstructionRegionOfInterestMax: Vector3i = Vector3i(-1, -1, -1)
    """
    Defines the upper boundary of a region of interest on the reconstruction
    volume.

    Region of interest definition; see ``ReconstructionRegionOfInterestMin``.

    :Important:
    This setting will be ignored if auto-ROI mode is turned on (see
    param ``ReconstructionAutoRegionOfInterestMode``).

    :Hint:
    Optional definition. The default value is ``Vector3i(-1, -1, -1)``, i.e. the
    full volume (when param ``ReconstructionRegionOfInterestMin`` is
    ``Vector3i(0, 0, 0)``).
    """

    ReconstructionAutoRegionOfInterestMode: bool = False
    """
    Turn auto-ROI mode on or off.

    The *complete reconstruction volume* is automatically calculated to cover
    the entire region that can theoretically be reconstructed with the given
    geometric setup. However, most scanned objects will probably cover less
    space than this entire cube. The automatic region-of-interest mode will
    inspect the actual projection data prior to the reconstruction process
    and -- based upon the presence or absence of material -- will minimize the
    reconstruction volume to the space covered by the object. This minimization
    will comprise of:
     a) Finding the best rotational offset that aligns the axes of the
        reconstruction volume with those of the scanned object
        (see param ``ReconstructionAngularOffset``).

     b) Reducing the reconstruction volume to a suitable minimal size (as can be
        done manually by ``ReconstructionRegionOfInterestMin`` / ``ReconstructionRegionOfInterestMax``).

    :Hint:
    Optional definition.
    """

    ReconstructionProjectionSkip: Vector2i = Vector2i(0, 0)
    """
    Defines the amount of pixels to be skipped when reading projection files.

    At a skip factor of :math:`n ≥ 0`, only every :math:`(n + 1)`-th
    projection pixel will be considered, the rest will be skipped. Skipping
    can reduce reconstruction times significantly, but naturally at a loss of
    achievable resolution. When skipping projection pixels, it is recommended
    to adjust the number of reconstructed voxels to a similar magnitude, see
    param ``ReconstructionSkip``.

    The first component of *skip* applies to the horizontal detector axis
    (Y), the second component applies to the vertical axis (Z).

    :Hint:
    Optional definition. The default value is ``Vector2i(0, 0)``, i.e. no
    projection-pixels are skipped.
    """

    ReconstructionProjectionSkipAngle: int = 0
    """
    Defines the amount of projections to be skipped.

    Defines the amount of whole projection files (or "angles") to be skipped.
    At a skip factor of :math:`n ≥ 0`, only every :math:`(n + 1)`-th projection
    file will be considered, the rest will be skipped entirely.
    *Angular* skipping can reduce reconstruction times more significantly than
    *pixel*-wise skipping (see param ``ReconstructionProjectionSkip``), but
    naturally at a loss of achievable resolution. When skipping projection
    pixels, it is recommended to adjust the number of reconstructed voxels to a
    similar magnitude, see param ``ReconstructionSkip``.

    :Hint:
    Optional definition. The default value is 0, i.e. no projection-pixels are
    skipped.
    """

    ReconstructionSkip: Vector3i = Vector3i(0, 0, 0)
    """
    Defines the amount of voxels to be skipped from the reconstruction volume.

    Defines the amount of voxels to be skipped when setting up and
    reconstructing the final volume data set. The voxel skip options effectively
    reduce the number of voxels that were initially defined for the
    reconstruction volume by ``ReconstructionResultNumberOfVoxels``. Thus, it is
    rather a convenience function: Instead of defining a reconstruction skip
    value of ``(1, 1, 1)`` and a result number of voxels of
    ``(1024, 1024,1024)``, you could also just set
    ``ReconstructionResultNumberOfVoxels`` with half the initial voxel
    number, ``(512, 512, 512)``, and leave the skip at ``(0, 0, 0)``. The three
    components of *skip* apply to the X-, Y- and Z-axis of the reconstruction
    volume, respectively.

    :Hint:
    Optional definition. The default value is Vector3i(0, 0, 0), i.e. no voxels
    are skipped.
    """

    ReconstructionClampLowMode: bool = False
    """
    Defines the lower clamping mode.

    If set to ``True``, lower clamping is enabled; otherwise, no lower clamping
    is done. For explanation, see param ``ReconstructionClampLowValue``.

    :Hint:
    Optional definition.
    """

    ReconstructionClampLowType: ReconstructionClampType = (
        ReconstructionClampType.AbsoluteClamping
    )
    """
    Defines the lower clamping type.

    Only relevant if lower clamping is enabled (see param
    ``ReconstructionClampLowMode``). For explanation, see
    ``ReconstructionClampLowValue``.

    :Hint:
    Optional definition.
    """

    ReconstructionClampLowValue: float = 0
    """
    Defines the lower clamping value.

    The reconstruction produces a volume with (floating point) gray values in a
    certain range. The lower boundary of this range will be restricted if
    desired (see param ``ReconstructionClampLowMode``). If low clamping type
    is ``AbsoluteClamping`` (see param ``ReconstructionClampHighType``), the
    given value denotes an absolute gray value.
    For clamping type ``PercentalClamping``, the effective clamping threshold is
    based upon an analysis of the resulting gray value histogram: For a given
    value between *0* and *100*, the clamping threshold is chosen such that
    *value* percent of the gray value histogram lie below the lower threshold.

    :Hint:
    Optional definition.
    """

    ReconstructionClampHighMode: bool = False
    """
    Defines the upper clamping mode.

    If set to ``True``, upper clamping is enabled; otherwise, no upper clamping
    is done. For explanation, see ``ReconstructionClampHighValue``.

    :Hint:
    Optional definition.
    """

    ReconstructionClampHighType: ReconstructionClampType = (
        ReconstructionClampType.AbsoluteClamping
    )
    """
    Defines the upper clamping type.

    Only relevant if upper clamping is enabled using param
    ``ReconstructionClampHighMode``. For explanation, see
    ``ReconstructionClampHighValue``.

    :Hint:
    Optional definition.
    """

    ReconstructionClampHighValue: float = float("inf")
    """
    Defines the upper clamping value.

    The reconstruction produces a volume with (floating point) gray values in a
    certain range. The upper boundary of this range will be restricted if
    desired (see param ``ReconstructionClampHighMode``). If high clamping type
    is ``AbsoluteClamping`` (see param ``ReconstructionClampHighType``), the
    given value denotes an absolute gray value.
    For clamping type ``PercentalClamping``, the effective clamping threshold is
    based upon an analysis of the resulting gray value histogram: For a given
    value between *0* and *100*, the clamping threshold is chosen such that
    *value* percent of the gray value histogram lie above the upper threshold.

    :Hint:
    Optional definition. The default value is positive infinity, i.e.
    effectively no clamping.
    """

    ReconstructionResultDataType: ReconstructionResultDataType = (
        ReconstructionResultDataType.UInt16
    )
    """
    Defines the result data type.

    Defines the result voxel data type. The effective result gray value range
    (after reconstruction and optional clamping) will be mapped to the entire
    range of the result data type, so precision is maximized and you do not have
    to worry about the original gray value range of the reconstruction procedure.
    See also param ``ReconstructionClampLowType``, ``ReconstructionClampHighType``.

    :Important:
    Type *UInt12* uses in fact a 16-bit storage, but confines gray values
    to the range *0* - *4095*.

    :Hint:
    Optional definition.
    """

    ReconstructionResultBaseFileName: str = ""
    """
    Defines the result base-filename.

    Defines the base-filename, including a directory path, that all written
    result slice files will start with. Each result slice will have a filename
    of the form *base* name + *file* number + *suffix*, where *file* number
    is a decimal number with enough digits to contain every result slice.
    Leading zeros are inserted where needed.

    :Important:
    See DataReferenceType to understand when result slices are written
    at all.

    :Hint:
    Mandatory definition if ``DataReferenceType`` is set to
    ``ReferenceVolumeData``. The default value is "", i.e. an invalid filename.
    """

    ReconstructionResultFileSuffix: str = ""
    """
    Defines a filename suffix that is applied to all written result slice files.

    :Hint:
    Optional definition.
    """

    ReconstructionResultImportMode: ReconstructionResultImportMode = (
        ReconstructionResultImportMode.WriteToDiskAndImport
    )
    """
    Defines the way the reconstructed data will be imported into VGSTUDIO (MAX)

    The import mode determines how VGSTUDIO (MAX) will handle the reconstructed
    volume data when opening a reconstruction .vgl file. There are three options:

    - DirectReference: VGSTUDIO (MAX) will only load the reconstructed volume
        into the scene, without saving it to disk. Reconstruction will have to
        be redone each time the project is opened. Use for "on-the-fly" analysis
        scenarios where you don't want to keep the reconstructed data.
    - WriteToDiskAndImport: VGSTUDIO (MAX) will save the reconstructed volume to
        disk (meaning reconstruction will only have to be done once) and load
        the volume into the scene after that. Use this if you want to process
        the volume further after reconstruction.
    - WriteToDiskOnly: The same as WriteToDiskAndImport, but the reconstructed
        volume won't actually be loaded by VGSTUDIO (MAX). Use this if you are
        interested in reconstruction only (of course, the project can be loaded
        later for further processing).

    :Hint:
    Optional definition.
    """

    ReconstructionManualResultVolumeSpecificationMode: bool = False
    """
    Enables or disables manual result volume specification mode

    Enables or disables the manual result volume specification mode. If it is
    disabled, the physical size of the reconstructed volume will be calculated
    using the geometry parameters of the scanner. If it is enabled, the
    specified physical size and offset will be used instead. See params
    ``ReconstructionResultPhysicalSize`` and ``ReconstructionResultOffset``.

    :Hint:
    Optional definition. The default value is ``False`` (=manual specification
    disabled)
    """

    ReconstructionResultPhysicalSize: Vector3f = Vector3f(0, 0, 0)
    """
    Sets the reconstructed volumes physical size

    Sets the result volumes physical size. The value is only used if manual
    result specification mode is enabled, otherwise it is ignored. The unit used
    for the size is *millimeter*.
    See param ``ReconstructionManualResultVolumeSpecificationMode``.

    :Important:
    The automatic geometry correction is done in the XY-slice of the result
    volume. So, if one of this dimensions is too small the correction may fail.

    :Hint:
    Optional definition.
    """

    ReconstructionResultOffset: Vector3f = Vector3f(0, 0, 0)
    """
    Sets the reconstructed volumes physical offset

    Sets the result volumes physical offset. The value is only used if manual
    result specification mode is enabled, otherwise it is ignored.
    The unit used for the offset is *millimeter*.
    See param ``ReconstructionManualResultVolumeSpecificationMode``.

    :Hint:
    Optional definition.
    """

    ReconstructionIntensityCorrectionBias: float = 0
    """
    Sets the constant offset for intensity correction.

    The value may be in the range of *0* - *100*.

    :Hint:
    Optional definition.
    """

    ReconstructionMetalArtifactReductionMode: (
        ReconstructionMetalArtifactReductionMode
    ) = ReconstructionMetalArtifactReductionMode.Off
    """
    Sets the mode that will be used for the metal artifact reduction.

    :Hint:
    Optional definition.
    """

    ReconstructionMetalArtifactReductionThresholdMode: (
        ReconstructionMetalArtifactReductionThresholdMode
    ) = ReconstructionMetalArtifactReductionThresholdMode.Relative
    """
    The mode that will be used for the threshold of the metal artifact reduction.

    :Hint:
    Optional definition.
    """

    ReconstructionMetalArtifactReductionThreshold: float = 0
    """
    Sets the threshold used for reducing metal artifacts.

    Depending on the mode the value is relative or absolute.

    :Important:
    If the mode for metal artifact reduction is relative, the value must be in
    the range *-100* -- *+100*.

    :Hint:
    Optional definition.
    """

    ReconstructionMetalArtifactReductionStrength: float = 0
    """
    Sets the strength of the metal artifact reduction.

    Sets how aggressively the metal artifact reduction should operate. The value
    may be in the range of *0* - *100*.

    :Hint:
    Optional definition.
    """

    ReconstructionAlgorithmMode: ReconstructionAlgorithmMode = (
        ReconstructionAlgorithmMode.FBP
    )
    """
    Defines the reconstruction algorithm mode.

    :Hint:
    Optional definition.
    """

    ReconstructionArtNumberOfIterations: int = 1
    """
    Defines how many iterations are used for algebraic reconstruction technique.

    :Hint:
    Optional definition.
    """

    ReconstructionArtRelaxationFactor: float = 0.1
    """
    Sets the relaxation factor for algebraic reconstruction technique.

    Sets how aggressively the iterative solution is calculated.

    :Hint:
    Optional definition.
    """

    ReconstructionRadiationIntensityCompensationMode: (
        ReconstructionRadiationIntensityCompensationMode
    ) = ReconstructionRadiationIntensityCompensationMode.ProjectionMax
    """
    Defines the mode for radiation intensity compensation.

    Defines which gray value in the projections is used as air value. This is
    useful, if the air value changes during the measurement.

    :Hint:
    Optional definition.
    """

    ReconstructionRadiationIntensityCompensationFixedValueI0: float = 0
    """
    Defines fix scaling factor for radiation intensity compensation.

    Allows to specify a fix scaling factor in percent to be applied to all
    intensity values. If the gray values (intensities) of your projection do not
    cover the complete gray value range of the dataset, you can calculate a fix
    scaling factor in order to stretch out the histogram to the available data
    range. The scaling factor is calculated from the maximum gray value of the
    object divided by the total number of available gray values of the data
    set, e.g., a maximum gray value of 200 in a 8-bit data set would result in a
    scaling factor of 78%.

    :Important:
    The value must be between *0* and *100*, and will be clamped to this interval.

    :Hint:
    This scaling factor is only used if ``FixedValueI0`` is set for param
    ``ReconstructionRadiationIntensityCompensationMode``
    """

    ReconstructionRingArtifactReductionMode: ReconstructionRingArtifactReductionMode = (
        ReconstructionRingArtifactReductionMode.Off
    )
    """
    Defines the mode for ring artifact reduction.

    Use these modes to reduce ring artifact in the reconstructed volume.

    :Hint:
    Optional definition.
    """

    ReconstructionFieldOfViewExtensionMode: ReconstructionFieldOfViewExtensionMode = (
        ReconstructionFieldOfViewExtensionMode.No
    )
    """
    Sets the field of view extension mode

    The effective field of view for reconstruction can be extended by either
    moving the detector or the object rotation axis. When enabled, set the
    corresponding shift via param ``ReconstructionFieldOfViewExtensionShift``.

    :Hint:
    Optional definition. The default value is No (=no field of view extension)
    """

    ReconstructionFieldOfViewExtensionShift: float = 0
    """
    Defines the shift to be used for field of view extension.

    Depending on the specified field of view extension mode, either the object
    or the detector is shifted by the given value in *mm*.

    :Hint:
    Optional definition. The default value is ``0``, i.e. no shift distance.
    """

    ReconstructionEnsureIsotropicVoxelSize: bool = False
    """
    Determines whether the voxel size will be calculated automatically.

    When this option is set to true, the dimensions of the reconstructed volume
    are calculated automatically from the detector number of pixels. When set to
    ``False``, the result number of voxels can be specified manually.

    :Hint:
    Optional definition.
    """

    ReconstructionAutomaticAdaptiveDetectorBinning: bool = False
    """
    Determines whether automatic adaptive detector binning is used.

    When this option is set to true, projection image filters are automatically
    adapted to the scan geometry and voxel size. When set to ``False``, the
    projection image filters can be specified manually.

    :Hint:
    Optional definition.
    """
