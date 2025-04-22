"""Manufacturer info."""

from dataclasses import dataclass, field
from typing import Mapping


@dataclass
class ManufacturerInfoSection:
    """Information about the CT scanner manufacturer and the CT scanner itself."""

    Name: str = ""
    """ Defines the manufacturer of the CT scanner. """

    Address: str = ""
    """ Defines the manufacturer address. """

    Homepage: str = ""
    """ Defines the homepage of the scanner manufacturer. """

    DeviceName: str = ""
    """ Defines the designation of the CT scanner. """

    AcquisitionSoftware: str = ""
    """ Defines the software name and version used with the CT scanner. """

    Metadata: Mapping[str, str] = field(default_factory=dict)
    """ Used to defines custom component information via a key, value dict """
