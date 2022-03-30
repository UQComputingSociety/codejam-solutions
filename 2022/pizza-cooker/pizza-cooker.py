#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER c
#  3. INTEGER s
#  4. INTEGER p_c
#  5. INTEGER p_s
#  6. INTEGER p_b
#


def cost(n, c, s, p_c, p_s, p_b):
    c_pizzas = c * 3
    s_pizzas = s * 2

    b_to_buy = n

    c_whole = max(n - c_pizzas, 0)
    s_whole = max(n - s_pizzas, 0)

    c_to_buy = c_whole // 3 + (c_whole % 3 != 0)
    s_to_buy = s_whole // 2 + (s_whole % 2 != 0)

    return b_to_buy * p_b + c_to_buy * p_c + s_to_buy * p_s


def solve(x, c, s, p_c, p_s, p_b):
    left = 0
    right = max(x, (c + x) * 3, (s + x) * 2)

    while right - left > 1:
        mid = (left + right) // 2

        cost_ = cost(mid, c, s, p_c, p_s, p_b)

        if cost_ == x:
            return mid

        if cost_ > x:
            right = mid

        if cost_ < x:
            left = mid

    return left


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    x0 = int(input().strip())

    first_multiple_input = input().rstrip().split()

    c0 = int(first_multiple_input[0])

    s0 = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    p_c0 = int(second_multiple_input[0])

    p_s0 = int(second_multiple_input[1])

    p_b0 = int(second_multiple_input[2])

    res = solve(x0, c0, s0, p_c0, p_s0, p_b0)

    fptr.write(str(res) + "\n")

    fptr.close()
