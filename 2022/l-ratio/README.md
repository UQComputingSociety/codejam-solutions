# l + ratio

## Problem Statement

For a front cog with f teeth and a rear cog with r teeth, the gear ratio is defined to be f / r.
Remember, cyclists are mostly normal people who start counting at 1, not 0.

## Input Format

f<sub>n</sub>, r<sub>k</sub>

f<sub>1</sub>, f<sub>2</sub>, ..., f<sub>n</sub>

r<sub>k</sub>, r<sub>k-1</sub>, ..., r<sub>1</sub>

## Constraints

$f_n \in [1, 2, ..., 9]$
$r_k \in [1, 2, ..., 20]$

Front teeth counts are given in ascending order, but rear teeth counts are given in descending order. This isn't to make your life harder, it's to mimic how a bike works.

There should be one $f_n$ lines of output.
On each line, there should be:

 1. a single digit representing the front cog number
 2. a colon, then a space ": "
 3. $r_k$ ratios, wrapped in brackets [] and separated by a comma and a space ", "
 
 The ratios should be rounded to two decimal places, but if it can be represented exactly with one decimal place, give it just one (this is how python's inbuilt round() function works)


## Output Format
1: [ratio_1, ..., ratio_k]

...

n: ...


## Sample Input

```
1 1
44
16
```

## Sample Output

```
1: [2.75]
```

## Explanation

Fixed gear bicycle with one front cog and one rear cog. The front cog has 44 teeth and the rear cog has 16 teeth. This results in a gear ratio of 2.75, meaning one revolution of the front cog will result in 2.75 revolutions of the rear cog.
