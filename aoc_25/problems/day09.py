"""Day 09 scaffold."""

from __future__ import annotations

from aoc_25.utils import Point


def area(point_one: Point, point_two: Point) -> float:
    return abs(point_one.x - point_two.x + 1) * abs(point_one.y - point_two.y + 1)


class Day09:
    """Placeholder implementation for Day 09."""

    day = 9
    name = "Theater"

    def __init__(self, data: str):
        self.points = [
            Point(int(line.split(",")[0]), int(line.split(",")[1]))
            for line in data.splitlines()
        ]

    def solve_part_one(self) -> str:
        max_area = 0
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                left, right = self.points[i], self.points[j]
                max_area = max(max_area, area(left, right))

        return str(max_area)

    def solve_part_two(self) -> str:
        return ""
