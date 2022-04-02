#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'toText' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def toText(n):
    words = {1:'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine',
             10: 'ten',
             11: 'eleven',
             12: 'twelve',
             13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen',
             16: 'sixteen',
             20: 'twenty',
             30: 'thirty',
             40: 'forty',
             50: 'fifty',
             60: 'sixty',
             80: 'four-twenties',
             100: 'one-hundred'}
    num = n
    separator = "-and-" if (num % 10 == 1 and num < 80) else "-"

    if num in words:
        return words[num]
    else:
        tens, ones = num // 10 * 10, num % 10
        if 17 <= num < 20:
            word = "ten" + separator + words[ones]
        elif 20 <= num < 60:
            word = words[tens] + separator + words[ones]
        elif 60 < num < 80:
            word = 'sixty' + separator + toText(num - 60)
        elif num == 80:
            word = 'four-twenties'
        elif num > 80:
            word = 'four-twenty'+ separator + toText(num - 80)
        return word

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    word = toText(num)

    fptr.write(word + '\n')

    fptr.close()