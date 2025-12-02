"""Command-line runner for Advent of Code 2025 problems."""

from __future__ import annotations

from enum import StrEnum
from pathlib import Path
from typing import Annotated

import typer

from aoc_25.problems import get_problem
from aoc_25.problems.base import Problem, ProblemResult

app = typer.Typer(help="Run Advent of Code 2025 solutions.")


class Dataset(StrEnum):
    EXAMPLE = "example"
    ACTUAL = "actual"


def _read_input(day: int, dataset: Dataset, override: Path | None) -> str:
    """Read the requested dataset for a problem, optionally using an override."""

    if override is not None:
        path = override
    else:
        path = Path("inputs") / f"day{day:02d}_{dataset.value}.txt"

    if not path.exists():
        raise typer.BadParameter(f"Input file not found: {path}")

    return path.read_text().rstrip("\n")


def _execute(problem: Problem, data: str) -> ProblemResult:
    """Execute both parts of a problem and return structured results."""

    part_one = problem.solve_part_one(data)
    part_two = problem.solve_part_two(data)
    return ProblemResult(part_one=part_one, part_two=part_two)


@app.command("run")
def run_problem(
    day: Annotated[int, typer.Argument(min=1, max=12, help="Problem day to execute.")],
    dataset: Annotated[
        Dataset,
        typer.Option(
            "--dataset",
            "-d",
            case_sensitive=False,
            help="Choose between the example or actual input dataset.",
        ),
    ] = Dataset.EXAMPLE,
    input_path: Annotated[
        Path | None,
        typer.Option(
            "--input-path",
            "-i",
            exists=False,
            help="Optional override path for the input file.",
        ),
    ] = None,
) -> None:
    """Run a specific problem for the requested dataset."""

    problem = get_problem(day)
    data = _read_input(day, dataset, input_path)
    result = _execute(problem, data)

    typer.echo(f"Day {problem.day:02d} – {problem.name}")
    typer.echo(f"  Part 1: {result.part_one}")
    typer.echo(f"  Part 2: {result.part_two}")


if __name__ == "__main__":
    app()
