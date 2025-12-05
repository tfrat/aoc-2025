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
        product_strings, _ = chunk_by_blank_lines(data)
        product_ranges = sorted(
            [
                (left, right)
                for s in product_strings
                for left, right in [tuple(map(int, s.split("-", 1)))]
            ],
            key=lambda x: x[0],
        )

        current_range = product_ranges[0]
        total = 0
        for product_range in product_ranges[1:]:
            merged = sorted_merge(current_range, product_range)
            if merged is None:
                total += current_range[1] - current_range[0] + 1
                current_range = product_range
            else:
                current_range = merged
        total += current_range[1] - current_range[0] + 1

        return str(total)
