"""Volume descriptor."""

from dataclasses import dataclass
from pathlib import Path

from .mesh_enums import MeshFormat, MeshUnit
from .types import Vector3f


@dataclass
class MeshSection:
    """Descriptor class to completely define a mesh data set import."""

    FileName: Path
    """
    Path to the mesh file that has to be imported.

    Mandatory definition.
    """

    MeshFormat: MeshFormat = MeshFormat.STL
    """
    Defines the format of the mesh file.

    Optional definition.
    """

    MeshRotation: Vector3f = Vector3f(0, 0, 0)
    """
    Controls the rotation of the mesh in the scene.

    This may be used to change the orientation of the volume in the scene.
    The x-, y- and z-component of the vector contain the angle of rotation
    (in degree) for heading, elevation and bank (euler angles), respectively.
    See http://en.wikipedia.org/wiki/Euler_Angles for a definition of euler
    angles

    :Hint:
    Optional. If you do not set this, the axes of the volume will be aligned to
    the ones of the scene coordinate system.
    """

    MeshTranslation: Vector3f = Vector3f(0, 0, 0)
    """
    Controls the position of the mesh in the scene.

    A translation vector which may be used to change the position of the mesh
    in the scene. The origin (which is the center of the volume) will be
    translated according to the supplied vector.

    :Hint:
    Optional. If you do not set this, the origin of the mesh will lie in the
    origin of the scene.
    """

    MeshUnit: MeshUnit = MeshUnit.Millimeter
    """
    Defines the unit of the legths within the mesh file.

    Optional definition.
    """

    ObjectNameInScene: str = ""
    """
    Controls the name of the object in the scene.

    Controls the name of the mesh object in the scene of the saved vg project.
    By default, this name is automatically created (e.g. "Mesh 1"). If you set
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
