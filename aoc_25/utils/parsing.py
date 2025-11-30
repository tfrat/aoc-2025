"""General-purpose parsing helpers for Advent of Code inputs."""

from __future__ import annotations

import re
from itertools import islice
from typing import Iterable, Iterator, Sequence, Tuple, TypeVar

T = TypeVar("T")

_INT_RE = re.compile(r"-?\d+")


def chunk_by_blank_lines(text: str) -> list[list[str]]:
    """Split text into sections separated by blank lines."""

    sections: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.strip():
            current.append(line)
        elif current:
            sections.append(current)
            current = []
    if current:
        sections.append(current)
    return sections


def chunk_every(iterable: Iterable[T], size: int) -> Iterator[tuple[T, ...]]:
    """Yield tuples of ``size`` elements from ``iterable``."""

    if size <= 0:
        raise ValueError("size must be positive")

    iterator = iter(iterable)
    while batch := tuple(islice(iterator, size)):
        if len(batch) != size:
            return
        yield batch


def sliding_window(sequence: Sequence[T], size: int) -> Iterator[tuple[T, ...]]:
    """Generate overlapping windows of ``size`` from ``sequence``."""

    if size <= 0:
        raise ValueError("size must be positive")
    if size > len(sequence):
        return

    window: Tuple[T, ...] = tuple(sequence[:size])
    yield window

    for index in range(size, len(sequence)):
        window = window[1:] + (sequence[index],)
        yield window


def parse_ints(line: str, sep: str | None = None) -> list[int]:
    """Parse integers from a single line."""

    if sep is None:
        return [int(match.group()) for match in _INT_RE.finditer(line)]

    parts = [chunk.strip() for chunk in line.split(sep) if chunk.strip()]
    return [int(part) for part in parts]


def extract_ints(text: str) -> list[int]:
    """Extract all integers from a text block."""

    return [int(match.group()) for match in _INT_RE.finditer(text)]
