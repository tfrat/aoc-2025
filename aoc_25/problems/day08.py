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


def closest_x_junctions(num_junctions: int) -> dict[int, set[Point3D]]:
    return {}


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
        for i in range(10):
            _, linked = sorted_distances[i]
            left, right = None, None
            for j in range(0, len(junctions)):
                if junctions[j] & linked:
                    if not left:
                        left = j
                        continue
                    if not right:
                        right = j
                        break

            match left, right:
                case None, None:
                    junctions.append({*linked})
                case _, None:
                    junctions[left] |= linked
                case _, _:
                    junctions[left] |= junctions[right]
                    junctions.pop(right)

        lengths = sorted([len(junction) for junction in junctions], reverse=True)

        return str(lengths[0] * lengths[1] * lengths[2])

    def solve_part_two(self) -> str:
        distances = pair_closest(self.boxes)
        sorted_distances = sorted(distances.items(), key=lambda x: x[0])
        junctions = []

        i = 0
        while len(junctions) != 1 or len(junctions[0]) != len(self.boxes):
            _, linked = sorted_distances[i]
            left, right = None, None
            for j in range(0, len(junctions)):
                if junctions[j] & linked:
                    if not left:
                        left = j
                        continue
                    if not right:
                        right = j
                        break

            match left, right:
                case None, None:
                    junctions.append({*linked})
                case _, None:
                    junctions[left] |= linked
                case _, _:
                    junctions[left] |= junctions[right]
                    junctions.pop(right)
            i += 1
        return str(linked.pop().x * linked.pop().x)
