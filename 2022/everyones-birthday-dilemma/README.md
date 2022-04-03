# Everyone's Birthday Dilemma

## Problem Statement

UQCS wants to find a date for codejam which doesn't overlap with anyone's birthdays next year.

Given a list of birthdays of everyone planning to come to codejam, determine the best day to hold the codejam.

- We want to choose a day which conflicts with the least number of birthdays
- If there are multiple candidate days with the same number of birthdays, we want to choose the earliest.

## Input Format

- The first line contains an integer $n$: the number of people that are planning to attend codejam
- The next $n$ lines contian one integer $x_i$: the birthdays of each of the $n$ people planning to attend codejam. This is represented as days from January 1st.

## Constraints

- $1 \le n \le 10^6$
- $0 \le x_i < 365$

## Output Format
one integer: the day chosen to hold codejam (represented as days from January 1st)

## Sample Input

```
3
0
1
60
```

## Sample Output

```
2
```
## Explanation

- There are birthdays on day 0, 1, and 60 of the year.
- All other days of the year do not conflict with a birthday.
- The earliest of the days which conflicts with the least number of birthdays is day 2

