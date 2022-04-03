# Initialisms

## Problem Statement

After arguing with your friend about the difference between acronyms, initialisms, and abbreviations, you create an initialism converter to educate them. An initialism is a type of abbreviation in which the first letter of each word in a phrase is pronounced separately. For example, `FBI` is an initialism of the `Federal Bureau of Investigation`. Words that do not start with a capital letter (e.g. `of`) are ignored and do not contribute to the initialism. Any symbols that aren't letters are also ignored. For words with multiple capital letters (e.g. `McDonald's`), only the first capital letter is used in the initialism.

You are given a string and your task is to convert it to its initialism.

## Input Format

A single line containing the string to be converted into an initialism, $s$.

## Constraints

$0 < len(s) < 10^3$

## Output Format
A single line containing the initialism as a string.

## Sample Input

```
Federal Bureau of Investigation
```

## Sample Output

```
FBI
```

