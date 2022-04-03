#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'draw_keyboard' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER num_letters
#  2. CHARACTER_ARRAY letters
#

KEYBOARD = '''Q W E R T Y U I O P
 A S D F G H J K L
  Z X C V B N M'''
import string

LETTERS = set(string.ascii_uppercase)

def draw_keyboard(num_letters, letters):
    delete_letters = LETTERS.difference(set(letters))
    k = KEYBOARD
    for x in delete_letters:
        k = k.replace(x, ' ')
    return k
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    keys = []

    for _ in range(N):
        keys_item = input()[0]
        keys.append(keys_item)

    keyboard = draw_keyboard(N, keys)

    fptr.write(keyboard + '\n')

    fptr.close()
