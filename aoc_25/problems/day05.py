from __future__ import annotations

from aoc_25.utils import chunk_by_blank_lines


def sorted_merge(one: tuple[int, int], two: tuple[int, int]) -> tuple[int, int] | None:
    """Assumes that the first tuple precedes the second tuple."""
    if two[0] <= one[1]:
        return one[0], max(one[1], two[1])
    return None


class Day05:
    day = 5
    name = "Cafeteria"

    def __init__(self, data: str):
        ranges_raw, inventory = chunk_by_blank_lines(data)
        self.ranges = [
            (int(range_raw.split("-")[0]), int(range_raw.split("-")[1]))
            for range_raw in ranges_raw
        ]
        self.inventory = inventory

    def solve_part_one(self) -> str:
        fresh = set()
        for item in self.inventory:
            for range_ in self.ranges:
                if range_[0] <= int(item) <= range_[1]:
                    fresh.add(item)
        return str(len(fresh))

    def solve_part_two(self) -> str:
        product_ranges = sorted(self.ranges, key=lambda x: x[0])

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
