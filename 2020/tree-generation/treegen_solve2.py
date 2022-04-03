#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

def rec(d, n):
    s = []
    for k in sorted(d, key=lambda x: (len(d[x]) == 0, x)):
        s.append((max(0,n-1)*"| ") + ("+-" if n > 0 else "") + k + ("/" if len(d[k]) > 0 else ""))
        s.extend(rec(d[k], n+1))
    return s

def draw_tree_layout(files):
    n = lambda: defaultdict(n)
    d = n()
    for i in files:
        r = d
        for j in i.split("/"):
            r = r[j]
    s = rec(d, 0)
    print('\n'.join(s))
    for i in range(len(s)):
        for j in range(0, len(s[i]), 2):
            if s[i][j] != "|":
                break
            for k in range(i+1, len(s)):
                if len(s[k]) > j and s[k][j] == "+":
                    b = True
                    break
                if len(s[k]) > j and s[k][j] != "|":
                    b = False
                    break
            else:
                b = False
            if b:
                continue
            s[i] = s[i][:j] + "  " + s[i][j+2:]
    return "\n".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    files_input = []

    for _ in range(N):
        files_input_item = input()
        files_input.append(files_input_item)

    result = draw_tree_layout(files_input)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
