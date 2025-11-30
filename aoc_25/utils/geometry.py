"""Basic coordinate and direction primitives."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


@dataclass(frozen=True, slots=True)
class Point:
    """2D integer coordinate used for AoC grid problems."""

    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def step(self, direction: Direction) -> Point:
        """Move one unit in ``direction``."""

        dx, dy = direction.delta
        return Point(self.x + dx, self.y + dy)

    def neighbors4(self) -> Tuple[Point, Point, Point, Point]:
        """Return orthogonal neighbors."""

        north, east, south, west = Direction.cardinals()
        return (
            self.step(north),
            self.step(east),
            self.step(south),
            self.step(west),
        )

    def neighbors8(self) -> Tuple[Point, ...]:
        """Return orthogonal + diagonal neighbors."""

        return tuple(self.step(direction) for direction in Direction.octants())

    def manhattan(self, other: Point) -> int:
        """Taxicab distance to ``other``."""

        return abs(self.x - other.x) + abs(self.y - other.y)


class Direction(Enum):
    """Compass directions with associated deltas."""

    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    NORTH_EAST = (1, -1)
    SOUTH_EAST = (1, 1)
    SOUTH_WEST = (-1, 1)
    NORTH_WEST = (-1, -1)

    @property
    def delta(self) -> tuple[int, int]:
        return self.value

    def turn_left(self) -> Direction:
        """Rotate 90° left (only valid for cardinal directions)."""

        mapping = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }
        return mapping[self]

    def turn_right(self) -> Direction:
        """Rotate 90° right (only valid for cardinal directions)."""

        mapping = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }
        return mapping[self]

    @classmethod
    def cardinals(cls) -> Tuple[Direction, Direction, Direction, Direction]:
        """Return N/E/S/W directions."""

        return cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST

    @classmethod
    def diagonals(cls) -> Tuple[Direction, Direction, Direction, Direction]:
        """Return diagonal directions."""

        return cls.NORTH_EAST, cls.SOUTH_EAST, cls.SOUTH_WEST, cls.NORTH_WEST

    @classmethod
    def octants(cls) -> Tuple[Direction, ...]:
        """Return all eight directions."""

        return cls.cardinals() + cls.diagonals()
