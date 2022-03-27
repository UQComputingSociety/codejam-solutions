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
#  1. 2D_INTEGER_ARRAY times
#  2. INTEGER_ARRAY supply
#  3. INTEGER_ARRAY rate
#


def solve_r(time, to_visit, current, nodes, travel_time, supply, rate, memo):
    if (time, to_visit, current) in memo:
        return memo[time, to_visit, current]

    if to_visit == 0:
        return 0

    max_gain = 0
    for node in range(1, nodes):

        if ((to_visit >> node) & 1) == 0:
            continue

        gain = supply[node] - (time + travel_time[current][node]) * rate[node]

        if gain <= 0:
            continue

        gain += solve_r(
            time + travel_time[current][node],
            (to_visit & ~(1 << node)),
            node,
            nodes,
            travel_time,
            supply,
            rate,
            memo,
        )

        max_gain = max(gain, max_gain)

    memo[time, to_visit, current] = max_gain
    return max_gain


def solve(travel_time, supply, rate):
    nodes = 11
    memo = {}
    to_visit = (1 << nodes) - 1 & ~(1)
    supply = [0] + supply
    rate = [0] + rate
    return solve_r(0, to_visit, 0, nodes, travel_time, supply, rate, memo)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    times0 = []

    for _ in range(11):
        times0.append(list(map(int, input().rstrip().split())))

    supply0 = list(map(int, input().rstrip().split()))

    rate0 = list(map(int, input().rstrip().split()))

    res = solve(times0, supply0, rate0)

    fptr.write(str(res) + "\n")

    fptr.close()
