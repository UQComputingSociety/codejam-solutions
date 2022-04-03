# INFS1200

## Problem Statement

You are given the task of inserting a new item into a list of names in a database. Each name is stored as a string and the list is sorted in alphabetical order.

Calculate the index where the new item should be inserted into the database. If the value already exists the position returned should be its first occurence. Your algorithm should run in O(log n) time.

HINT: Try resubmitting multiple times if you don't pass test case 4 straight away.

## Input Format

- The first line represents the new item to be inserted.
- The second line indicates the length of the data $n$.
- The subsequent line/s represent each name in the database.

## Constraints

Your algorithm should have O(log n) time complexity.

## Output Format
Integer: index to store new entry.

## Sample Input

```
Steve
7
Alfred
Alice
Beth
John
Perceval
Tina
Xavier
```

## Sample Output

```
5
```


