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
    computers = list(map(set, computer_pieces))
    iteration = 0
    new_pieces = {1:1}
    while 1:
        new_pieces.clear()        
        for i, comp in enumerate(computers):
            next_i = (i+1) % len(computers)
            next_comp = computers[next_i]
            possible = list(comp - next_comp)
            if not possible: continue
            possible.sort(reverse=0) 
            possible.sort(key=lambda p: sum(p in c for c in computers))
            new_pieces[next_i] = possible[0]
        
        print(new_pieces, file=sys.stderr)
        if not new_pieces: break
            
        
        for i, p in new_pieces.items():
            assert p not in computers[i]
            computers[i].add(p)            
        iteration += 1
        
    
    return iteration

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
