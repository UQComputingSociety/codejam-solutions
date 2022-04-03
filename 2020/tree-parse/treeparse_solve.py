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
    # Write your code here
    parents = []
    for line in tree:
        prefix = None 
        prefix = line[(len(parents)-1)*2:len(parents)*2]
        # if parents and prefix != '+-':
        #     parents.pop()
        while parents and prefix != '+-':
            parents.pop()
            prefix = line[(len(parents)-1)*2:len(parents)*2]

        basename = line[len(parents)*2:]
        if line.endswith('/'):
            parents.append(basename)
        else:
            yield (''.join(parents) + basename)
            

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
