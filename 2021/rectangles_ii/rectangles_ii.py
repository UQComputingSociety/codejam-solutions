#!/bin/python

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

def solve(table):
    min_x, min_y = float('-inf'), float('-inf')
    max_x, max_y = float('inf'), float('inf')
    for x1, y1, x2, y2 in table:
        # assert x1 < x2 and y1 < y2
        min_x = max(x1, min_x)
        min_y = max(y1, min_y)

        max_x = min(x2, max_x)
        max_y = min(y2, max_y)

    for x1, y1, x2, y2 in table:
        assert x1 <= min_x and max_x <= x2
        assert y1 <= min_y and max_y <= y2
    return map(int, (min_x, min_y, max_x, max_y))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    data = []

    for _ in range(N):
        data.append(list(map(float, input().rstrip().split())))

    result = solve(data)

    fptr.write('\n'.join(list(map(str, result))))
    fptr.write('\n')

    fptr.close()
