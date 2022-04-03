# All You Need Is Love

## Problem Statement

You are playing tennis but you're having trouble keeping track of the score, so you decide to write a program that will help you determine the winner...

In a typical match of tennis, 4 points win a game, 6 games win a set, and 2 sets win a match. However, you must win a game by at least two points. If two players are drawn at 4 points each, "deuce" is called. The winner of the next game is awarded "advantage", and can then win the game by taking the next point or be brought back to deuce if their opponent scores. There is no limit to the number of times players can tie at deuce.

Similarly, a set must be won by at least two games. If players are tied at 6-6 games, there is a tie-break. A tie-break is won by the first player to score 7 points. "Deuce" isn't used but the concept of the two-clear-point win remains.

Given a string sequence $s$ of a match record between two players A and B, return the winner of the first set.

NOTE: you must pass ALL of the test cases to gain points.

## Input Format

A single line containing a string $s$ containing a match record of which player A or B wins each point in the game.

## Constraints

$s$ consists of two characters only: "A" or "B". Also, the record will have at least a complete set (though it may not have a complete match).

## Output Format
A single line determining the winner, either A or B.

## Sample Input

```
AAABABBAABBAAAAAABAAABBBAAAABBBABAAAAABABABABAABBBABABAABABABAABABBBBABBBBABBBAAABAAAAAAAAABBAAAABABABAAA
```

## Sample Output

```
A
```

## Explanation

In the first set, the winners of the first set of games are as follows:

- Game 1: AAABA, so player A wins.
- Game 2: BBAABB, so player B wins.
- Game 3: AAAA, so player A wins.
- Game 4: AABAA, so player A wins.
- Game 5: ABBBAAAA, so player A wins.
- Game 6: BBBAB, so player B wins.
- Game 7: AAAA, so player A wins.
- Game 8: ABABABABAA, so player A wins.

So player A wins the first set with a record of 6 games to 2.

