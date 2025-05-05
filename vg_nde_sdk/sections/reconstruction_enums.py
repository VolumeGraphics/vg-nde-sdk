"""Reconstruction enums."""

from enum import Enum


class ReconstructionGeneralSystemGeometryMode(Enum):
    """Mode used for reconstructing, depending on the setup used to create the scan."""

    ConeBeamCT = "ConeBeamCT"
    """ Standard circle trajectory with 2D detector. """

    FanBeamCT = "FanBeamCT"
    """ Standard circle trajectory setup using line detector """

    ParallelBeamCT = "ParallelBeamCT"
    """ Standard circle trajectory with parallel x-ray beams. """

    PlanarCT = "PlanarCT"
    """
    Planar setup (laminography geometry),
    for details see docs/vg-reconstruction-planar.pdf.
    """

    HelixCT = "HelixCT"
    """ Helix trajectory with 2D detector. """


class ReconstructionAlgorithmicOptimizationMode(Enum):
    """Controls whether the reconstruction algorithm favours quality or performance."""

    Quality = "Quality"
    """ Quality mode. """

    Performance = "Performance"
    """ Performance mode. """


class ReconstructionGeometricSetup(Enum):
    """Used to define which setup was used during planar CT.."""

    RotateFrustum = "RotateFrustum"
    """ Center ray always orthogonal to detector. """

    PerspectiveWarp = "PerspectiveWarp"
    """ Center ray NOT always orthogonal to detector. """

    AdvancedPlanarCT = "AdvancedPlanarCT"
    """ Based on translational movement of two separate tables. """


class ReconstructionRotationDirection(Enum):
    """Used to define the rotational direction of the reconstruction."""

    CounterClockwise = "CounterClockwise"
    """ Counterclockwise rotation of the object when viewed from above. """

    Clockwise = "Clockwise"
    """ Clockwise rotation of the object when viewed from above. """


class ReconstructionPreprocessingMode(Enum):
    """Defines which preprocessing method will be used."""

    Off = "Off"
    """
    The projection files have already been completely preprocessed
    (calibrated and high pass filtered). The data will be used "as is".
    """

    Filter = "Filter"
    """
    The projection files have already been calibrated and logarithmized.
    The data will be high pass filtered.
    """

    CalibrateAndFilter = "CalibrateAndFilter"
    """
    The projection files have not been preprocessed.
    The data will be calibrated and high pass filtered.
    """


class ReconstructionProjectionSorting(Enum):
    """Defines order in which the projection data files will be read and reconstructed."""

    def __str__(self):
        """Provide custom string for format compatibility."""
        return str("ReconstructionSorting." + self.value)

    NumbersUp = "NumbersUp"
    """
    The data files will be sorted according to increasing numbers in the file
    name (e.g. a0, d1, c2, b20).
    """

    Off = "Off"
    """
    The data files won't be sorted, instead the order in which they were added
    will be used.
    """

    AlphabeticUp = "AlphabeticUp"
    """ The data files will be sorted alphabetically (e.g. a0, b20, c2, d1). """

    CanonicUp = "CanonicUp"
    """
    The data files will be sorted first by length of filename, then
    alphabetically.
    """

    ReverseUp = "ReverseUp"
    """
    The numbers in the file name will be read "backwards"
    (e.g. 0021 becomes 1200) and the resulting names sorted alphabetically.
    """


class ReconstructionProjectionDataType(Enum):
    """Defines the data type as stored in the file(s)."""

    UInt16 = "UInt16"
    """ Unsigned 16 bit coded gray values. """

    Int16 = "Int16"
    """ Signed 16 bit coded gray values. """

    UInt32 = "UInt32"
    """ Unsigned 32 bit coded gray values. """

    Int32 = "Int32"
    """ Signed 32 bit coded gray values. """

    Float = "Float"
    """ 32 bit float, will be clamped to [0,1.0f] during import. """

    Float16 = "Float16"
    """ 32 bit float, will be clamped to [0,2^16-1] during import. """

    Float20 = "Float20"
    """ 32 bit float, will be clamped to [0,2^20-1] during import. """


