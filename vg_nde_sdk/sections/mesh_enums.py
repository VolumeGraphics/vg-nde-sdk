"""Enums for volume descriptor."""

from enum import Enum


class MeshFormat(Enum):
    """Specifies the format of a mesh file."""

    STL = "STL"
    """ Stereolithography file format """

    OBJ = "OBJ"
    """ Wavefront OBJ file format """

    PLY = "PLY"
    """ Polygon File Format """


class MeshUnit(Enum):
    """Specifies the unit that should be used for loading a mesh."""

    Kilometer = "Kilometer"
    Meter = "Meter"
    Centimeter = "Centimeter"
    Millimeter = "Millimeter"
    Micrometer = "Micrometer"
    Nanometer = "Nanometer"
    Inch = "Inch"
    Foot = "Foot"
    Yard = "Yard"
    Mile = "Mile"
