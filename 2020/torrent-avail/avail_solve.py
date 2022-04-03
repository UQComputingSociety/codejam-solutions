#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a FLOAT.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER P
#  3. 2D_STRING_ARRAY computer_pieces
#

def solve(N, P, computer_pieces):
    # Compute and return the availability metric.
    piece_counts = {k:0 for k in range(P)}
    for comp in computer_pieces:
        for piece in comp:
            piece_counts[piece] += 1

    min_count = min(piece_counts.values())
    for k in list(piece_counts):
        piece_counts[k] -= min_count
        if piece_counts[k] == 0:
            del piece_counts[k]
        else:
            assert piece_counts[k] > 0

    return (len(piece_counts) / P + min_count)

if __name__ == '__main__':
    #fptr = open(sys.argv[1], 'w')
    fptr = sys.stdout

    N = int(input().strip())

    P = int(input().strip())

    computer_pieces = []

    for _ in range(N):
        computer_pieces.append(list(map(int, input().rstrip().split())))

    result = solve(N, P, computer_pieces)

    fptr.write(str(result) + '\n')

    fptr.close()
