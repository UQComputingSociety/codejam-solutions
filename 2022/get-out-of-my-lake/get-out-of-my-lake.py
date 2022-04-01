#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a 2D_CHARACTER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER r
#  3. INTEGER c
#  4. 2D_CHARACTER_ARRAY grid
#

sys.setrecursionlimit(10000)


def solve_r(n, r, c, grid):
    if grid[r][c] == "0":
        grid[r][c] = "#"

    if grid[r][c] != "1":
        return

    grid[r][c] = "_"

    for r_, c_ in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= r_ and r_ < n and 0 <= c_ and c_ < n:
            solve_r(n, r_, c_, grid)


def solve(n, r, c, grid):
    solve_r(n, r, c, grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] != "0":
                continue
            for r_, c_ in [(i + k, j + l) for k in (-1, 1) for l in (-1, 1)]:
                if 0 <= r_ and r_ < n and 0 <= c_ and c_ < n and grid[r_][c_] == "_":
                    grid[i][j] = "#"

    return [[ch if ch != "_" else "1" for ch in row] for row in grid]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n0 = int(input().strip())

    first_multiple_input = input().rstrip().split()

    r0 = int(first_multiple_input[0])

    c0 = int(first_multiple_input[1])

    grid0 = []

    for _ in range(n0):
        grid0.append(list(map(lambda x: x[0], input().rstrip().split())))

    res = solve(n0, r0, c0, grid0)

    fptr.write("\n".join([" ".join(x) for x in res]))
    fptr.write("\n")

    fptr.close()
