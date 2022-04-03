#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'parse_tree_files' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY tree as parameter.
#

def parse_tree_files(tree):
    d = {-1: tree[0]}
    s = []
    for i in tree[1:]:
        n = i.find("+")
        d[n//2] = i[n+2:]
        if i[-1] != "/":
            s.append("".join(d[j] for j in range(-1,n//2+1)))
    return s
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = sys.stdout

    N = int(input().strip())

    tree_lines = []

    for _ in range(N):
        tree_lines_item = input()
        tree_lines.append(tree_lines_item)

    result = parse_tree_files(tree_lines)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
