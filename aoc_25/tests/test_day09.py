from pathlib import Path

import pytest

from aoc_25.problems.day09 import Day09


def test_day09_part_one_example() -> None:
    data = Path("inputs/day09_example.txt").read_text().strip("\n")
    solver = Day09(data)

    pytest.xfail("Day 09 not implemented yet")
    assert solver.solve_part_one() == ""


def test_day09_part_two_example() -> None:
    data = Path("inputs/day09_example.txt").read_text().strip("\n")
    solver = Day09(data)

    pytest.xfail("Day 09 not implemented yet")
    assert solver.solve_part_two() == ""
