from pathlib import Path

from aoc_25.problems.day02 import Day02


def test_day02_part_one_example() -> None:
    data = Path("inputs/day02_example.txt").read_text().strip("\n")
    solver = Day02(data)

    assert solver.solve_part_one() == "1227775554"


def test_day02_part_two_example() -> None:
    data = Path("inputs/day02_example.txt").read_text().strip("\n")
    solver = Day02(data)

    assert solver.solve_part_two() == "4174379265"
