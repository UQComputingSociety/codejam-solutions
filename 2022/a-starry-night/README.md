# A *-ry Night

## Problem Statement

Given a 20x20 grid of cells, you'll need to find an optimal (shortest, least number of cells visited) path from a single point to another single point, navigating around "walls".

The starting point will be a cell containing "1", the ending point will be a cell containing "2", walls will be "-", and all other cells will be '\*'.

## Input Format

A table, with rows seperated by newlines and columns seperated by columns. You can assume the table format is correct and exactly as described.

## Constraints

The optimal solution for a grid will never be ambiguous, and it will always exist.

## Output Format
A list of comma-seperated "points" in the grid, starting with the start cell and ending with the end cell.

## Sample Input

```
1,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,*
2,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*
```

## Sample Output

```
(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(19,1),(19,2),(18,2),(17,2),(16,2),(15,2),(14,2),(13,2),(12,2),(11,2),(10,2),(9,2),(8,2),(7,2),(6,2),(5,2),(4,2),(3,2),(2,2),(1,2),(0,2)
```

