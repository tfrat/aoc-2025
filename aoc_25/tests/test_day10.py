from pathlib import Path

import pytest

from aoc_25.problems.day10 import Day10


def test_day10_part_one_example() -> None:
    data = Path("inputs/day10_example.txt").read_text().strip("\n")
    solver = Day10(data)

    pytest.xfail("Day 10 not implemented yet")
    assert solver.solve_part_one() == ""


def test_day10_part_two_example() -> None:
    data = Path("inputs/day10_example.txt").read_text().strip("\n")
    solver = Day10(data)

    pytest.xfail("Day 10 not implemented yet")
    assert solver.solve_part_two() == ""
