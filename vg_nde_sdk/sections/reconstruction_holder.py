"""Container holding the reconstructions."""

from dataclasses import dataclass, field
from typing import Sequence

from .reconstruction import ReconstructionSection


@dataclass
class ReconstructionSectionHolder:
    """Reconstruction section holder."""

    reconstructions: Sequence[ReconstructionSection] = field(default_factory=tuple)
