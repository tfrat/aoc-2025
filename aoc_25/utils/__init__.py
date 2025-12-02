"""
Utility helpers shared across Advent of Code 2025 solutions.

The modules provide parsing helpers, grid utilities, geometric primitives,
and ready-made search routines that frequently appear across AoC problems.
"""

from __future__ import annotations

from .geometry import Direction, Point
from .grid import Grid2D, parse_grid
from .parsing import (
    chunk_by_blank_lines,
    chunk_every,
    extract_ints,
    parse_ints,
    sliding_window,
)
from .search import bfs, dijkstra

__all__ = [
    "Direction",
    "Point",
    "Grid2D",
    "parse_grid",
    "chunk_by_blank_lines",
    "chunk_every",
    "extract_ints",
    "parse_ints",
    "sliding_window",
    "bfs",
    "dijkstra",
]
