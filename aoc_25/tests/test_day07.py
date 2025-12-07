from pathlib import Path

import pytest

from aoc_25.problems.day07 import Day07


def test_day07_part_one_example() -> None:
    data = Path("inputs/day07_example.txt").read_text().strip("\n")
    solver = Day07(data)

    pytest.xfail("Day 07 not implemented yet")
    assert solver.solve_part_one() == ""


def test_day07_part_two_example() -> None:
    data = Path("inputs/day07_example.txt").read_text().strip("\n")
    solver = Day07(data)

    pytest.xfail("Day 07 not implemented yet")
    assert solver.solve_part_two() == ""
