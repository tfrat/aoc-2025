"""Starter practice problem template."""

from __future__ import annotations


class Practice01:
    """Placeholder practice problem for experimentation."""

    slug = "practice01"
    title = "Practice Placeholder"

    def __init__(self, data: str):
        self.lines = data.splitlines()

    def solve_part_one(self) -> str:
        return str(len(self.lines))

    def solve_part_two(self) -> str:
        return str(sum(len(line) for line in self.lines))
