"""Problem registry for Advent of Code 2025."""

from __future__ import annotations

from typing import Dict

from .base import Problem
from .day01 import Day01
from .day02 import Day02
from .day03 import Day03
from .day04 import Day04
from .day05 import Day05
from .day06 import Day06
from .day07 import Day07
from .day08 import Day08
from .day09 import Day09
from .day10 import Day10
from .day11 import Day11
from .day12 import Day12

PROBLEMS: Dict[int, Problem] = {
    problem.day: problem
    for problem in (
        Day01(),
        Day02(),
        Day03(),
        Day04(),
        Day05(),
        Day06(),
        Day07(),
        Day08(),
        Day09(),
        Day10(),
        Day11(),
        Day12(),
    )
}


def get_problem(day: int) -> Problem:
    """Return the problem for the requested day."""

    try:
        return PROBLEMS[day]
    except KeyError as exc:  # pragma: no cover - defensive guard
        raise ValueError(f"No problem registered for day {day}") from exc


__all__ = ["Problem", "PROBLEMS", "get_problem"]
