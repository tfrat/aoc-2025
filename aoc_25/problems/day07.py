"""Day 07 scaffold."""

from __future__ import annotations

from aoc_25.utils import parse_grid, Point


class Day07:
    """Placeholder implementation for Day 07."""

    day = 7
    name = "Day 07 Placeholder"

    def __init__(self, data: str):
        self.grid = parse_grid(data, start_value="S")
        self.splitter = "^"

    def solve_part_one(self) -> str:
        count = 0
        beams = {self.grid.start.x}
        new_beams = set()
        remove_beams = set()
        for y in range(1, self.grid.height):
            for x in beams:
                if self.grid.get(Point(x, y)) == self.splitter:
                    count += 1
                    remove_beams.add(x)
                    new_beams |= {x - 1, x + 1}
            beams |= new_beams
            beams -= remove_beams
            new_beams.clear()
            remove_beams.clear()

        return str(count)

    def solve_part_two(self) -> str:
        return ""
