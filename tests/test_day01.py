from pathlib import Path

from aoc_25.problems.day01 import Day01


def test_day01_part_one_example() -> None:
    data = Path("inputs/day01_example.txt").read_text().strip("\n")
    solver = Day01(data)

    assert solver.solve_part_one() == "3"


def test_day01_part_two_example() -> None:
    data = Path("inputs/day01_example.txt").read_text().strip("\n")
    solver = Day01(data)

    assert solver.solve_part_two() == "6"
