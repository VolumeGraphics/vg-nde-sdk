"""Enums for volume descriptor."""

from enum import Enum


class VolumeFileFormat(Enum):
    """Defines the format of the data files."""

    Raw = "Raw"
    """ Signed/unsigned 8/16/32 bit integer, 32 bit float or 32 bit RGBA. """

    Gzip = "Gzip"
    """ Signed/unsigned 8/16/32 bit integer, 32 bit float or 32 bit RGBA. """

    Tiff = "Tiff"
    """ Signed/unsigned 8/16 bit integer, 8/16 bit RGB or 8/16 bit RGBA. """

    Jpeg = "Jpeg"
    """ Color and grayscale images """

    Bmp = "Bmp"
    """ Color and grayscale images """

    Bir = "Bir"
    """ 16 bit grayscale images from Varian/BIR CT systems. """

    Toshiba = "Toshiba"
    """" Signed 16 bit images from Toshiba CT systems. """

    Shimadzu = "Shimadzu"
    """ Grayscale images from Shimadzu CT systems. """

    Pnm = "Pnm"
    """ Binary 24 bit color and grayscale images. """

    Jpeg2 = "Jpeg2"
    """ 8/16 bit grayscale images, 8 bit RGB or 8 bit RGBA. """

    Yxlon = "Yxlon"
    """ Volumes from Yxlon line detector CT. """

    Hdf = "Hdf"
    """ Signed/unsigned 8/16/32 bit integer or 32 bit float. """

    Dicom = "Dicom"
    """
    Signed/unsigned 8/16/32 bit integer, typically from medical CT systems.
    """

    Imtec = "Imtec"
    """ Grayscale images from IMTEC CT systems. """

    Aracor = "Aracor"
    """ Grayscale images from Rapiscan CT systems. """

    Fhg = "Fhg"
    """
    Unsigned 8/16/32 bit integer from Fraunhofer CT systems or Werth CT systems.
    """

    ShimadzuVolume = "ShimadzuVolume"
    """ Grayscale volume from Shimadzu CT systems. """


class VolumeDataType(Enum):
    """Defines the data type as stored in the file(s).

    Objects with 32 bit signed/unsigned data have an effective data range
    of 20 bit for all rendering procedures (full data range for analysis
    procedures).
    """

    UInt8 = "UInt8"
    """ Unsigned 8 bit coded gray values, 0 to 255. """

    Int8 = "Int8"
    """ Signed 8 bit coded gray value, -128 to 127. """

    UInt16 = "UInt16"
    """ Unsigned 16 bit coded gray values, 0 to 65535. """

    Int16 = "Int16"
    """ Signed 16 bit coded gray values, -32768 to 32767. """

    UInt32 = "UInt32"
    """ Unsigned 32 bit coded gray values, 0 to 1048575. """

    Int32 = "Int32"
    """ Signed 32 bit coded gray values, -524288 to 524287. """

    Float = "Float"
    """ 32 bit float (3D rendering as 16 bit). """

    Rgb8 = "Rgb8"
    """ 8 bit per RGB component color images (total of 24 bit color) """


class VolumeDataMappingMode(Enum):
    """Defines the opacity mapping applied to the data range."""

    Ramp = "Ramp"
    """ Applies a ramp mapping (lower left to upper right). """

    InverseRamp = "InverseRamp"
    """ Applies an inverse ramp mapping (lower right to upper left). """

    Sawtooth = "Sawtooth"
    """
    Applies a sawtooth mapping (incline to peak from lower left to upper right).
    """

    InverseSawtooth = "InverseSawtooth"
    """
    Applies an inverse sawtooth mapping (incline to peak from lower right to upper left).
    """


class VolumeSliceInterpolationMode(Enum):
    """Defines non-equidistant slice interpolation mode."""

    On = "On"
    """ Always interpolates between gaps. """

    Off = "Off"
    """ Never interpolates between gaps. """

    Threshold = "Threshold"
    """
    Only interpolates between gaps if the gap is smaller than the given threshold.
    """


class VolumeAxesSwapMode(Enum):
    """Defines which axes will be swapped."""

    XYZ = "XYZ"
    """ Axes will not be swapped. """

    XZY = "XZY"
    """ Axes will be swapped from XYZ to XZY. """

    YXZ = "YXZ"
    """ Axes will be swapped from XYZ to YXZ. """

    YZX = "YZX"
    """ Axes will be swapped from XYZ to YZX. """

    ZXY = "ZXY"
    """ Axes will be swapped from XYZ to ZXY. """

    ZYX = "ZYX"
    """ Axes will be swapped from XYZ to ZYX. """


class VolumeEndian(Enum):
    """Defines byte order (endianness) of the data type elements of files."""

    Little = "Little"
    """
    The memory location with the lowest address contains the least significant byte.
    """

    Big = "Big"
    """
    The memory location with the lowest address contains the most significant byte.
    """
