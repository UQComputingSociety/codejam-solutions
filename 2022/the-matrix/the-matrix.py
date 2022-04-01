#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'invert_matrix' function below.
#
# The function is expected to return a 2D_FLOAT_ARRAY.
# The function accepts 2D_INTEGER_ARRAY a as parameter.
#

def invert_matrix(a):
    a1, b1, c1, d1 = a[0][0], a[0][1], a[1][0], a[1][1] 
    det = (a1 * d1) - (b1 * c1)
    adj = [[d1, -b1], [-c1, a1]]
    if det == 0:
        return [[0.0, 0.0], [0.0, 0.0]]
    for i in range(len(adj)):
        for j in range(len(adj[0])):
            adj[i][j] = round(adj[i][j] / det, 2)
    return adj

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    matrix = []

    for _ in range(2):
        matrix.append(list(map(int, input().rstrip().split())))

    result = invert_matrix(matrix)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
