"""Container holding the volumes."""

from dataclasses import dataclass, field
from typing import Sequence

from .volume import VolumeSection


@dataclass
class VolumeSectionHolder:
    """A container holding VolumeSection object(s)."""

    volumes: Sequence[VolumeSection] = field(default_factory=tuple)
