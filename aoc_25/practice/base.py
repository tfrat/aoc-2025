"""Shared interfaces for practice problems."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class PracticeProblem(Protocol):
    """Common interface every practice problem must implement."""

    slug: str
    title: str

    def __init__(self, data: str): ...

    def solve_part_one(self) -> str: ...

    def solve_part_two(self) -> str: ...


@dataclass(slots=True)
class PracticeResult:
    """Container for both parts of a practice problem execution."""

    part_one: str
    part_two: str
