# Get Ouf Of My Lake!

## Problem Statement

The ‘UQ Lake and Amphitheatre Renewal’ project has attracted a new kind of student: Shrek. 

UQ has allowed Shrek to build a lake house on one of the lakes on campus. 
They know that he is very territorial, and have agreed to build a fence around the lake which he chooses to reside in.

Given a map of lakes, and the coordinates of Shrek's lake house, draw a fence around the lake containing Shrek's house. 

All edges of the lake area should be adjacent to a fence.

## Input Format

- The first line contains one integer $n$: the length and width of the map
- The second line contains two integers $r$ and $c$: the coordinates (row, column) for Shrek's lake house
- The next $n$ lines contain $n$ characters representing a 2d map: 0 for land, 1 for lake

A lake is a group of 4-directionally connected group of 1s

## Constraints

- $4 \leq n \leq 100$
- Lakes do not touch diagonally
- There are no lakes on the border of the map
- The coordinates for the lake house are always on a lake

## Output Format
Output the $n \times n$ 2d map with a border drawn around Shrek's lake.

## Sample Input

```
10
1 2
0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 0
0 1 0 0 0 0 0 0 0 0
0 1 1 0 0 1 1 0 0 0
0 1 0 0 0 1 1 0 0 0
0 0 0 0 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
```

## Sample Output

```
# # # # # # # # # 0
# 1 1 1 1 1 1 1 # 0
# 1 1 1 1 1 1 1 # 0
# 1 # # # # # # # 0
# 1 1 # 0 1 1 0 0 0
# 1 # # 0 1 1 0 0 0
# # # 0 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 0
0 1 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
```

## Explanation

There are two lakes on the map. Shrek wants to place his lake house on row 1 col 2. We draw a fence around the top lake so that all edges of the lake are surrounded by #

