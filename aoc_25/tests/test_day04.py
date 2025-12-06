from pathlib import Path

from aoc_25.problems.day04 import Day04


def test_day04_part_one_example() -> None:
    data = Path("inputs/day04_example.txt").read_text().strip("\n")
    solver = Day04(data)

    assert solver.solve_part_one() == "13"


def test_day04_part_two_example() -> None:
    data = Path("inputs/day04_example.txt").read_text().strip("\n")
    solver = Day04(data)

    assert solver.solve_part_two() == "43"
