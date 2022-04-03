# Day Of The Caesar (Cipher II)

## Problem Statement

You're under attack! Your box fortress is being swarmed by greedy little, hypo-intelligent delivery men! A message must be relayed to your A.S.S (American Shipping Services) army generals, but you mustn't let the delivery men intercept your plans...

In the haste of battle you conjure up a cipher which will surely leave your opponents baffled. A cipher as old as time itself (citation needed), from the ancient Romans, is what you find in your notes - a cipher pertaining to one "Julias Caesar". Quickly implement it and encrypt the secret messages to ensure the security of your battle plans!

https://en.wikipedia.org/wiki/Caesar_cipher

## Input Format

Two lines, the first containing the rotation number n, and the second being the plaintext string s.

## Constraints

0 < len(s) < 1000

0 <= n < 26

## Output Format
A single line containing the encrypted plaintext, rotated by n. Any character that is not a letter (e.g. whitespace, $, \*, ...) must be preserved.

E = (x + n) mod 26

## Sample Input

```
3
banana
```

## Sample Output

```
edqdqd
```

## Explanation

"banana" is the input word, and each letter is rotated by 3 characters to produce "edqdqd"

