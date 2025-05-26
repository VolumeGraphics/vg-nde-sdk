"""Volume project generation."""

import os
import shutil
from pathlib import Path

from vg_nde_sdk.projects import ProjectDescription
from vg_nde_sdk.sections import (
    ComponentInfoSection,
    ManufacturerInfoSection,
    ScanInfoSection,
    Vector3f,
    Vector3i,
    VolumeDataType,
    VolumeEndian,
    VolumeFileFormat,
    VolumeFileSection,
    VolumeMetaInfoContainer,
    VolumeSection,
    VolumeSectionHolder,
)
from vg_nde_sdk.serializers import xvgi

THIS_DIR = Path(__file__).parent


def main():
    """Generate a volume import project in the current directory."""
    targetXVGIFilepath = THIS_DIR / "manual_setup.xvgi"
    targetVGDataFolderPath = THIS_DIR / "[vg-data] manual_setup"

    targetVGDataFolderPath.mkdir(exist_ok=True)

    volumeFilePath = targetVGDataFolderPath / "engine.gz"
    shutil.copy(
        os.path.dirname(os.path.abspath(__file__)) + "\\..\\volumes\\data\\engine.gz",
        volumeFilePath,
    )

    block_section = VolumeFileSection(
        FileName=volumeFilePath,
        FileFileFormat=VolumeFileFormat.Gzip,
        FileEndian=VolumeEndian.Little,
        FileSize=Vector3i(256, 256, 110),
        FileDataType=VolumeDataType.UInt8,
    )

    meta_infos = VolumeMetaInfoContainer(
        ComponentInfoSection(
            CavityNumber="",
            Description="Engine",
            LotNumber="",
            ProductionDateTime="06.12.2018 20:01:02",
            SerialNumber="1234",
            Metadata={"myNewTag": "My new tag description"},
        ),
        ManufacturerInfoSection(
            Name="My company", Metadata={"someTag": "Some tag content"}
        ),
        ScanInfoSection(
            ScanTime="90",
            ReconstructionTime="10",
            TotalProcessTime="120",
            Geometry="usual",
            IntegrationTime="10",
            Metadata={"someTag": "Tag content"},
        ),
    )

    project = ProjectDescription(
        volumes=VolumeSectionHolder(
            [
                VolumeSection(
                    VolumeDestinationDataType=VolumeDataType.UInt8,
                    VolumeResolution=Vector3f(1, 1, 1),
                    VolumeProjections=[block_section],
                    VolumeMetaInfo=meta_infos,
                )
            ]
        ),
    )

    writer = xvgi.XVGIWriter()
    with open(targetXVGIFilepath, "wt+", encoding="utf-8") as output:
        writer.dump(project, output)
    print(f"Successfully wrote {targetXVGIFilepath}")


if __name__ == "__main__":
    main()
