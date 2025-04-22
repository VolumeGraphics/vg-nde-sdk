"""Common types.

We subclass the tuple in order to be able to both enforce strong types
and to typecheck at runtime because different types serialize
differently (number formatting, etc.).

"""

import copy
from typing import Any, Dict, Optional, Sequence


class Vectorf(tuple):
    """Float vector."""

    def __new__(cls, arg: Sequence[float] = ()):  # noqa ANN102
        """Construct from sequence."""
        return tuple.__new__(cls, arg)

    def __copy__(self):
        """Copy implementation."""
        return Vectorf([*self])

    def __deepcopy__(self, memo: Optional[Dict[int, Any]]):
        """Deep copy implementation."""
        return Vectorf(tuple((copy.deepcopy(x, memo) for x in self)))


class Vector3f(tuple):
    """3D float vector."""

    def __new__(cls, x: float, y: float, z: float):
        """Constructor."""
        return tuple.__new__(cls, (x, y, z))

    def __copy__(self):
        """Copy implementation."""
        return Vector3f(*self)

    def __deepcopy__(self, memo: Optional[Dict[int, Any]]):
        """Deep copy implementation."""
        return Vector3f(*(copy.deepcopy(x, memo) for x in self))


class Vector2f(tuple):
    """2D float vector."""

    def __new__(cls, x: float, y: float):
        """Constructor."""
        return tuple.__new__(cls, (x, y))

    def __copy__(self):
        """Copy implementation."""
        return Vector2f(*self)

    def __deepcopy__(self, memo: Optional[Dict[int, Any]]):
        """Deep copy implementation."""
        return Vector2f(*(copy.deepcopy(x, memo) for x in self))


class Vector3i(tuple):
    """3D int vector."""

    def __new__(cls, x: int, y: int, z: int):
        """Constructor."""
        return tuple.__new__(cls, (x, y, z))

    def __copy__(self):
        """Copy implementation."""
        return Vector3i(*self)

    def __deepcopy__(self, memo: Optional[Dict[int, Any]]):
        """Deep copy implementation."""
        return Vector3i(*(copy.deepcopy(x, memo) for x in self))


class Vector2i(tuple):
    """2D int vector."""

    def __new__(cls, x: int, y: int):
        """Constructor."""
        return tuple.__new__(cls, (x, y))

    def __copy__(self):
        """Copy implementation."""
        return Vector2i(*self)

    def __deepcopy__(self, memo: Optional[Dict[int, Any]]):
        """Deep copy implementation."""
        return Vector2i(*(copy.deepcopy(x, memo) for x in self))