class ReconstructionProjectionOrientation(Enum):
    """Defines if the y and z axes of the projections will be swapped."""

    def __str__(self):
        """Provide custom string for format compatibility."""
        return str("ReconstructionOrientation." + self.value)

    YZ = "YZ"
    """ Axes will not be swapped. """

    ZY = "ZY"
    """ Axes will be swapped from YZ to ZY. """


class ReconstructionProjectionFileFormat(Enum):
    """Defines the format of the data files."""

    def __str__(self):
        """Provide custom string for format compatibility."""
        return str("ReconstructionFileFormat." + self.value)

    Raw = "Raw"
    """ Signed/unsigned 8/16/32 bit integer, 32 bit float or 32 bit RGBA. """

    Gzip = "Gzip"
    """ Signed/unsigned 8/16/32 bit integer, 32 bit float or 32 bit RGBA. """

    Tiff = "Tiff"
    """ Signed/unsigned 8/16 bit integer, 8/16 bit RGB or 8/16 bit RGBA. """

    Jpeg = "Jpeg"
    """ Color and gray scale images. """

    Bmp = "Bmp"
    """ Color and gray scale images. """

    Jpeg2 = "Jpeg2"
    """ 8/16 bit gray scale images, 8 bit RGB or 8 bit RGBA. """

    Imtec = "Imtec"
    """ Grayscale images from IMTEC CT systems. """


class ReconstructionProjectionFileEndian(Enum):
    """Defines the byte order (endianness) of the data type elements of the files."""

    def __str__(self):
        """Provide custom string for format compatibility."""
        return str("ReconstructionEndian." + self.value)

    Little = "Little"
    """
    The memory location with the lowest address contains the least significant
    byte.
    """

    Big = "Big"
    """
    The memory location with the lowest address contains the most significant
    byte.
    """


class ReconstructionProjectionSmoothingMode(Enum):
    """Applies a Gaussian filter mask on each projection slice."""

    def __str__(self):
        """Provide custom string for format compatibility."""
        return str("ReconstructionSmoothingMode." + self.value)

    Off = "Off"
    """ No projection smoothing is done. """

    Low = "Low"
    """ Gaussian filter mask with 3 x 3 pixels. """

    Medium = "Medium"
    """ Gaussian filter mask with 7 x 7 pixels. """

    High = "High"
    """ Gaussian filter mask with 11 x 11 pixels. """


class ReconstructionCalibrationMode(Enum):
    """Defines which calibration method will be used."""

    No = "None"  # This value differs from its key on purpose!
    """ No calibration file will be used. """

    All = "All"
    """ Two calibration files ("bright" and "dark") will be used. """

    OnlyBright = "OnlyBright"
    """ One calibration file ("bright") will be used. """


class ReconstructionCalibrationFilterMode(Enum):
    """Applies a Gaussian filter mask on the calibration images."""

    Off = "Off"
    """ No projection smoothing is done. """

    Low = "Low"
    """ Gaussian filter mask with 3 x 3 pixels. """

    Medium = "Medium"
    """ Gaussian filter mask with 7 x 7 pixels. """

    High = "High"
    """ Gaussian filter mask with 11 x 11 pixels. """


class ReconstructionMisalignmentCorrectionMode(Enum):
    """Defines desired mode of automatic geometry correction."""

    Off = "Off"
    """ No calculations for detector geometry correction will done. """

    HorizontalDetectorOffset = "HorizontalDetectorOffset"
    """ Automatically calculate value for horizontal detector offset. """

    RotationAxisTiltXZ = "RotationAxisTiltXZ"
    """ Automatically calculate value for axis tilt correction. """

    All = "All"
    """
    Calculate values for horizontal detector offset and axis tilt correction
    both.
    """


