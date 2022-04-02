#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insert' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING entry
#  2. STRING_ARRAY data
#

# test case 4 had 3 million rows,
# needs to be binary search to not time out
def insert(entry, data):
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == entry:
            return mid
        elif data[mid] < entry:
            start = mid + 1
        elif data[mid] > entry:
            end = mid - 1
    return start
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    record = input()

    n = int(input().strip())

    records = []

    for _ in range(n):
        records_item = input()
        records.append(records_item)

    index = insert(record, records)

    fptr.write(str(index) + '\n')

    fptr.close()
