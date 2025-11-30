# Repository Guidelines

## Project Structure & Module Organization
- Core package lives under `aoc_25/` with submodules `problems/`, `utils/`, and `runner.py`.
- Placeholder day solutions: `aoc_25/problems/dayXX.py`. Implement logic per part there.
- Shared helpers: `aoc_25/utils/` (parsing, geometry, grids, search) and `aoc_25/__init__.py` exposes the Typer app.
- Inputs reside in `inputs/dayXX_example.txt` and `inputs/dayXX_actual.txt`. Keep large inputs out of Git if they are personal data.
- `main.py` is the simple entrypoint while `pyproject.toml` defines dependencies and the `aoc25` script.

## Build, Test, and Development Commands
```bash
uv run python -m aoc_25.runner run 1 --dataset example   # Run day 01 with example input
uv run python main.py run 1                              # Alternate entrypoint
uv sync                                                  # Install/lock dependencies
```
Add puzzle-specific scripts under `scripts/` if necessary; document them here.

## Coding Style & Naming Conventions
- Python 3.14+, fully typed. Enable `from __future__ import annotations` in new modules.
- Follow standard PEP 8 with 4-space indentation; prefer dataclasses over heavy frameworks unless required.
- Name puzzle classes `DayXX`; functions use `snake_case`. Inputs: `dayXX_example.txt` / `dayXX_actual.txt`.
- Keep comments succinct and only for non-obvious intent; avoid redundancy.

## Testing Guidelines
- Prefer pytest (add to `pyproject.toml` when needed). Place tests under `tests/` mirroring module paths (`tests/test_day01.py`).
- Cover both parts of each day plus helper utilities. When parsing inputs, test corner cases like blank lines and malformed tokens.
- Run `uv run pytest` before submitting changes. Include sample input fixtures in `tests/data/` if they’re small.

## Commit & Pull Request Guidelines
- Write clear, descriptive commits: `feat(day05): add part two solver` or `chore(utils): add grid parser`.
- PRs should describe problem day, approach, and verification. Link AoC problem statement or issue number if tracked.
- Include CLI output snippets showing both parts’ answers and any test results. Add screenshots only when visual output is relevant.
