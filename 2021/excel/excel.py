import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING expr
#  2. STRING cellRange
#


# A = 1, Z = 26, AA = 27, AZ = 52

def parse_b26(letter):
    x = 0
    c = len(letter) - 1
    for i, n in enumerate(letter):
        x += 26**c * (ord(n) - ord('A') + 1)
        c -= 1
    return x

def to_b26(num):
    x = []
    while num > 0 or not x:
        y = (num - 1) % 26
        x.append(y)
        num -= y
        num //= 26
    return ''.join(chr(ord('A') + i) for i in x)[::-1]

def to_ints(pos):
    pos = pos.replace('$', '')
    col = pos.rstrip('1234567890')
    row = pos[len(col):]

    col = parse_b26(col)
    row = int(row)

    return row, col

def sign(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

def solve(expr, cellRange):
    lock_col = '$' == expr[0]
    lock_row = '$' in expr and expr.rindex('$') > 0
    expr = expr.replace('$', '')
    expr = to_ints(expr)

    start, end = cellRange.split(':')
    r0, c0 = to_ints(start)
    r1, c1 = to_ints(end)

    dr = sign(r1 - r0)
    dc = sign(c1 - c0)

    assert dr == 0 or dc == 0

    # print(dr, dc)

    xr, xc = expr

    o = []
    r, c = r0, c0
    while True:
        s = ''
        if lock_col:
            s += '$' + to_b26(xc)
        else:
            s += to_b26(xc)
            xc += dc

        if lock_row:
            s += '$' + str(xr)
        else:
            s += str(xr)
            xr += dr

        o.append(s)
        if r == r1 and c == c1: break
        r += dr
        c += dc

    return o


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    exprInput = input()

    rangeInput = input()

    result = solve(exprInput, rangeInput)

    print(' '.join(result))
    fptr.write(' '.join(result))
    fptr.write('\n')

    fptr.close()
