"""Practice problem registry."""

from __future__ import annotations

from aoc_25.practice.base import PracticeProblem
from aoc_25.practice.problem01 import Practice01

PRACTICE_PROBLEM_CLASSES: dict[str, type[PracticeProblem]] = {
    problem.slug: problem for problem in (Practice01,)
}


def get_practice_problem(slug: str, data: str) -> PracticeProblem:
    """Instantiate and return the requested practice problem."""

    try:
        problem_cls = PRACTICE_PROBLEM_CLASSES[slug]
    except KeyError as exc:  # pragma: no cover - defensive guard
        raise ValueError(f"No practice problem registered for slug {slug!r}") from exc

    return problem_cls(data)


__all__ = ["PracticeProblem", "PRACTICE_PROBLEM_CLASSES", "get_practice_problem"]
