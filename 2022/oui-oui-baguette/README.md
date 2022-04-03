# Oui Oui Baguette

## Problem Statement

The French are known for many things; cheese, wine, guillotines, but also their bizarre way of counting.

Using the following French rules, convert an integer between 0 and 100 into English text:

**Rules:**

1. Numbers 17-19: "ten"-ones e.g. 17 = "ten-seven"
2. Numbers 20-59: tens-ones e.g. 29 = "twenty-nine"
3. Numbers 60-79: sixty-[remainder from 60] e.g. 75 = "sixty-fifteen"
4. Number 80: "four-twenties"
5. Numbers 81-99: "four-twenty"-[remainder from 80] e.g. 96 = "four-twenty-sixteen"

Additionally, numbers in the range 20 to 80 which end in one have the special separator "-and-"

All other numbers should keep their normal English spellings.

## Input Format

- An integer $n$ to be converted to text

## Constraints

$
0 < n \leq 100
$


## Output Format
string: text-based representation of number

## Sample Input

```
96
```

## Sample Output

```
four-twenty-sixteen
```

