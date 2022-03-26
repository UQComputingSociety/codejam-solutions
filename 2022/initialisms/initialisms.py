#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialismConverter' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def initialismConverter(s):
    # Write your code here
    out = ""
    for word in s.split():
        if word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            out += word[0]

    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = initialismConverter(s)

    fptr.write(result + '\n')

    fptr.close()
