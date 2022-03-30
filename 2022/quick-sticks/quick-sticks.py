#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY times
#


def solve_r(left, n, speed, memo):

    if (left) in memo:
        return memo[left]

    _left = [i for i in range(n) if left & (1 << i) != 0]
    right = [i for i in range(n) if left & (1 << i) == 0]

    pairs = itertools.combinations(_left, 2)

    if len(_left) <= 2:
        return max([speed[i] for i in _left])

    min_time = sys.maxsize

    for pair in pairs:
        trip = max([speed[i] for i in pair])
        ret = min(*pair, *right[:1])

        next_left = (left & ~(1 << pair[0]) & ~(1 << pair[1])) | (1 << ret)
        res = trip + speed[ret] + solve_r(next_left, n, speed, memo)
        min_time = min(min_time, res)

    memo[left] = min_time

    return min_time


def solve(n, times):
    # YOUR SOLUTION HERE

    speed = sorted(times)
    memo = {}
    left = (1 << n) - 1

    return solve_r(left, n, speed, memo)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n0 = int(input().strip())

    times0 = list(map(int, input().rstrip().split()))

    time = solve(n0, times0)

    fptr.write(str(time) + "\n")

    fptr.close()
