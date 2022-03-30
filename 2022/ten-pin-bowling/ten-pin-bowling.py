#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculateScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING scores as parameter.
#

class Turn():
    def __init__(self, val1, val2, nxt=None):
        self.val1 = val1
        self.val2 = val2
        self.next = nxt

class TurnList():
    def create(self, scoreList):
        turnList = Turn(0, 0, None)
        head = turnList
        for s in scoreList:
            ball1, ball2 = s[0], s[1]
            turnList.next = Turn(ball1, ball2, None)
            turnList = turnList.next
        return head.next

def get_pins(p):
    if p is None:
        return 0
    elif p == "-" or p == "_":
        return 0
    if p == "X" or p == "/":
        return 10
    else:
        return int(p)

def get_bonus(curr, mark):
    bonus = 0
    if curr.next is None:
        return 0
    b1 = curr.next.val1
    b2 = curr.next.val2

    # strike was originally scored
    if mark == "X":
        # next ball is also a strike
        if b1 == "X":
            bonus += get_pins(b1)
            print(curr.next.next)
            if curr.next.next:
                bonus += get_pins(curr.next.next.val1)
        # next ball is a spare
        elif b2 == "/":
            bonus += 10
        # add next two balls normally
        else:
            bonus += get_pins(b1)
            bonus += get_pins(b2)
    # spare was originally scored
    elif mark == "/":
        bonus += get_pins(b1) 
    return bonus

def calculateScore(scores):
    turnList = TurnList()
    turns = turnList.create(scores) 
    head = turns
    curr = head
    total = 0

    while curr:
        b1, b2 = curr.val1, curr.val2
        frame = 0
        if b1 == "X":
            frame += 10
            frame += get_bonus(curr, b1)
        else:
            if b2 == "/":
                frame += 10
                frame += get_bonus(curr, b2)
            else:
                frame += get_pins(b1)
                frame += get_pins(b2)
        total += frame
        curr = curr.next
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    scores = []

    for _ in range(t):
        scores.append(list(map(lambda x: x[0], input().rstrip().split())))

    total = calculateScore(scores)

    fptr.write(str(total) + '\n')

    fptr.close()
