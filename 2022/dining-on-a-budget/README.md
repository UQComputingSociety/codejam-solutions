# Dining On A Budget

## Problem Statement

Imagine you sit down at restaurant, after a long day of uni for dinner. You are absolutely starving for a meal (in fact you are so starving that you want 2 items off the menu) after enduring a brutal day of back-to-back letures. The problem is, you only have a certain amount of money in your account.

In order stretch your budget as far as possible, your task is to find all the possible sets of 2 food items off of the given menu whose prices sum exactly to a certain budget number.
(e.g. If your budget is $20, you need to find all the sets of 2 dishes, dish_a and dish_b, such that dish_a_price + dish_b_price = 20)

The input for your program is the menu and a SUM_TO value (in the format shown below), and the output should be a list of pairs of names of 2 menu items, whose values sum exactly to the given budget/SUM_TO value (see output format below).

IMPORTANT NOTES FOR YOUR OUTPUT:

- In each pair of menu items, the cheaper item must be first in the pair
- The final list of pairs that you output should be sorted alphabetically (A-first, Z-last) (i.e like ```avocado on toast,hot pot;baguette,goulash```, and not like ```baguette,goulash;avocado on toast,hot pot```)

## Input Format

SUM_TO,18;pancakes,2;chai latte,4;wonton soup,14;beef casserole,22;cappuccino,9

## Constraints

* The given menu will always have 1 or more item
* There will always be at least one pair of menu items that sums to the given budget

## Output Format
chai latte,wonton soup;cookie,avocado on toast;muffin,green tea
