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
        num_cols = len(lines[0])

        # Trim out the operators
        lines = lines[0:-1]

        # Loop over every character in the worksheet, building the vertical digits, keeping whitespace
        columns = defaultdict(list)
        for i in range(0, num_cols):
            for j in range(0, len(lines)):
                ch = lines[j][i]
                if ch != " ":
                    columns[i].append(int(ch))

        problem_index = 0
        # Seed the results with the operator's identity value
        results = [0 if op == "+" else 1 for op in operators]

        for i in range(0, num_cols):
            # We hit a column of pure white space, time to move on to the next problem
            if not (column := columns[i]):
                problem_index += 1
                continue

            # Build our number up MSB at the the, LSB at the bottom
            number = sum(
                int(val) * pow(10, len(column) - x - 1) for x, val in enumerate(column)
            )

            if operators[problem_index] == "+":
                results[problem_index] += number
            else:
                results[problem_index] *= number

        return str(sum(results))
