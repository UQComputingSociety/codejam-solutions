# JetChar Airlines

## Problem Statement

With the borders now open, you and a few friends decide to go to Hawaii for the weekend. As cheap uni students, you settle for flying with the cheapest budget airline, JetChar.

Being the cheapest budget airline, JetChar has lost your all your baggage. Being the spiteful uni students you are, you decide to take out your misfortune on everyone else and decide to steal as many suitcases as possible from the baggage carousel.

For each suitcase, there is one small window of opportunity to steal it while it is on the luggage carousel. To steal a stuitcase, you must keep a close eye on it for the entire duration that it is on a luggage carousel. You can only take the suitcase at the end of this time window. You cannot steal two suitcases at the same time. 

Once you have stolen a suitcase, you can begin the process of stealing the next suitcase in the next time period.

Given a list of suitcases and their start and end windows of opportunity, output the maximum number of suitcases you can steal.

## Input Format

The first line contains the number of suitcases, $n$.

Each of the $n$ following lines represents a single suitcase and contains two numbers; the first number $x$ is the start time of the window of opportunity for that particular suitcase, and the second number $y$ is the end time.

## Constraints

$0 < len(n) < 100$

$0 < x < 300$

$0 < y < 300$

$x < y$

## Output Format
A single integer.

## Sample Input

```
4
3 4
9 11
10 17
16 19
```

## Sample Output

```
3
```

## Explanation


- You spend time periods 3 and 4 stealing the first stuitcase.
- You spend time periods 9 to 11 stealing the second suitcase.
- You can begin stealing the next suitcase in time period 12, but it is too late to steal the third stuitcase.
- You spend time periods 16 to 19 stealing the fourth suitcase.

In total you have stolen 3 suitcases. This is the maximum number of suitcases can be stolen.