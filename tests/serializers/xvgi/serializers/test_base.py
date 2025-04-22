"""Project section tests."""

import os
from configparser import ConfigParser
from os import PathLike
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Mapping, Union

import pytest

from vg_nde_sdk import Vector2f, Vector2i, Vector3f, Vector3i, Vectorf
from vg_nde_sdk.sections.reconstruction_enums import ReconstructionGeometricSetup
from vg_nde_sdk.serializers.xvgi import SectionSerializerBase

escape_map = [
    (";", "\\;"),
    ("[", "\\["),
    ("]", "\\]"),
    ("=", "\\="),
    ("\r", "\\r"),
    ("\n", "\\n"),
    (" ", "\\ "),
    ("_", "\\_"),
    ("\\", "\\\\"),
]


@pytest.mark.parametrize(
    "bad_str, expected",
    (
        (f"section{bad_char}name", f"[section{escaped_bad_char}name]")
        for bad_char, escaped_bad_char in escape_map
    ),
)
def test_section_name_escaping(bad_str: str, expected: str) -> None:
    # GIVEN a data to be serialized & serializer
    serializer = SectionSerializerBase()

    section_name = f"{bad_str}"
    data: Mapping[str, object] = {}

    # WHEN I serialize it
    serialized = serializer.serialize(section_name, data)

    # THEN the section name has been correctly escaped
    # Hack required, ConfigParser will not parse keys with backslashes
    lines = serialized.split("\n")
    assert lines[0].strip() == expected


@pytest.mark.parametrize(
    "bad_str, expected",
    (
        (f"key{bad_char}name", f"key{escaped_bad_char}name")
        for bad_char, escaped_bad_char in escape_map
    ),
)
def test_key_name_escaping(bad_str: str, expected: str) -> None:
    # GIVEN a data to be serialized & serializer
    serializer = SectionSerializerBase()

    section_name = "test"
    data: Mapping[str, object] = {bad_str: "aaa"}

    # WHEN I serialize it
    serialized = serializer.serialize(section_name, data)

    # THEN the key name has been correctly escaped
    # Hack required, ConfigParser will not parse keys with backslashes
    lines = serialized.split("\n")
    k, v = lines[1].split(" = ")
    assert k.strip() == expected


def test_none_serialization() -> None:
    # GIVEN a data to be serialized & serializer
    serializer = SectionSerializerBase()

    section_name = "test"
    key = "key"
    data: Mapping[str, object] = {key: None}

    # WHEN I serialize it
    serialized = serializer.serialize(section_name, data)

    # THEN the None value has been turned into empty string
    parser = ConfigParser()
    parser.read_string(serialized)

    assert parser[section_name][key] == ""


@pytest.mark.parametrize(
    "path, expected",
    [
        (PureWindowsPath("C:\\foo\\bar\\baz"), "C:/foo/bar/baz"),
        (PureWindowsPath("bar\\baz"), "bar/baz"),
        (PurePosixPath("/c/foo/bar/baz"), "/c/foo/bar/baz"),
        (PurePosixPath("bar/baz"), "bar/baz"),
        (
            (Path("/c/foo/bar/baz"), "/c/foo/bar/baz")
            if os.name == "posix"
            else (Path("C:/foo/bar/baz"), "C:/foo/bar/baz")
        ),
        (
            (Path("/mnt/test"), "/mnt/test")
            if os.name == "posix"
            else (Path("\\\\mnt\\test\\"), "//mnt/test/")
        ),
    ],
)
def test_path_serialization(path: PathLike, expected: str) -> None:
    # GIVEN a data to be serialized & serializer
    serializer = SectionSerializerBase()

    section_name = "test"
    key = "key"
    data: Mapping[str, object] = {key: path}

    # WHEN I serialize it
    serialized = serializer.serialize(section_name, data)

    # THEN the path value has been turned into a posix path string
    parser = ConfigParser()
    parser.read_string(serialized)

    assert parser[section_name][key] == expected


def test_enum_serialization() -> None:
    # GIVEN a data to be serialized & serializer
    serializer = SectionSerializerBase()

    section_name = "test"
    key = "key"
    data: Mapping[str, object] = {key: ReconstructionGeometricSetup.RotateFrustum}

    # WHEN I serialize it
    serialized = serializer.serialize(section_name, data)

    # THEN the enum value has been turned into a string representation
    parser = ConfigParser()
    parser.read_string(serialized)

    assert parser[section_name][key] == "ReconstructionGeometricSetup_RotateFrustum"


@pytest.mark.parametrize(
    "vector, expected",
    [
        (Vector3f(1, 2, 3), "1.0000000  2.0000000  3.0000000"),
        (Vector2f(1, 2), "1.0000000  2.0000000"),
        (Vectorf([1, 2, 3, 4]), "1.0000000  2.0000000  3.0000000  4.0000000"),
        (Vector3i(1, 2, 3), "1  2  3"),
        (Vector2i(1, 2), "1  2"),
    ],
)
def test_vector_serialization(
    vector: Union[Vectorf, Vector2f, Vector3f, Vector2i, Vector3i], expected: str
) -> None:
    # GIVEN a data to be serialized & serializer
    serializer = SectionSerializerBase()

    section_name = "test"
    key = "key"
    data: Mapping[str, object] = {key: vector}

    # WHEN I serialize it
    serialized = serializer.serialize(section_name, data)

    # THEN the vector value has been turned into a string representation
    parser = ConfigParser()
    parser.read_string(serialized)

    assert parser[section_name][key] == expected


def test_renaming() -> None:
    # GIVEN a data to be serialized & serializer & field renaming table
    serializer = SectionSerializerBase()

    section_name = "test"
    key_renaming = {"original": "renamed", "original2": "renamed2"}
    data: Mapping[str, object] = {
        "original3": "data3",
        "original": "data",
        "original2": "data2",
    }

    # WHEN I serialize it
    serialized = serializer.serialize_with_renaming_meta(
        section_name, data, key_renaming, {}
    )

    # THEN the data have been serialized with renamed keys
    parser = ConfigParser()
    parser.read_string(serialized)

    expected_keys = [("renamed", "data"), ("renamed2", "data2"), ("original3", "data3")]
    for k, v in expected_keys:
        assert parser[section_name][k] == v


def test_metadata() -> None:
    # GIVEN a data to be serialized & serializer & metadata table
    serializer = SectionSerializerBase()

    section_name = "test"
    data: Mapping[str, object] = {}
    metadata = {"tag1": "val1", "tag2": "val2"}

    # WHEN I serialize it
    serialized = serializer.serialize_with_renaming_meta(
        section_name, data, {}, metadata
    )

    # THEN the metadata have been appended
    parser = ConfigParser()
    parser.read_string(serialized)

    for k, v in metadata.items():
        assert parser[section_name][k] == v
