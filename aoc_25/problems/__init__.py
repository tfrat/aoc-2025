"""Problem registry for Advent of Code 2025."""

from __future__ import annotations

from aoc_25.problems.base import Problem
from aoc_25.problems.day01 import Day01
from aoc_25.problems.day02 import Day02
from aoc_25.problems.day03 import Day03
from aoc_25.problems.day04 import Day04
from aoc_25.problems.day05 import Day05
from aoc_25.problems.day06 import Day06
from aoc_25.problems.day07 import Day07
from aoc_25.problems.day08 import Day08
from aoc_25.problems.day09 import Day09
from aoc_25.problems.day10 import Day10
from aoc_25.problems.day11 import Day11
from aoc_25.problems.day12 import Day12

PROBLEM_CLASSES: dict[int, type[Problem]] = {
    problem.day: problem
    for problem in (
        Day01,
        Day02,
        Day03,
        Day04,
        Day05,
        Day06,
        Day07,
        Day08,
        Day09,
        Day10,
        Day11,
        Day12,
    )
}


def get_problem(day: int, data: str) -> Problem:
    """Instantiate and return the problem for the requested day."""

    try:
        problem_cls = PROBLEM_CLASSES[day]
    except KeyError as exc:  # pragma: no cover - defensive guard
        raise ValueError(f"No problem registered for day {day}") from exc

    return problem_cls(data)


__all__ = ["Problem", "PROBLEM_CLASSES", "get_problem"]
