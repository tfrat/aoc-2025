"""Shared interfaces for AoC 2025 problems."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Problem(Protocol):
    """Common interface every day must implement."""

    day: int
    name: str

    def __init__(self, data: str): ...

    def solve_part_one(self) -> str: ...

    def solve_part_two(self) -> str: ...


@dataclass(slots=True)
class ProblemResult:
    """Container for both parts of a problem execution."""

    part_one: str
    part_two: str
    part_one_time: float
    part_two_time: float
