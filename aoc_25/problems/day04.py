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


def find_removable(grid: Grid2D[str], point: Point, removed: set[Point]) -> set[Point]:
    removable = set()
    if can_be_accessed(grid, point, removed):
        removable.add(point)
    return removable


class Day04:
    day = 4
    name = "Printing Department"

    def __init__(self, data: str):
        self.grid = parse_grid(data)

    def solve_part_one(self) -> str:
        removed = set()
        for point in self.grid.points():
            removed |= find_removable(self.grid, point, set())
        return str(len(removed))

    def solve_part_two(self) -> str:
        removed = set()
        prev_removed = None
        while removed != prev_removed:
            prev_removed = removed.copy()
            for point in self.grid.points():
                removed |= find_removable(self.grid, point, removed)

        return str(len(removed))
