from __future__ import annotations

from collections.abc import Callable


def sum_invalid_products(
    ranges: list[tuple[int, int]], detector: Callable[int, bool]
) -> int:
    total = 0
    for left, right in ranges:
        while left <= right:
            if detector(left):
                total += left
            left += 1
    return total


def has_repeating_pattern(n: int) -> bool:
    n_str = str(n)
    half = len(n_str) // 2
    return n_str[:half] == n_str[half:]


def has_variable_repeating_pattern(n: int) -> bool:
    str_n = str(n)
    split_len = 1
    while split_len < len(str_n):
        # Skip if the split isn't a divisor as it can't have a complete repeating pattern
        if len(str_n) % split_len != 0:
            split_len += 1
            continue
        offset = 0
        splits = set()
        while offset < len(str_n):
            section = str_n[offset : offset + split_len]
            splits.add(section)
            offset += split_len
            # Bail early if one of the segments doesn't match
            if len(splits) > 1:
                break
        if len(splits) == 1:
            return True
        split_len += 1
    return False


class Day02:
    day = 2
    name = "Gift Shop"

    def __init__(self, data: str):
        self.ranges = [
            (int(left), int(right))
            for range_raw in data.split(",")
            for left, right in [range_raw.split("-")]
        ]

    def solve_part_one(self) -> str:
        return str(sum_invalid_products(self.ranges, has_repeating_pattern))

    def solve_part_two(self) -> str:
        return str(sum_invalid_products(self.ranges, has_variable_repeating_pattern))
