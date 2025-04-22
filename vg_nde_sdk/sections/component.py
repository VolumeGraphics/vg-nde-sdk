"""Component info section."""

from dataclasses import dataclass, field
from typing import Mapping


@dataclass
class ComponentInfoSection:
    """Defines all information related to the component."""

    Description: str = ""
    """ Defines a description of the scanned object. """

    LotNumber: str = ""
    """ Defines the lot number of the scanned component. """

    ProductionDateTime: str = ""
    """
    Defines the production date and time of the scanned component.
    Date time format: *DD.MM.YYYY hh:mm:ss* or *YYYY-MM-DD hh:mm:ss*.
    """

    CavityNumber: str = ""
    """ Defines the cavity number of the scanned component. """

    SerialNumber: str = ""
    """ Defines the serial number of the scanned component. """

    Metadata: Mapping[str, str] = field(default_factory=dict)
    """ Used to defines custom component information via a key, value dict """