class ReconstructionMisalignmentOptimizationMode(Enum):
    """Defines misalignment correction optimization for full or short scans."""

    FullScan = "FullScan"
    """
    Optimize correction for full scans that were created using a large angular
    section.
    """

    ShortScan = "ShortScan"
    """
    Optimize correction for short scans that were created using an angular
    section around 180°.
    """


class ReconstructionMisalignmentSkipMode(Enum):
    """Defines the skip strategy mode for automatic geometry correction."""

    Auto = "Auto"
    """
    In auto mode, the skip/precision is automatically determined by the
    geometric setup, e.g.  number of reconstruction voxels and number of
    detector pixels.
    """

    Off = "Off"
    """ Never skip reconstructed voxels. """

    On = "On"
    """
    Always skip with the value defined by param
    ``ReconstructionSection.ReconstructionMisalignmentSkip``.
    """


class ReconstructionInterpolationMode(Enum):
    """Defines which interpolation method will be used."""

    Linear = "Linear"
    """ Interpolates linearly between given data points. """

    Nearest = "Nearest"
    """ Uses the value of the nearest neighbor. """


class ReconstructionFilterMode(Enum):
    """Defines which filter method will be used for the high pass filtering."""

    SheppLogan = "SheppLogan"
    """
    Filters the data using a modified ramp. The higher frequencies are slightly
    less emphasized compared to the ramp filter.
    """

    Ramp = "Ramp"
    """
    Filters the data using a ramp. The higher frequencies are slightly more
    emphasized compared to the Shepp-Logan filter.
    """


class ReconstructionSpeckleRemovalMode(Enum):
    """Defines the method used for speckle removal."""

    Off = "Off"
    """ No speckle removal will be done. """

    MultiPixel = "MultiPixel"
    """ Speckle removal enabled, optimized for neighboring defective pixels. """

    SinglePixel = "SinglePixel"
    """ Speckle removal enabled, optimized for singular defective pixels. """


class ReconstructionCalculationMode(Enum):
    """Specifies how the Feldkamp reconstruction is calculated."""

    CPU = "CPU"
    """ Reconstruction via the CPU """

    GPU = "GPU"
    """
    Reconstruction via the GPU. Deprecated, single-GPU support.
    Do not use in new projects!
    """

    OpenCL = "OpenCL"
    """ Reconstruction via OpenCL. Recommended, includes multi-GPU support. """


class ReconstructionBeamHardeningCorrectionMode(Enum):
    """Defines beam hardening correction mode."""

    Off = "Off"
    """ No beam hardening correction is done. """

    Preset = "Preset"
    """
    Use correction preset, which will then be used to correct the projection
    data during the calibration process.
    """


class ReconstructionBeamHardeningCorrectionPresetMode(Enum):
    """Defines beam hardening correction preset."""

    Static = "Static"
    """ Do not overwrite the LUT range of the current preset. """

    Dynamic = "Dynamic"
    """
    Adjusts the user defined presets to the actual data range of the current
    data set.
    """

    Explicit = "Explicit"
    """
    Set LUT range values via
    ``ReconstructionSection.ReconstructionBeamHardeningCorrectionPresetValueRange``,
    overwrites the Lut range of presets.
    """

    Automatic = "Automatic"
    """
    Uses mode defined in the user defined preset (Dynamic or Static),
    and Dynamic for predefined presets.
    """


class ReconstructionMultipleROIPositioningMode(Enum):
    """Defines positioning of reconstructed volumes of a multi ROI reconstruction."""

    KeepOrientation = "KeepOrientation"
    """ Reconstructed volumes will keep their positions relative to each other. """

    MoveToCenter = "MoveToCenter"
    """ Reconstructed volumes will be positioned in the center of the scene. """


class ReconstructionClampType(Enum):
    """Defines the gray value clamping type."""

    AbsoluteClamping = "AbsoluteClamping"
    """ The given value denotes absolute gray values. """

    PercentalClamping = "PercentalClamping"
    """ The given value denotes percent of the gray value histogram. """


