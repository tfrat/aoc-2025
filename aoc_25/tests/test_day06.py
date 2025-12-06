from pathlib import Path

from aoc_25.problems.day06 import Day06


def test_day06_part_one_example() -> None:
    data = Path("inputs/day06_example.txt").read_text().strip("\n")
    solver = Day06(data)

    assert solver.solve_part_one() == "4277556"


def test_day06_part_two_example() -> None:
    data = Path("inputs/day06_example.txt").read_text().strip("\n")
    solver = Day06(data)

    assert solver.solve_part_two() == "3263827"
