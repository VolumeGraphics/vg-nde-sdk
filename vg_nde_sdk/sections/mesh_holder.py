"""Container holding the Meshs."""

from dataclasses import dataclass, field
from typing import Sequence

from .mesh import MeshSection


@dataclass
class MeshSectionHolder:
    """A container holding MeshSection object(s)."""

    meshes: Sequence[MeshSection] = field(default_factory=tuple)
