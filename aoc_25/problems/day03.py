from __future__ import annotations

from aoc_25.utils import chunk_by_blank_lines


def find_total_voltage(banks: list[str], battery_size: int) -> int:
    total = 0

    for bank in banks:
        digits = [0 for _ in range(battery_size)]
        max_index = len(bank)
        for i in range(battery_size - 1, -1, -1):
            for idx, battery in enumerate(bank[::-1][i:max_index]):
                value = int(battery)
                if value >= digits[i]:
                    digits[i] = value
                    max_index = i + idx
        total += sum(val * pow(10, i) for i, val in enumerate(digits))
    return total


class Day03:
    day = 3
    name = "Lobby"

    def __init__(self, data: str):
        [self.banks] = chunk_by_blank_lines(data)

    def solve_part_one(self) -> str:
        return str(find_total_voltage(self.banks, 2))

    def solve_part_two(self) -> str:
        return str(find_total_voltage(self.banks, 12))
