# Pizza Cooker

## Problem Statement

UQCS (UQ Cooking Society) would like to start making their own cheese pizzas.

They have enlisted the help of UQCS (UQ Cheese Society) and UQCS (UQ Creators of Sauce), who have agreed to supply $c$ blocks of cheese and $s$ bottles of pizza sauce.

The cheapest pizza ingredients can be bought from UQCS (Unnamed Queensland Cheap Supermarket), which is selling pizza bases for $p_b$ dollars each. They are also selling blocks of cheese and bottles of sauce for $p_c$ and $p_s$ dollars each.

- 1 pizza base can be used to make 1 pizza
- 1 block of cheese can be used to make 3 pizzas
- 1 bottle of sauce can be used to make 2 pizzas

A pizza requires all three of these ingredients. Only whole units of each ingredient can be bought, and only whole pizzas can be made.

How many pizzas can UQCS make given a budget of $x$ dollars.

## Input Format

- The first line contains an integer $x$: dollars that UQCS can spend on ingredients
- The second line contains 2 integers $c$ and $s$: the initial supply of cheese and sauce
- The third line contains 3 integers $p_c$, $p_s$, $p_b$: the price of one pizza base, one block of cheese and one bottle of sauce

## Constraints

- $0 \leq x \leq 10^16$
- $1 \leq c,s, p_c, p_s, p_b \leq 100$

## Output Format
One integer for the number of pizzas that can be made

## Sample Input

```
100
5 50
7 5 1
```

## Sample Output

```
39
```

## Explanation

- We begin with an initial supply of 5 blocks of cheese and 50 bottles of sauce.
- We buy 8 blocks of cheese (for 7 dollars each) and 39 pizza bases (for 1 dollar each)
- The remaining budget is
- Our total suppy is now 13 blocks of cheese, 50 bottles of sauce, and 39 pizza bases.
- This allows us to make 39 pizzas