"""Reusable search algorithms for AoC puzzles."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Callable, Deque, Dict, Generic, Iterable, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class SearchResult(Generic[T]):
    """Information about a search that finished."""

    node: T
    cost: int
    parents: Dict[T, T]

    def reconstruct_path(self, start: T) -> list[T]:
        """Return path from ``start`` to the result node."""

        path = [self.node]
        current = self.node
        while current != start:
            current = self.parents[current]
            path.append(current)
        return list(reversed(path))


def bfs(
    start: T,
    *,
    is_goal: Callable[[T], bool],
    neighbors: Callable[[T], Iterable[T]],
) -> SearchResult[T] | None:
    """Breadth-first search over an unweighted graph."""

    queue: Deque[tuple[T, int]] = deque([(start, 0)])
    parents: Dict[T, T] = {}
    seen: set[T] = {start}

    while queue:
        node, dist = queue.popleft()
        if is_goal(node):
            return SearchResult(node=node, cost=dist, parents=parents)

        for neighbor in neighbors(node):
            if neighbor in seen:
                continue
            seen.add(neighbor)
            parents[neighbor] = node
            queue.append((neighbor, dist + 1))

    return None


def dijkstra(
    start: T,
    *,
    is_goal: Callable[[T], bool],
    neighbors: Callable[[T], Iterable[tuple[T, int]]],
) -> SearchResult[T] | None:
    """Dijkstra's algorithm for weighted graphs."""

    heap: list[tuple[int, T]] = [(0, start)]
    parents: Dict[T, T] = {}
    costs: Dict[T, int] = {start: 0}

    while heap:
        cost, node = heappop(heap)
        if cost != costs.get(node, cost):
            continue
        if is_goal(node):
            return SearchResult(node=node, cost=cost, parents=parents)

        for neighbor, weight in neighbors(node):
            new_cost = cost + weight
            if new_cost < costs.get(neighbor, new_cost + 1):
                costs[neighbor] = new_cost
                parents[neighbor] = node
                heappush(heap, (new_cost, neighbor))

    return None
