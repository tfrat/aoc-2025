from pathlib import Path

from aoc_25.problems.day08 import Day08


def test_day08_part_one_example() -> None:
    data = Path("inputs/day08_example.txt").read_text().strip("\n")
    solver = Day08(data)

    assert solver.solve_part_one() == ""


def test_day08_part_two_example() -> None:
    data = Path("inputs/day08_example.txt").read_text().strip("\n")
    solver = Day08(data)

    assert solver.solve_part_two() == ""
