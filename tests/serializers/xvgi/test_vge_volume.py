"""XVGI volume project tests."""

from pathlib import Path

import pytest

from vg_nde_sdk.projects import VolumeProjectDescription
from vg_nde_sdk.sections import (
    ComponentInfoSection,
    ManufacturerInfoSection,
    ScanInfoSection,
    Vectorf,
    VolumeFileSection,
    VolumeMetaInfoContainer,
    VolumeSection,
    VolumeSectionHolder,
)
from vg_nde_sdk.serializers.xvgi import XVGIWriter


@pytest.fixture()
def volume_project_description(tmpdir: Path) -> VolumeProjectDescription:
    project = VolumeProjectDescription(
        volumes=VolumeSectionHolder(
            [
                VolumeSection(
                    VolumeProjections=[
                        VolumeFileSection(
                            FileName=Path("/foo/bar/volume0/projection0.tif"),
                            FilePositionList=Vectorf([1, 2, 3, 4, 5]),
                        ),
                        VolumeFileSection(
                            FileName=Path("/foo/bar/volume0/projection1.tif")
                        ),
                    ],
                    VolumeMetaInfo=VolumeMetaInfoContainer(
                        ComponentInfoSection(
                            CavityNumber="3",
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
                            TubeVoltage="50",
                            TubeCurrent="10",
                            ScanTime="90",
                            ReconstructionTime="10",
                            TotalProcessTime="120",
                            ReconstructionAlgorithm="Some algo",
                            ScanMethod="turntable",
                            Geometry="usual",
                            IntegrationTime="10",
                            Filter="Cu",
                            NumberOfProjections="2",
                            DateTime="yesterday morning",
                            User="John Someuser",
                            Metadata={"someTag": "Tag content"},
                        ),
                    ),
                ),
                VolumeSection(
                    VolumeProjections=[
                        VolumeFileSection(
                            FileName=Path("/foo/bar/volume1/projection0.tif")
                        ),
                        VolumeFileSection(
                            FileName=Path("/foo/bar/volume1/projection1.tif")
                        ),
                    ]
                ),
            ]
        ),
    )

    return project


def test_serialize_volume_project(
    volume_project_description: VolumeProjectDescription, tmpdir: Path
):
    # GIVEN a volume and a serializer
    writer = XVGIWriter()

    # WHEN I serialize the project
    serialized = writer.dumps(volume_project_description)

    # THEN the data has been exported correctly
    assert len(serialized) > 0


def test_serialize_volume_project_to_file(
    volume_project_description: VolumeProjectDescription, tmpdir: Path
):
    # GIVEN a volume and a serializer
    output_dir = Path(tmpdir, "output")
    output_dir.mkdir(parents=True)

    output_file_name = Path(output_dir, "volume.xvgi")
    writer = XVGIWriter()

    # WHEN I serialize the project
    with open(output_file_name, "w+") as output_file:
        writer.dump(volume_project_description, output_file)

    # THEN the data has been exported
    assert output_file_name.exists()
    serialized = output_file_name.read_text()
    assert len(serialized) > 0
