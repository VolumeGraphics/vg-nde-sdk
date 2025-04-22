"""Reconstruction descriptor serializer."""

from dataclasses import dataclass
from typing import Mapping, Sequence, cast

from vg_nde_sdk.sections import (
    ReconstructionProjectionFileSection,
    ReconstructionROISection,
)
from vg_nde_sdk.sections.volume import VolumeMetaInfoContainer

from .base import SectionSerializerBase
from .component_serializer import ComponentInfoSectionSerializer
from .manufacturer_serializer import ManufacturerInfoSectionSerializer
from .reconstruction_roi_serializer import ReconstructionROISerializer
from .scan_serializer import ScanInfoSectionSerializer


@dataclass
class ReconstructionSectionSerializer(SectionSerializerBase):
    """Serializer for reconstruction section."""

    def serialize(
        self,
        section_name: str,
        section_data: Mapping[str, object],
    ) -> str:
        """Serialize the provided section."""
        roi_serializer = ReconstructionROISerializer()

        section_data = dict(section_data)
        rois = cast(
            Sequence[ReconstructionROISection], section_data.pop("AxisAlignedRois")
        )
        projections = cast(
            Sequence[ReconstructionProjectionFileSection],
            section_data.pop("ProjectionFiles"),
        )

        result = super().serialize_with_renaming_meta(
            section_name,
            section_data,
            {},
            {},
        )

        # ROIs
        for i, r in enumerate(rois):
            roi_section_name = f"{section_name}_AxisAlignedRoiListSection_{i}"
            result += roi_serializer.serialize(roi_section_name, vars(r))

        # Projections
        for i, p in enumerate(projections):
            projection_section_name = f"{section_name}_ProjectionFilesSection_{i}"
            result += super().serialize(projection_section_name, vars(p))

        metaData = cast(VolumeMetaInfoContainer, section_data.pop("VolumeMetaInfo"))
        ManufacturerInfoSectionSerializer().serialize(
            f"{section_name}_ManufacturerInfoSection", vars(metaData.ManufacturerInfo)
        )
        ScanInfoSectionSerializer().serialize(
            f"{section_name}_ScanInfoSection", vars(metaData.ScanInfo)
        )
        ComponentInfoSectionSerializer().serialize(
            f"{section_name}_ComponentInfoSection", vars(metaData.ComponentInfo)
        )

        return result
