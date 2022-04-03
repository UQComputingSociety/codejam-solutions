#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compute_clash_groups' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER num_events
#  2. 2D_INTEGER_ARRAY events
#

def compute_clash_groups(num_events, events):
    groups = []
    group = []
    clash_ending = None
    events.sort(key=lambda e: (e[1], e[2]))
    clash_ending = 0
    for event in events:
        id, h, m, d = event
        start = h*60 + m 
        end = h*60 + m + d
        if clash_ending is None:
            clash_ending = end

        if start >= clash_ending:
            if group:
                groups.append(group)
            group = [] 
        clash_ending = max(clash_ending, end)
        group.append(id)
    if group:
        groups.append(group)
    return [' '.join(map(str,sorted(g))) for g in groups]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = sys.stdout

    N = int(input().strip())

    events_input = []

    for _ in range(N):
        events_input.append(list(map(int, input().rstrip().split())))

    output = compute_clash_groups(N, events_input)

    fptr.write('\n'.join(output))
    fptr.write('\n')

    fptr.close()