class ReconstructionResultDataType(Enum):
    """Defines the result volume slice data type.

    :Hint:
    Objects with 32 bit signed/unsigned data have an effective data range of
    20 bit for all rendering procedures (full data range for analysis procedures).
    """

    UInt8 = "UInt8"
    """ Unsigned 8 bit coded gray values, 0 to 255. """

    UInt12 = "UInt12"
    """ Unsigned 12 bit coded gray values, 0 to 4095. """

    UInt16 = "UInt16"
    """ Unsigned 16 bit coded gray values, 0 to 65535. """

    Float = "Float"
    """ 32 bit float (3D rendering as 16 bit). """


class ReconstructionResultImportMode(Enum):
    """Defines the import mode for reconstructed volume data."""

    WriteToDiskAndImport = "WriteToDiskAndImport"
    """
    Save reconstructed volume data to disk and immediately load it into the scene.
    Reference volume data.
    """

    DirectReference = "DirectReference"
    """
    Don't save volume data to disk after reconstruction, only load into scene.
    Reference projection data.
    """

    WriteToDiskOnly = "WriteToDiskOnly"
    """
    Save volume data to disk, but don't load it into the scene after that.
    Reference volume data.
    """


class ReconstructionImportMode(Enum):
    """Legacy enum for ``ReconstructionResultImportMode``.

    Defines the import mode for reconstructed volume data.
    """

    WriteToDiskAndImport = "WriteToDiskAndImport"
    """
    Save reconstructed volume data to disk and immediately load it into the scene.
    Reference volume data.
    """

    DirectReference = "DirectReference"
    """
    Don't save volume data to disk after reconstruction, only load into scene.
    Reference projection data.
    """

    WriteToDiskOnly = "WriteToDiskOnly"
    """
    Save volume data to disk, but don't load it into the scene after that.
    Reference volume data.
    """


class ReconstructionMetalArtifactReductionMode(Enum):
    """Defines the mode for metal artifact reduction."""

    Off = "Off"
    """ No metal artifact reduction. """

    MAR = "MAR"
    """ Use metal artifact reduction. """

    sMARt = "sMARt"
    """ Use advanced metal artifact reduction. """


class ReconstructionMetalArtifactReductionThresholdMode(Enum):
    """Defines the threshold mode for metal artifact reduction."""

    Relative = "Relative"
    """ Use a relative threshold value. """

    Absolute = "Absolute"
    """ Use an absolute threshold value. """


class ReconstructionAlgorithmMode(Enum):
    """Defines the used algorithm for reconstruction."""

    FBP = "FBP"
    """ Use filtered backprojection. """

    ART = "ART"
    """
    Use algebraic reconstruction technique. Should be used together with
    ``ReconstructionCalculationMode.OpenCL``.
    """


class ReconstructionRadiationIntensityCompensationMode(Enum):
    """Compensate varying gray values in projections."""

    Off = "Off"
    """ Use if there is now air in the projection. """

    ProjectionMax = "ProjectionMax"
    """ Use the maximum value of each projection for normalization. """

    ProjectionPeak = "ProjectionPeak"
    """ Use the peak air value of each projection for normalization. """

    FixedValueI0 = "FixedValueI0"
    """ Use a fixed scaling factor for projection normalization. """


class ReconstructionRingArtifactReductionMode(Enum):
    """Specifies the mode used for compensating ring artifacts."""

    Off = "Off"
    """ No ring artifact reduction. """

    Low = "Low"
    """ Low filtering to reduce ring artifacts. """

    Medium = "Medium"
    """ Medium filtering to reduce ring artifacts. """

    High = "High"
    """ High filtering to reduce ring artifacts. """


class ReconstructionFieldOfViewExtensionMode(Enum):
    """Defines the mode for field of view extension."""

    No = "None"  # This value differs from its key on purpose!
    """ No extension of field of view. """

    Detector = "Detector"
    """ Extend field of view by detector shift. """

    Object = "Object"
    """ Extend field of view by object shift. """
