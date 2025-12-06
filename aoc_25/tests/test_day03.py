from pathlib import Path

from aoc_25.problems.day03 import Day03


def test_day03_part_one_example() -> None:
    data = Path("inputs/day03_example.txt").read_text().strip("\n")
    solver = Day03(data)

    assert solver.solve_part_one() == "357"


def test_day03_part_two_example() -> None:
    data = Path("inputs/day03_example.txt").read_text().strip("\n")
    solver = Day03(data)

    assert solver.solve_part_two() == "3121910778619"
