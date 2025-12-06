from __future__ import annotations


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
        lines = lines[:-1]
        problem_index = 0
        total = 0
        curr_val = 0 if operators[problem_index] == "+" else 1
        for i in range(0, num_cols):
            column = ""
            for j in range(0, len(lines)):
                column += lines[j][i]
            column = column.strip()

            # We hit a column of pure white space, time to move on to the next problem
            if not column:
                total += curr_val
                problem_index += 1
                curr_val = 0 if operators[problem_index] == "+" else 1
                continue

            # Build our number up MSB at the top, LSB at the bottom
            number = int(column)

            curr_val = (
                curr_val + number
                if operators[problem_index] == "+"
                else curr_val * number
            )

        total += curr_val

        return str(total)
