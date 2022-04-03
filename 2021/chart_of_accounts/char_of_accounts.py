#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY table as parameter.
#
class State:
    def __init__(self):
        self.up = True
        self.down = True
        self.equal = True

    def __str__(self):
        if self.up:
            return 'A'
        elif self.down:
            return 'D'
        elif self.equal:
            return 'E'
        else:
            return '-'

def solve(table):
    state = [State() for i in range(len(table[0]))]
    prev = None
    # Write your code here
    for row in table:
        if prev is None:
            prev = row
            continue
        for i, x in enumerate(row):
            p = prev[i]
            state[i].down &= x < p
            state[i].up &= x > p
            state[i].equal &= x == p

            prev[i] = x

    return state


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    R = int(first_multiple_input[0])

    C = int(first_multiple_input[1])

    data = []

    for _ in range(R):
        data.append(list(map(int, input().rstrip().split())))

    result = solve(data)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
