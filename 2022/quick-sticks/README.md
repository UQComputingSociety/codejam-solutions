# Quick Sticks

## Problem Statement

Some of the UQCS committee are running late for an unnamed university programming competition.

They are gathered in the ITLC and each insist on travelling to the event via tandem bike.

They only have access to one bike, which can fit a maximum of two people at a time. The bike can only travel as fast as the slowest person on the bike.

Given the travel times of each person, determine the minimum time required for everyone to travel to the event.

## Input Format

- The first line is an integer $n$: the number of people that need to travel to the event

- The next line contains $n$ integers: $x_1, \ldots, x_n$ travel time of each person

## Constraints

- $1 \le n \le 15$
- $1 \le x_i \le 1000$

## Output Format
One integer: the minimum time required to transport everyone to the event

## Sample Input

```
3
1 2 3
```

## Sample Output

```
6
```

## Explanation

- On the first trip, 1 and 2 travel to the event (2 minutes)
- 1 returns to the ITLC with the bike (1 minute)
- 1 and 3 travel to the event (3 minutes)
- Now all people are at the event (total 6 minutes)
