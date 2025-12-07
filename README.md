AOC 2025 scaffolding with a Typer-powered runner.

## Usage

```bash
uv run python -m aoc_25.runner run 1 --dataset example
```

Use `--dataset actual` or `--input-path` to point at custom files. Input files live in `inputs/dayXX_example.txt` and `inputs/dayXX_actual.txt`.

## Practice Problems

There is a `aoc_25.practice` namespace alongside the daily problems for sandbox puzzles. Use `Practice01` as a template; each practice problem takes raw input in `__init__` and exposes `solve_part_one` / `solve_part_two`. Extend `aoc_25/practice/__init__.py` with new classes to register them.
