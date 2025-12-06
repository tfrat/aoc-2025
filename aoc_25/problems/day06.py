from __future__ import annotations

from collections import defaultdict

from aoc_25.utils import parse_ints


class Day06:
    day = 6
    name = "Trash Compactor"

    def solve_part_one(self, data: str) -> str:
        lines = data.splitlines()
        operators = lines[-1].split()
        results = parse_ints(lines[0])
        for line in lines[1:-1]:
            values = parse_ints(line)
            for i, value in enumerate(values):
                if operators[i] == "+":
                    results[i] += value
                else:
                    results[i] *= value
        return str(sum(results))

    def solve_part_two(self, data: str) -> str:
        lines = data.splitlines()
        operators = lines[-1].split()
        results = [0 if op == "+" else 1 for op in operators]
        problem_index = 0
        i = 0
        stacks = defaultdict(list)
        while i < len(lines[0]):
            for j in range(0, len(lines) - 1):
                stacks[i].append(lines[j][i])
            i += 1
        for i in range(0, len(stacks)):
            filtered = list(filter(lambda x: x != " ", stacks[i]))
            collapsed = sum(
                int(val) * pow(10, len(filtered) - x - 1)
                for x, val in enumerate(filtered)
            )
            if not collapsed:
                problem_index += 1
                continue
            if operators[problem_index] == "+":
                results[problem_index] += collapsed
            else:
                results[problem_index] *= collapsed
        return str(sum(results))
