from pathlib import Path

from aoc_25.problems.day05 import Day05


def test_day05_part_one_example() -> None:
    data = Path("inputs/day05_example.txt").read_text().strip("\n")
    solver = Day05(data)

    assert solver.solve_part_one() == "3"


def test_day05_part_two_example() -> None:
    data = Path("inputs/day05_example.txt").read_text().strip("\n")
    solver = Day05(data)

    assert solver.solve_part_two() == "14"
