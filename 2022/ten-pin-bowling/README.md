# Ten Pin Bowling

## Problem Statement

A local bowling alley's scoring system is under maintenance. The Big Lebowski and his bowling league need your help to score their match so they can win the championship.

You are given an array of char arrays containing the number of pins knocked down by bowling balls: 'X' (strike), '/' (spare), '-' (miss), or a number from 1-9 inclusive. Balls are bowled in groups of two called turns.

Each turn a maximum of 10 pins can be knocked down, either by a strike with the first ball, or a spare with the second ball. An underscore is left after a strike because the second ball of the turn gets skipped.

The number of pins knocked down in a turn is then added to the total, along with bonus points for a strike or spare.

**Bonus Points:**

- A strike is worth 10 points, plus the values of the **next two balls bowled in subsequent turn/s.**
- A spare is also worth 10 points, plus the value of the **next ball bowled in the subsequent turn.**

Example:

[["X", "_"], ["4", "3"], ["9", "/"], ["7", "3"]]

total = (10 + **4 + 3**) + (4 + 3) + (9 + 1 **+ 7**) + (7 + 3) = 51

(hint: bonus points for a strike or spare are in bold)

## Input Format

An integer n representing the number of turns
The next n lines are strings showing the points in each turn

## Constraints

$
0 < len(scores) \leq 20
$


## Output Format
The total points scored by the player.

## Sample Input

```
4
X _
4 3
9 /
7 3
```

## Sample Output

```
51
```

