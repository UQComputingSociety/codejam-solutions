#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve_polygon_area' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_DOUBLE_ARRAY points
#

def solve_polygon_area(N, points):
    mid = [0,0]
    # for x,y in points:
    #     mid[0] += x
    #     mid[1] += y 
    # mid[0] /= N 
    # mid[1] /= N 

    # for p in points:
    #     p[0] -= mid[0] 
    #     p[1] -= mid[1]

    area = 0 
    for i in range(N):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % N]
        area += 0.5 * (x1*y2 - x2*y1)
    return abs(area)


if __name__ == '__main__':
    fptr = sys.stdout

    N = int(input().strip())

    points = []

    for _ in range(N):
        points.append(list(map(float, input().rstrip().split())))

    result = solve_polygon_area(N, points)

    fptr.write(str(result) + '\n')

    fptr.close()
