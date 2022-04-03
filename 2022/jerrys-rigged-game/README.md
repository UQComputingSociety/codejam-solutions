# Jerry's Rigged Game

## Problem Statement

The yellow ("Y") party government has given you (a member of the yellow party) the task of drawing up new electorate boundaries. Your job is to draw the boundaries such that they are most favourable for the yellow party in the upcoming electionm against the blue party ("B") (see the GOAL below). You are given a 15x15 grid map to divide into 3 rectangular electorates (they do not have to be of equal size) subject to the following REQUIREMENTS:

- the rectangles must be at least 4 blocks wide and at least 4 blocks tall
- one of the rectangles must begin in the top-left corner of the map and span the whole width of the map (i.e. you must have a top-spanning electorate)
- the electorates must include every point of the grid (no points left out)

Your GOAL is to find an arrangement of rectangles such that:

- have 2 electorates that yellow party wins, and 1 electorate that blue party wins
- maximise the sum of the sizes of the 2 yellow-winning electorates

## Input Format

B,Y,Y,B,B,B,B,Y,B,Y,B,B,B,B,Y;Y,Y,B,Y,B,B,B,B,Y,B,Y,B,B,B,B;B,Y,B,Y,Y,Y,B,Y,B,B,B,Y,Y,B,B;Y,B,B,B,B,Y,Y,B,B,B,Y,B,Y,Y,B;B,B,B,Y,B,Y,Y,B,Y,Y,Y,Y,B,B,Y;Y,Y,B,Y,Y,B,B,B,B,B,Y,B,B,Y,B;Y,Y,Y,Y,Y,B,B,Y,B,B,Y,Y,B,B,Y;B,B,B,B,B,B,Y,Y,Y,B,Y,Y,B,Y,B;B,B,Y,Y,Y,B,B,Y,B,Y,B,B,B,Y,Y;B,Y,Y,B,B,B,Y,Y,Y,B,Y,B,B,B,Y;B,B,B,B,B,Y,Y,Y,B,B,Y,B,B,B,B;Y,Y,Y,Y,Y,Y,B,Y,Y,Y,Y,Y,B,B,Y;Y,Y,B,Y,B,Y,B,B,Y,Y,B,B,Y,B,B;B,Y,Y,Y,Y,Y,Y,Y,B,B,Y,B,B,B,B;B,B,Y,B,Y,B,Y,B,Y,Y,B,Y,Y,B,B

## Constraints

Constraints ... 

## Output Format

[[(0, 0), (9, 14)], [(10, 0), (14, 10)], [(10, 11), (14, 14)]]