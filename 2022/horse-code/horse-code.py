#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING code
#  2. STRING_ARRAY morse_code
#


def decode(code, morse_code):
    # YOUR CODE
    horse_code = {
        "tbh": "thoroughbred horse",
        "smh": "shaking my hooves",
        "gtfo": "galloping through fields occasionally",
        "idc": "i don't canter",
        "btw": "big trough of water",
    }

    d = {letter: chr(ord("a") + i) for i, letter in enumerate(morse_code)}

    words = []

    code = code.split("/")

    for word in code:

        word = "".join([d[letter] for letter in word.split(" ") if letter != ""])
        word = horse_code.get(word, word)
        words.append(word)

    return " ".join(words)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    code0 = input()

    morse_code0 = []

    for _ in range(26):
        morse_code0_item = input()
        morse_code0.append(morse_code0_item)

    decoded = decode(code0, morse_code0)
    fptr.write(decoded + "\n")

    fptr.close()
