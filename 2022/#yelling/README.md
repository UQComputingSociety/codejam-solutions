# \# yelling

## Problem Statement

It's time to implement the #yelling feature of our very own UQCS Discord Bot!

Given a string $s$, calculate the percentage of letters that are in lowercase and yell out the corresponding message. If there are no lowercase characters, print out "Acceptable."

Otherwise, let $x$ be the percentage of lowercase characters in the text. If:

- 0% < x < 15%, yell out "WHAT WAS THAT?!"
- 15% <= x < 25%, yell out "SAY THAT AGAIN?!"
- 25% <= x < 50%, yell out "YELL IT LOUDER!"
- 50% <= x < 65%, yell out "I CAN'T HEAR YOU!!"
- 65% <= x < 75%, yell out "I THOUGHT I HEARD SOMETHING?!"
- x >= 75%, yell out "WHY ARE YOU SO QUIET?"


Whitespaces are included in the total string length, but are not counted as lowercase characters.

Please see the #yelling channel on Discord for further reference.

## Input Format

A single string, $s$.

## Constraints

$s$ only contains letters and whitespaces.

$0 < len(s) < 1000$

## Output Format
A string message.

## Sample Input

```
YEEEEEEEeEEEEEET
```

## Sample Output

```
WHAT WAS THAT?!
```

