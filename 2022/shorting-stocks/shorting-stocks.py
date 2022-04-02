#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def maxLoss(prices):
    maxi = prices[0]
    mini = 0
    for p in prices:
        maxi = max(maxi, p)
        mini = min(mini, p - maxi)
    return abs(mini)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    diff = maxLoss(p)

    fptr.write(str(diff) + '\n')

    fptr.close()
