from pathlib import Path

from aoc_25.problems.day12 import Day12


def test_day12_part_one_example() -> None:
    data = Path("inputs/day12_example.txt").read_text().strip("\n")
    solver = Day12(data)

    assert solver.solve_part_one() == ""


def test_day12_part_two_example() -> None:
    data = Path("inputs/day12_example.txt").read_text().strip("\n")
    solver = Day12(data)

    assert solver.solve_part_two() == ""
