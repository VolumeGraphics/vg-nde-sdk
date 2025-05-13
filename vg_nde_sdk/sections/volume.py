"""Volume descriptor."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from .component import ComponentInfoSection
from .manufacturer import ManufacturerInfoSection
from .scan import ScanInfoSection
from .types import Vector2f, Vector3f, Vector3i, Vectorf
from .volume_enums import (
    VolumeAxesSwapMode,
    VolumeDataMappingMode,
    VolumeDataType,
    VolumeEndian,
    VolumeFileFormat,
    VolumeSliceInterpolationMode,
)


@dataclass
class VolumeFileSection:
    """Descriptor class to define a single file of a volume data set import."""

    FileName: Path
    """
    Defines name of this file, preferably as an absolute path.
    For file naming convention, see \ref SectionProjectNomenclature section project nomenclature.
    """

    FileFileFormat: VolumeFileFormat = VolumeFileFormat.Raw
    """
    Defines the format of the file.

    Optional definition.
    """

    FileDataType: VolumeDataType = VolumeDataType.UInt16
    """
    Defines the type of the voxel values inside the file data.

    You must specify the data type explicitly, even if the file format contains
    implicit information about the type. This is due to the fact that while
    specifying the VolumeDescriptor, the files are not really accessed.

    Mandatory definition.
    """

    FileEndian: VolumeEndian = VolumeEndian.Little
    """
    Defines file's endianness.

    Defines the endianness of the voxel values inside the file data.
    Only relevant for Raw or Gzip data with > 8 bits per pixel.

    Optional definition.
    """

    FileSize: Vector3i = Vector3i(0, 0, 0)
    """
    Defines the dimensions of the (3D-)volume or (2D-)image stored in the file.

    You must specify the size explicitly, even if the file format contains
    implicit information about the volume size. This is due to the fact that
    while specifying the VolumeDescriptor, the files are not really accessed.

    Mandatory definition. The default value is Vector3(0, 0, 0), i.e. an invalid
    size.
    """

    FileHeaderSkip: int = 0
    """
    Defines file header size in bytes.

    Defines the number of bytes to be skipped at the beginning of the file.
    Only relevant for Raw or Gzip data (see FileFileFormat).

    Optional definition. The default value is 0.
    """

    FilePositionList: Vectorf = Vectorf()
    """
    Defines physical positions of the file's slices.

    Defines the relative physical position of all the slices represented by
    this file. Use this function to define non-equidistant slices: normally,
    the slice distance is determined globally by the z-component of
    VolumeDescriptor::setResolution(), i.e. all given xy-slices are the same
    distance apart. If your scanned data has varying slice distances, however,
    you can define a kind of physical position (in mm) for each slice.
    These distances will then be used instead of the z-resolution value,
    which will be ignored.

    You cannot "mix" specifications: if you specify a position list,
    you must do it for all files in the VolumeDescriptor, and each file must
    specify as many positions as its z-size indicates!

    Optional definition.
    """


@dataclass
class VolumeMetaInfoContainer:
    """Container holding volume meta info."""

    ComponentInfo: ComponentInfoSection = field(default_factory=ComponentInfoSection)
    ManufacturerInfo: ManufacturerInfoSection = field(
        default_factory=ManufacturerInfoSection
    )
    ScanInfo: ScanInfoSection = field(default_factory=ScanInfoSection)


@dataclass
class VolumeSection:
    """Descriptor class to completely define a volume data set import."""

    ObjectNameInScene: str = ""
    """
    Controls the name of the object in the scene.

    Controls the name of the volume object in the scene of the saved vg project.
    By default, this name is automatically created (e.g. "Volume 1"). If you set
    a custom name and it conflicts with the name of another object in the
    scene, it is possible that the application will append something to the name
    to make it unique (similar to renaming in VGSTUDIO (MAX) itself).

    :Hint:
    Optional. If you do not set anything or set the empty string, the name will
    be automatically created.

    :Important:
    Names are used to find appropriate objects during macro playback. If you
    plan on using your created projects in automation scenarios, it is advised
    to stick with the default names.
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
    Optional. If you do not set anything here, the meta information will be empty.
    """

    VolumeRotation: Vector3f = Vector3f(0, 0, 0)
    """
    Controls the rotation of the volume in the scene.

    This may be used to change the orientation of the volume in the scene.
    The x-, y- and z-component of the vector contain the angle of rotation
    (in degree) for heading, elevation and bank (euler angles), respectively.
    See http://en.wikipedia.org/wiki/Euler_Angles for a definition of euler
    angles

    :Hint:
    Optional. If you do not set this, the axes of the volume will be aligned to
    the ones of the scene coordinate system.
    """

    VolumeTranslation: Vector3f = Vector3f(0, 0, 0)
    """
    Controls the position of the volume in the scene.

    A translation vector which may be used to change the position of the volume
    in the scene. The origin (which is the center of the volume) will be
    translated according to the supplied vector.

    :Hint:
    Optional. If you do not set this, the origin of the volume will lie in the
    origin of the scene.
    """

    VolumeAutomaticSourceRangeDetectionMode: bool = False
    """
    Toggle automatic grey value range detection.

    Enable this setting to perform an automated analysis of the original data's
    grey value histogram, resulting in a suitable automatic definition for the
    source data mapping range.
    If enabled, you specify a percentual range *(range.a, range.b)* with the
    param ``VolumeAutomaticSourceRangeDetectionBoundaries``.
    For *(range.a, range.b)* each between *0.0f* and *100.0f*, a source range is
    chosen such that *range.a* percent of the grey value histogram lie below the
    lower range boundary, and *range.a* percent of the grey value histogram lie
    above the upper range boundary.

    Use this setting with `percentages > 0` to automatically detect *outlier
    grey values* that will then be clamped prior to conversion into the
    destination type, which results in better exhaustion of the available
    destination precision.

    :Important:
    The automatic detection will override any range specified manually with
    param ``VolumeSourceRange``.

    :Hint:
    Optional definition.
    """

    VolumeAutomaticSourceRangeDetectionBoundaries: Vector2f = Vector2f(0, 0)
    """
    Defines percentual boundaries for automatic range detection.

    Defines percentual histogram boundaries for automatic range detection.
    See param ``VolumeAutomaticSourceRangeDetectionMode``.

    :Hint:
    Optional definition.
    """

    VolumeSourceRange: Vector2f = Vector2f(0, -1)
    """
    Defines usable source grey value range

    Defines the grey value range, in valid units of the original source data
    type (defined by information in file list), that should be mapped into the
    resulting datasets type. The exact way of this mapping is specified by
    param ``VolumeDataMappingMode``. Input values outside the specified range
    will be handled differently, depending on the mapping mode.

    :Important:
    If a ``Float`` data type is mapped on a destination type that is not
    ``Float``, a source range **must** be specified, either manually or via
    automatic detection with param ``VolumeAutomaticSourceRangeDetectionMode``.

    :Hint:
    Optional definition. The default value is ``Vector2f(0, -1.0f)``, denoting
    the full available range.
    """

    VolumeDestinationDataType: VolumeDataType = VolumeDataType.UInt16
    """
    Defines data type of destination volume.

    Defines the desired data type of the finally imported volume data.
    Regardless of the data type of the individual input files
    (see param ``VolumeFileSection.FileDataType``), the resulting data type can
    be chosen independently. For example, you can reduce 16-bit input data to
    8-bit result data to reduce memory consumption. The mapping between input
    and result data type is specified by params ``VolumeSourceRange``,
    ``VolumeDestinationRange`` and ``VolumeDataMapepingMode``.

    :Hint:
    Optional definition.
    """

    VolumeDataMappingMode: VolumeDataMappingMode = VolumeDataMappingMode.Ramp
    """
    Defines mapping of source to destination grey values.

    Defines the way grey values are mapped from the source data type to the
    destination type.  Given source range :math:`(source.a, source.b)` and
    destination range :math:`(destination.a, destination.b)` -- as defined
    e.g. via params ``VolumeSourceRange`` and ``VolumeDestinationRange``,
    values are always mapped in a linear manner.
    In mode ``Ramp`` and ``Sawtooth``, input values
    inside :math:`(source.a, source.b)` are mapped to the destination range
    linearly as:
        .. math:: source.a \\rightarrow destination.a ; source.b \\rightarrow destination.b
    For modes ``InverseRamp``, and ``InverseSawtooth`` the mapping is:
        .. math:: source.a \\rightarrow destination.b ;  source.b \\rightarrow destination.a
    i.e. a reverse linear mapping.

    Values outside the specified source range are handled differently:
    - ``Ramp``
        .. math:: x < source.a \\rightarrow destination.a ;  x > source.b \\rightarrow destination.b
    - ``Sawtooth``
        .. math:: x < source.a \\rightarrow destination.a ;  x>source.b \\rightarrow destination.a
    - ``InverseRamp``
        .. math:: x < source.a \\rightarrow destination.b ;  x > source.b \\rightarrow destination.a
    - ``InverseSawtooth``
        .. math:: x < source.a \\rightarrow destination.b ;  x > source.b \\rightarrow destination.b

    :Hint:
    Optional definition
    """

    VolumeDestinationRange: Vector2f = Vector2f(0, -1)
    """
    Defines usable destination grey value range

    Defines the grey value range, in valid units of the specified destination
    data type (param ``VolumeDestinationDataType``), that the original data
    values should be mapped onto. The exact way of this mapping is specified by
    param ``VolumeDataMappingMode``.

    :Hint:
    Optional definition. The default value is ``Vector2f(0, -1)``, denoting the
    full available range.
    """

    VolumeResolution: Vector3f = Vector3f(1, 1, 1)
    """
    Defines base resolution of the entire volume data set.

    Defines (in *mm*) the voxel resolution of the data set along each axis.
    Note that this defines the resolution of the volume before any voxel skip,
    resampling, or axis swapping is done. The z-resolution can become obsolete
    if you provide explicit position information for each slice (see
    param ``VolumeFileSection.FilePositionList``).

    :Hint:
    Optional definition. The default value is ``Vector3f(1, 1, 1)``, i.e. a
    standard unit resolution.
    """

    VolumeSliceInterpolationMode: VolumeSliceInterpolationMode = (
        VolumeSliceInterpolationMode.On
    )
    """
    Defines non-equidistant slice interpolation mode.

    Generally, all volume data is considered to be "continuous", i.e. positions
    between voxel centers have a grey value determined by interpolating between
    the neighbouring voxel information. For equidistant volume data sets, this
    is always pragmatic. If, however, you have non-equidistant slices
    (whose position information is specified using param
    ``VolumeFileSection.FilePositionList``), it is possible to create
    significant "gaps" in the data. Between those gaps, applications can either
    interpolate as usual, or treat the gap as an empty/undefined area.

    If this is set to ``Threshold`` and a valid threshold distance is given in
    *mm* by param ``VolumeSliceInterpolationThreshold``, all slices that
    are further apart form each other than the threshold will be split apart,
    so that no interpolation is done between them. If this is set to ``On``, the
    application will always interpolate between gaps. If this is set to
    ``Off``, no interpolation will be done.

    :Hint:
    Optional definition.
    """

    VolumeSliceInterpolationThreshold: float = 0
    """
    Defines the desired threshold distance for slice interpolation.

    This setting is only relevant if slice interpolation mode is enabled (see
    param ``VolumeSliceInterpolationMode``).

    :Important:
    This is a mandatory param if param ``VolumeSliceInterpolationMode`` is set
    to anything other than ``Off``. The default value is *0*, i.e. an invalid
    threshold.
    """

    VolumeResamplingMode: bool = False
    """
    Toggles resampling of volume data.

    Toggles this setting to force a resampling of the original volume data.
    This can be used to make a dataset isotropic: If slice distances
    are significantly higher than the in-slice resolution, you can enable
    resampling, define an isotropic resolution with param
    ``ResamplingResolution`` and the resulting volume will be uniform.

    Depending on the original resolution and the resampling resolution, the
    resulting volume will consist of a different number of voxels.

    :Hint:
    Optional definition.
    """

    VolumeResamplingResolution: Vector3f = Vector3f(1, 1, 1)
    """
    Defines the desired final resolution for resampling.

    This setting is only relevant if resampling is enabled by param
    ``VolumeResamplingMode``. Use this to define the desired final
    resolution of the volume data set. Voxel values will be taken from the
    original data, but will most likely be interpolated (i.e. resampled) due
    to the different resolutions.

    :Important:
    The components of this param refer to the original axes of the
    volume, before any swapping is applied (see param ``VolumeAxesSwapMode``).

    :Hint:
    Mandatory param if param ``VolumeResamplingMode`` is set to ``True``. The
    default value is ``Vector3f(1, 1, 1)``, i.e. a most probably inappropriate
    resolution.
    """

    VolumeRegionOfInterestMin: Vector3i = Vector3i(0, 0, 0)
    """
    Defines the lower boundary of a region of interest on the base volume.

    The *base* volume is the volume comprised of all the voxels contained in
    all the (stacked) files defined via param ``VolumeProjections``. The number
    of voxels in the base volume is thus defined by the sizes of the files.
    Using this and param ``VolumeRegionOfInterestMax``, you can restrict the
    volume. Given values are voxel indices, that means they have to lie in the
    range of :math:`0 <= value < basesize` along each axis. The upper boundary
    must not be smaller than the lower boundary, except for the special
    pair ``Vector3i(0, 0, 0)`` / ``Vector3i(-1, -1, -1)`` which denotes the full
    volume with no ROI.

    :Important:
    This param will be ignored if auto-ROI mode is turned on
    (see param ``VolumeAutoRegionOfInterestMode``).

    :Hint:
    Optional definition. The default value is ``Vector3i(0, 0, 0)``,
    i.e. the full volume (when param ``VolumeRegionOfInterestMax`` is
    ``Vector3i(-1, -1, -1)``).
    """

    VolumeRegionOfInterestMax: Vector3i = Vector3i(-1, -1, -1)
    """
    Defines the upper boundary of a region of interest on the base volume.

    Region of interest definition; see param ``VolumeRegionOfInterestMin``.

    :Important:
    This param will be ignored if auto-ROI mode is turned on
    (see param ``VolumeAutoRegionOfInterestMode``).

    :Hint:
    Optional definition. The default value is ``Vector3i(-1, -1, -1)``,
    i.e. the full volume (when param ``VolumeRegionOfInterestMin`` is
    ``Vector3i(0, 0, 0)``).
    """

    VolumeAutoRegionOfInterestMode: bool = False
    """
    Turns auto-ROI mode on or off.

    To reduce memory consumption of the finally imported volume automatically,
    you can enable the auto-ROI mode. The volume data is analyzed before the
    final import, and a region of interest is calculated that contains all
    material, but ignores as much unused background space as possible.

    :Important:
    If this params is enabled, the manual ROI params will be ignored (see
    ``VolumeRegionOfInterestMax`` and ``VolumeRegionOfInterestMin``).

    :Hint:
    Optional definition.
    """

    VolumeVoxelSkip: Vector3i = Vector3i(0, 0, 0)
    """
    Defines the amount of voxels to be skipped when importing volume data.

    Defines, for each coordinate axis, the amount of voxels to be skipped when
    importing the specified volume data. At a skip factor of :math:`n ≥ 0`,
    only every (:math:`n + 1`)-th input voxel will be considered, the rest
    will be skipped. Skipping will decrease the number of voxels in the
    finally imported volume, thus reducing memory consumption significantly.

    :Important:
    Skipping is done after applying the region of interest (see
    param ``VolumeRegionOfInterestMin``), and before optional resampling
    (see param ``VolumeResamplingMode``).

    :Hint:
    Optional definition. The default value is ``Vector3i(0, 0, 0)``, i.e. no
    voxels are skipped.
    """

    VolumeMirrorAxisX: bool = False
    """
    Toggles volume mirror mode (X-axis).

    Toggles this setting to mirror the resulting volume data along the X-axis.
    This will effectively "reverse the direction" of the voxels along the axis.

    :Hint:
    Optional definition.
    """

    VolumeMirrorAxisY: bool = False
    """
    Toggles volume mirror mode (Y-axis).

    Toggles this setting to mirror the resulting volume data along the Y-axis.
    This will effectively "reverse the direction" of the voxels along the axis.

    :Hint:
    Optional definition.
    """

    VolumeMirrorAxisZ: bool = False
    """
    Toggles volume mirror mode (Z-axis).

    Toggles this setting to mirror the resulting volume data along the Z-axis.
    This will effectively "reverse the direction" of the voxels along the axis.

    :Hint:
    Optional definition.
    """

    VolumeAxesSwapMode: VolumeAxesSwapMode = VolumeAxesSwapMode.XYZ
    """
    Defines volume axis swapping.

    Defines an axis swap if you want the final volume's axes to represent a
    different axis combination as the initial data in the file. For example,
    an axis swap value ``YXZ`` will exchange the X- and Y-axis.

    :Hint:
    Optional definition. The default value is ``XYZ``, i.e. no swapping.
    """

    VolumeAlignedClippingBoxMin: Vector3f = Vector3f(0, 0, 0)
    """
    Defines the lower boundary of an axis aligned clipping box.

    Defining a clipping box will only change the visual appearance of the volume
    and has no influence on the actual data. The box is defined in the grid
    coordinate system of the volume. Everything outside of it will be clipped.
    Defining a clipping box this way is equivalent to using the
    "Axis aligned clippingbox" functionality/dialogue in VGSTUDIO (MAX).
    If an invalid or empty box is specified, nothing will be clipped.
    The clipping box will be intersected with the bounding box of the volume.

    :Important:
    The grid coordinates of the clipping box refer to the "final" grid
    coordinate system of the volume (after resampling, ROI, axes swap etc. have
    been handled).

    :Hint:
    Optional definition. The default value is ``Vector3f(0, 0, 0)``,
    with param ``VolumeAlignedClippingBoxMax`` being ``Vector3f(-1, -1, -1)``,
    an invalid box.
    """

    VolumeAlignedClippingBoxMax: Vector3f = Vector3f(-1, -1, -1)
    """
    Defines the upper boundary of an axis aligned clipping box.

    Axis aligned clipping box; see param ``VolumeAlignedClippingBoxMin``.

    :Hint:
    Optional definition. The default value is ``Vector3f(-1, -1, -1)``,
    with param ``VolumeAlignedClippingBoxMin`` being ``Vector3f(0, 0, 0)``,
    an invalid box.
    """

    VolumeProjections: Sequence[VolumeFileSection] = field(default_factory=tuple)
    """
    Set of file(s) the volume consists of.

    :Hint:
    Mandatory definition. At least one file must be specified to define a valid
    volume.
    """
