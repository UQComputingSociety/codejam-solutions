# Huge Lunch

## Problem Statement

UQ has 10 sausage sizzle locations that are all giving away sausages for free.

![image](https://s3.amazonaws.com/hr-assets/0/1647755858-fff1681bd6-Screenshot2022-03-18at17-27-05UQStLucia-EventandBBQsitesmap-01-st-lucia-event-bbq-site-mappdf-min.png)

You are given the travel times between each location (in minutes).

Upon arriving at UQ lakes bus stop, you are given the initial supply of sausages at each location.

Some locations are more efficient than others, but they are all very consistent. Each location has a rate $r$ describing the number of sausages given away per minute.

You are very persuasive, so once you arrive at a location, you can convince the people running the sausage sizzle to give you all of their remaining supply. (This exchange happens in no time at all)

Find the maximum number of sausages you can take.

## Input Format

- The first 11 lines contain 11 integers, forming a 2d matrix containing the fastest travel times to and from each location. The first row and column of the matrix $T$ are the travel times to and from the bus stop.
- The next line contains 10 integers $s_1, \ldots, s_{10} $: the initial supply of sausages at each location
- The next line contains 10 integers $r_1, \ldots, r_{10} $: the rate which sausages are being given away at each location

## Constraints

- $1 \leq T_{i, j} \leq 50$
- $T_{i, j} = T_{j, i}$
- $0 \leq s_i \leq 1000$
- $1 \leq r_i \leq 10$

## Output Format
One integer: the maximum number of sausages that can be taken

## Sample Input

```
0 18 8 16 20 24 11 16 16 20 11
18 0 10 10 14 18 9 2 3 9 10
8 10 0 11 15 19 6 8 10 15 7
16 10 11 0 4 8 5 12 13 5 6
20 14 15 4 0 4 9 16 17 7 9
24 18 19 8 4 0 13 20 21 10 13
11 9 6 5 9 13 0 9 11 9 1
16 2 8 12 16 20 9 0 2 11 10
16 3 10 13 17 21 11 2 0 12 12
20 9 15 5 7 10 9 11 12 0 10
11 10 7 6 9 13 1 10 12 10 0
20 30 40 0 0 0 0 0 0 0
1 2 3 1 1 1 1 1 1 1
```

## Sample Output

```
16
```

## Explanation

The initial supply at each locaiton is

- location 1: 20

- location 2: 30

- location 3: 40 

with all other locations having 0 supply

The optimal route is: bus stop -> 2 -> 1

It takes 8 minutes to travel from the bus stop to location 2.

Upon arriving at location 2, the supply at each location is

- location 1: $20 - 8 = 12$

- location 2: $30 - 16 = 14$

- location 3: $40 - 24 = 16$

You take the remaining 14 sausages from location 2 and travel to location 1

It then takes 10 minutes to travel from location 2 to 1

Upon arriving at location 2, the supply at each location is

- location 1: $12 - 10 = 2$ 

- location 2: $0$

- location 3: $0$

You take the remaining 2 sausages from location 1.

Location 3 has run out of sausages, so your journey ends here with a total of 16 sausages