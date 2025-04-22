"""Version info."""

from dataclasses import dataclass


@dataclass(frozen=True)
class VersionSection:
    """File version section."""

    Version: str = "3.0.0"
    """ Current version of the transferfile schema """
