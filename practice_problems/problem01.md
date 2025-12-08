# Practice 01: Conveyor Calibration

## Part One

You stumble into a maintenance bay full of conveyor belts. Each belt is described by a sequence of `L` and `R` turns plus an integer speed. Belts are chained: the end of one connects to the start of the next. Your input is a list of belts, one per line, in the form `LLRLR 5` (directions then speed).

Starting with an initial heading of north and position `(0, 0)`, process the belts in order:

- For each character in the directions string, turn left or right 90 degrees, then move forward by the belt's speed in the current heading.
- After finishing a belt, continue with the next belt from the new heading/position.

Compute the Manhattan distance from the origin after all belts. What distance do you end up at?

### Example

```
LR 3
RRL 2
L 1
```

Walkthrough:

- Belt 1 (`LR`, speed 3): turn left (west), move 3 → (-3, 0); turn right (north), move 3 → (-3, 3).
- Belt 2 (`RRL`, speed 2): right (east) move 2 → (-1, 3); right (south) move 2 → (-1, 1); left (east) move 2 → (1, 1).
- Belt 3 (`L`, speed 1): left (north) move 1 → (1, 2).

Final distance from origin: `|1| + |2| = 3`.

## Part Two

The maintenance bot mentions some belts are faulty: any belt with an *even* speed causes the robot to **skip the next turn instruction** on that same belt (it still moves for the remaining instructions).

Apply this rule while walking the belts. What is the Manhattan distance from the origin now?
