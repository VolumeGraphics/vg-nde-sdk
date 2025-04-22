"""Tests for primitive types."""

import copy

import pytest

import vg_nde_sdk as sdk


@pytest.mark.parametrize(
    "t",
    [
        sdk.Vectorf([1, 2, 3, 4]),
        sdk.Vector3f(1, 2, 3),
        sdk.Vector3i(1, 2, 3),
        sdk.Vector2f(1, 2),
        sdk.Vector2i(1, 2),
    ],
)
def test_copy(t: object):
    # GIVEN an object
    # WHEN I copy it
    c = copy.copy(t)

    # THEN I expect the objects to be distinct but contain the same data
    assert c is not t
    assert c == t


@pytest.mark.parametrize(
    "t",
    [
        sdk.Vectorf([1, 2, 3, 4]),
        sdk.Vector3f(1, 2, 3),
        sdk.Vector3i(1, 2, 3),
        sdk.Vector2f(1, 2),
        sdk.Vector2i(1, 2),
    ],
)
def test_deepcopy(t: object):
    # GIVEN an object
    # WHEN I deepcopy it
    c = copy.deepcopy(t)

    # THEN I expect the objects to be distinct but contain the same data
    assert c is not t
    assert c == t
