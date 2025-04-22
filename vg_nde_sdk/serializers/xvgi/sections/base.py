"""Base section serializer."""

from dataclasses import dataclass
from enum import Enum
from os import PathLike
from pathlib import PurePath, PureWindowsPath
from typing import Mapping, Optional

from vg_nde_sdk.sections import Vector2f, Vector2i, Vector3f, Vector3i, Vectorf
from vg_nde_sdk.serializers import AbstractSectionSerializer


def _escape_key(s: str) -> str:
    """Mapping used to escape characters in keys."""
    escape_map = {
        ";": "\\;",
        "[": "\\[",
        "]": "\\]",
        "=": "\\=",
        "\r": "\\r",
        "\n": "\\n",
        " ": "\\ ",
        "_": "\\_",
        "\\": "\\\\",
    }
    return s.translate(str.maketrans(escape_map))  # type: ignore


def _map_infinite_float(nr: float) -> float:
    if nr == float("inf"):
        return 3.402823e38
    if nr == float("-inf"):
        return 1.175494e-38
    return nr


@dataclass
class SectionSerializerBase(AbstractSectionSerializer):
    """Base section serializer."""

    def serialize(
        self,
        name: str,
        data: Mapping[str, object],
    ) -> str:
        """Serialize section."""
        return self.serialize_with_renaming_meta(name, data)

    def serialize_with_renaming_meta(
        self,
        name: str,
        data: Mapping[str, object],
        attr_renaming: Optional[Mapping[str, str]] = None,
        metadata: Optional[Mapping[str, str]] = None,
    ) -> str:
        """Serialize section."""
        attr_renaming = attr_renaming or {}
        metadata = metadata or {}

        # write the section out
        result = f"[{_escape_key(name)}]\n"
        for k, v in data.items():
            # process the key
            escaped_key = _escape_key(attr_renaming.get(k, k))

            # process the value
            if v is None:
                v = ""

            elif isinstance(v, PureWindowsPath):
                v = v.as_posix()

            elif isinstance(v, PathLike):
                v = PurePath(v).as_posix()

            elif isinstance(v, Enum):
                v = str(v).replace(".", "_")

            elif (
                isinstance(v, Vector3f)
                or isinstance(v, Vector2f)
                or isinstance(v, Vectorf)
            ):
                v = "  ".join(f"{_map_infinite_float(f):.7f}" for f in v)

            elif isinstance(v, Vector3i) or isinstance(v, Vector2i):
                v = "  ".join(f"{i}" for i in v)

            result += f"\t{escaped_key} = {v}\n"

        # append metadata
        for tag, desc in metadata.items():
            result += f"\t{_escape_key(tag)} = {desc}\n"

        result += "\n"

        return result
