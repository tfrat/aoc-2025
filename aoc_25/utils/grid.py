"""Helpers for working with 2D grids."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Iterable, Iterator, TypeVar

from aoc_25.utils.geometry import Direction, Point

T = TypeVar("T")


@dataclass(slots=True)
class Grid2D(Generic[T]):
    """Sparse grid backed by a ``dict`` of :class:`Point` -> value."""

    cells: dict[Point, T]
    width: int
    height: int

    def __contains__(self, point: Point) -> bool:
        return point in self.cells

    def __getitem__(self, point: Point) -> T:
        return self.cells[point]

    def neighbors(
        self, point: Point, diagonals: bool = False
    ) -> Iterator[tuple[Point, T]]:
        """Iterate over neighbors optionally including diagonals."""

        directions = Direction.octants() if diagonals else Direction.cardinals()
        for direction in directions:
            neighbor = point.step(direction)
            if neighbor in self.cells:
                yield neighbor, self.cells[neighbor]

    def points(self) -> Iterator[Point]:
        """Iterate over all points in the grid."""

        yield from self.cells.keys()

    def items(self) -> Iterator[tuple[Point, T]]:
        """Iterate ``(Point, value)`` pairs."""

        yield from self.cells.items()


def parse_grid(
    data: Iterable[str] | str,
    *,
    cast: Callable[[str], T] | None = None,
    keep_blank_lines: bool = False,
) -> Grid2D[T | str]:
    """Parse text into a :class:`Grid2D`."""

    if isinstance(data, str):
        lines = data.splitlines()
    else:
        lines = list(data)

    processed = [line.rstrip("\n") for line in lines if keep_blank_lines or line]
    height = len(processed)
    width = max((len(line) for line in processed), default=0)

    cells: dict[Point, T | str] = {}
    for y, line in enumerate(processed):
        for x, char in enumerate(line):
            value: T | str = cast(char) if cast else char
            cells[Point(x, y)] = value

    return Grid2D(cells=cells, width=width, height=height)
