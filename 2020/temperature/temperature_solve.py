#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'convert_one_temperature' function below.
#
# The function is expected to return a FLOAT.
# The function accepts following parameters:
#  1. CHARACTER target_unit
#  2. FLOAT source_value
#  3. CHARACTER source_unit
#

def convert_one_temperature(target_unit, source_value, source_unit):
    # Write your code here
    kelvin = None
    if source_unit == 'K':
        kelvin = source_value
    elif source_unit == 'C':
        kelvin = source_value + 273.15
    elif source_unit == 'F':
        kelvin = (source_value - 32) * 5/9 + 273.15

    if target_unit == 'K': return kelvin
    elif target_unit == 'C': return kelvin - 273.15
    elif target_unit == 'F': return (kelvin - 273.15) * 9/5 + 32

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    target = input()[0]

    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        x = float(first_multiple_input[0])

        unit = first_multiple_input[1][0]

        converted = convert_one_temperature(target, x, unit)

        fptr.write(str(converted) + '\n')

    fptr.close()
