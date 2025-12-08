from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True, slots=True)
class Point3D:
    x: int
    y: int
    z: int

    def distance(self, other: Point3D) -> float:
        return sqrt(
            pow(self.x - other.x, 2)
            + pow(self.y - other.y, 2)
            + pow(self.z - other.z, 2)
        )


def pair_closest(boxes: list[Point3D]) -> dict[int, set[Point3D]]:
    distances = {}
    for i, box in enumerate(boxes):
        for y in range(i + 1, len(boxes)):
            other_box = boxes[y]
            distances[box.distance(other_box)] = {box, other_box}
    return distances


def integrate_nodes(
    nodes: set[Point3D], junctions: list[set[Point3D]]
) -> list[set[Point3D]]:
    copied = junctions.copy()
    matches = []
    # Find all existing junctions that contain any of the input nodes
    for j in range(0, len(copied)):
        if copied[j] & nodes:
            matches.append(j)

    # No existing junctions reference the nodes, make a new junction
    if not matches:
        copied.append({*nodes})
    else:
        # Remove the matche junctions, merge and re-add back to the junctions list
        new_junction = {*nodes}
        for match in sorted(matches, reverse=True):
            new_junction |= copied.pop(match)
        copied.append(new_junction)
    return copied


class Day08:
    day = 8
    name = "Playground"

    def __init__(self, data: str):
        self.boxes = [
            Point3D(*[int(x) for x in line.split(",")]) for line in data.splitlines()
        ]

    def solve_part_one(self) -> str:
        junctions = []
        distances = pair_closest(self.boxes)
        sorted_distances = sorted(distances.items(), key=lambda x: x[0])
        for _ in range(1000):
            _, linked = sorted_distances.pop(0)
            junctions = integrate_nodes(linked, junctions)

        lengths = sorted([len(junction) for junction in junctions], reverse=True)

        return str(lengths[0] * lengths[1] * lengths[2])

    def solve_part_two(self) -> str:
        distances = pair_closest(self.boxes)
        sorted_distances = sorted(distances.items(), key=lambda x: x[0])
        junctions = []

        while len(junctions) != 1 or len(junctions[0]) != len(self.boxes):
            _, linked = sorted_distances.pop(0)
            junctions = integrate_nodes(linked, junctions)
        return str(linked.pop().x * linked.pop().x)
