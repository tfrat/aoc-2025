from pathlib import Path

from aoc_25.problems.day11 import Day11


def test_day11_part_one_example() -> None:
    data = Path("inputs/day11_example.txt").read_text().strip("\n")
    solver = Day11(data)

    assert solver.solve_part_one() == ""


def test_day11_part_two_example() -> None:
    data = Path("inputs/day11_example.txt").read_text().strip("\n")
    solver = Day11(data)

    assert solver.solve_part_two() == ""
