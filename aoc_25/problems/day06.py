from __future__ import annotations

from aoc_25.utils import parse_ints


class Day06:
    day = 6
    name = "Trash Compactor"

    def __init__(self, data: str):
        self.lines = data.splitlines()
        self.operators = self.lines[-1].split()
        self.problem_lines = self.lines[:-1]
        self.num_cols = len(self.lines[0]) if self.lines else 0

    def solve_part_one(self) -> str:
        results = parse_ints(self.problem_lines[0])
        for line in self.problem_lines[1:]:
            values = parse_ints(line)
            for i, value in enumerate(values):
                if self.operators[i] == "+":
                    results[i] += value
                else:
                    results[i] *= value
        return str(sum(results))

    def solve_part_two(self) -> str:
        problem_index = 0
        total = 0
        curr_val = 0 if self.operators[problem_index] == "+" else 1
        for i in range(0, self.num_cols):
            column = "".join(line[i] for line in self.problem_lines).strip()

            # We hit a column of pure white space, time to move on to the next problem
            if not column:
                total += curr_val
                problem_index += 1
                curr_val = 0 if self.operators[problem_index] == "+" else 1
                continue

            number = int(column)

            curr_val = (
                curr_val + number
                if self.operators[problem_index] == "+"
                else curr_val * number
            )

        total += curr_val

        return str(total)
