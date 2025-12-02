"""Day 01 scaffold."""

from __future__ import annotations

from aoc_25.utils import chunk_by_blank_lines


def count_zeros(rotations: list[tuple[str, int]], count_passes: bool = False) -> int:
    number = 50
    counter = 0
    for rotation, clicks in rotations:
        prev = number
        number = number - clicks if rotation == "L" else number + clicks

        if number in {0, 100}:
            counter += 1
        elif count_passes:
            counter += (abs(number) + 100) // 100 if number < 0 else number // 100
            if prev == 0 and number < 0:
                counter -= 1

        number = number % 100

    return counter


class Day01:
    day = 1
    name = "Day 01 - Password"

    def solve_part_one(self, data: str) -> str:
        rotations_raw = chunk_by_blank_lines(data)
        rotations = [
            (rotation_raw[0], int(rotation_raw[1:]))
            for rotation_raw in rotations_raw[0]
        ]

        return str(count_zeros(rotations, False))

    def solve_part_two(self, data: str) -> str:
        rotations_raw = chunk_by_blank_lines(data)
        rotations = [
            (rotation_raw[0], int(rotation_raw[1:]))
            for rotation_raw in rotations_raw[0]
        ]

        return str(count_zeros(rotations, True))
