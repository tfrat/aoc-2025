"""Day 04 scaffold."""

from __future__ import annotations

from aoc_25.utils import parse_grid, Grid2D, Point


def can_be_accessed(grid: Grid2D[str], point: Point, removed: set[Point]) -> bool:
    if grid.get(point, ".") == "." or point in removed:
        return False
    neighbors = point.neighbors8()
    blocked = sum(
        1
        for neighbor in neighbors
        if grid.get(neighbor, ".") == "@" and neighbor not in removed
    )
    return blocked < 4


def find_removable(
    grid: Grid2D[str], point: Point, removed: set[Point] | None
) -> set[Point]:
    new_removed = set()
    if can_be_accessed(grid, point, removed if removed is not None else set()):
        new_removed.add(point)
        if removed is not None:
            for neighbor, _ in grid.neighbors(point, diagonals=True):
                new_removed |= find_removable(grid, neighbor, removed | new_removed)
    return new_removed


class Day04:
    day = 4
    name = "Day 04 Printing Department"

    def solve_part_one(self, data: str) -> str:
        grid = parse_grid(data)
        removed = set()
        for point in grid.points():
            removed |= find_removable(grid, point, None)
        return str(len(removed))

    def solve_part_two(self, data: str) -> str:
        grid = parse_grid(data)
        removed = set()
        for point in grid.points():
            removed |= find_removable(grid, point, removed)

        return str(len(removed))
