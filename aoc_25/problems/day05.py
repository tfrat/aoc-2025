"""Day 05 scaffold."""

from __future__ import annotations

from aoc_25.utils import chunk_by_blank_lines


def sorted_merge(one: tuple[int, int], two: tuple[int, int]) -> tuple[int, int] | None:
    """Assumes that the first tuple precedes the second tuple."""
    if two[0] <= one[1]:
        return one[0], max(one[1], two[1])
    return None


class Day05:
    """Placeholder implementation for Day 05."""

    day = 5
    name = "Cafeteria"

    def solve_part_one(self, data: str) -> str:
        ranges_raw, inventory = chunk_by_blank_lines(data)
        ranges = [
            (int(range_raw.split("-")[0]), int(range_raw.split("-")[1]))
            for range_raw in ranges_raw
        ]
        fresh = set()
        for item in inventory:
            for range_ in ranges:
                if range_[0] <= int(item) <= range_[1]:
                    fresh.add(item)
        return str(len(fresh))

    def solve_part_two(self, data: str) -> str:
        ranges_raw, _ = chunk_by_blank_lines(data)
        ranges = [
            (int(range_raw.split("-")[0]), int(range_raw.split("-")[1]))
            for range_raw in ranges_raw
        ]
        ranges = sorted(ranges, key=lambda x: x[0])
        current = ranges[0]
        total = 0
        for range_ in ranges[1:]:
            merged = sorted_merge(current, range_)
            if merged is None:
                total += current[1] - current[0] + 1
                current = range_
            else:
                current = merged
        total += current[1] - current[0] + 1
        return str(total)
