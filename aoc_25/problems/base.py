"""Shared interfaces for AoC 2025 problems."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Problem(Protocol):
    """Common interface every day must implement."""

    day: int
    name: str

    def solve_part_one(self, data: str) -> str: ...

    def solve_part_two(self, data: str) -> str: ...


@dataclass(slots=True)
class ProblemResult:
    """Container for both parts of a problem execution."""

    part_one: str
    part_two: str
