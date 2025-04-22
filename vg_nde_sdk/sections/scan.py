"""Scan info."""

from dataclasses import dataclass, field
from typing import Mapping


@dataclass
class ScanInfoSection:
    """Information about the scan process."""

    TubeVoltage: str = ""
    """ Defines the acceleration voltage of the x-ray tube during the scan. """

    TubeCurrent: str = ""
    """ Defines the current of the x-ray tube during the scan. """

    ScanTime: str = ""
    """ Defines the time used for scanning the object. """

    ReconstructionTime: str = ""
    """ Defines the time used for the reconstruction. """

    TotalProcessTime: str = ""
    """
    Defines the time used for the whole process, including scanning the
    object, reconstructing the data and creating the project file.
    """

    ReconstructionAlgorithm: str = ""
    """ Defines which algorithm was used for the reconstruction, i.e. Feldkamp. """

    ScanMethod: str = ""
    """
    Defines the method which was used for scanning
    (e.g., stop-and-go, continuous rotation).
    """

    Geometry: str = ""
    """
    Returns the geometrical arrangement of the source/object/detector during the
    scan process.
    """

    IntegrationTime: str = ""
    """ Defines the integration time of the pixels. """

    Filter: str = ""
    """ Defines the source side filter used to reduce beam-hardening artifacts. """

    NumberOfProjections: str = ""
    """ Defines the number of projections created while scanning the object. """

    DateTime: str = ""
    """ Defines the date and time at which the scan was performed. """

    User: str = ""
    """ Defines the user who performed the scan. """

    Metadata: Mapping[str, str] = field(default_factory=dict)
