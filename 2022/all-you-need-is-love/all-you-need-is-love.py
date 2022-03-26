#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'AllYouNeedIsLove' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def AllYouNeedIsLove(s):
    # Write your code here
    aPoints = aGames = aSets = aTieBreak = 0
    bPoints = bGames = bSets = bTieBreak = 0

    for char in s:
        if aGames == bGames == 6:  # tie break
            # update points
            if char == "A":
                aTieBreak += 1
            elif char == "B":
                bTieBreak += 1
        else:
            # update points
            if char == "A":
                aPoints += 1
            elif char == "B":
                bPoints += 1

            # update games
            if aPoints >= 4 and (aPoints - bPoints > 1):
                aPoints = bPoints = 0
                aGames += 1
            elif bPoints >= 4 and (bPoints - aPoints > 1):
                aPoints = bPoints = 0
                bGames += 1

        # set winner: no tiebreak
        if aGames >= 6 and (aGames - bGames > 1):
            return "A"
        elif bGames >= 6 and (bGames - aGames > 1):
            return "B"

        if aTieBreak >= 7 and (aTieBreak - bTieBreak > 1):
            return "A"
        elif bTieBreak >= 7 and (bTieBreak - aTieBreak > 1):
            return "B"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = AllYouNeedIsLove(s)

    fptr.write(result + '\n')

    fptr.close()
