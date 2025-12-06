"""Day 06 scaffold."""

from __future__ import annotations

from aoc_25.utils import parse_ints


class Day06:
    """Placeholder implementation for Day 06."""

    day = 6
    name = "Day 06 Placeholder"

    def solve_part_one(self, data: str) -> str:
        lines = data.splitlines()
        operators = lines[-1].split()
        results = parse_ints(lines[0])
        for line in lines[1:-1]:
            values = parse_ints(line)
            for i, value in enumerate(values):
                if operators[i] == "+":
                    results[i] += value
                else:
                    results[i] *= value
        return str(sum(results))

    def solve_part_two(self, data: str) -> str:
        return (
            f"Day 06 part 2 not implemented (received {len(data.splitlines())} lines)"
        )
