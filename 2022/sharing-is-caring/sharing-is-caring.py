#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY sizes
#


def solve(n, sizes):
    memo = {}
    return solve_r(0, 0, n, sizes, memo)


M = 1000000000


def solve_r(diff, i, n, sizes, memo):
    if (diff, i) in memo:
        return memo[diff, i]

    if i == n:
        return 0 if diff == 0 else M

    size = sizes[i]

    left = solve_r(abs(diff - size), i + 1, n, sizes, memo)
    right = solve_r(diff + size, i + 1, n, sizes, memo)
    mid = solve_r(diff, i + 1, n, sizes, memo) + size

    res = min(left, right, mid)
    memo[diff, i] = res
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n0 = int(input().strip())

    sizes0 = list(map(int, input().rstrip().split()))

    res = solve(n0, sizes0)

    fptr.write(str(res) + "\n")

    fptr.close()
