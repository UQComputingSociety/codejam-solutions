# Day Of The Rail (Cipher III)

## Problem Statement

Given a plaintext string and a number of rails, implement a [rail \[fence\]cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher)
Your task differs from the wikipedia article in that the "fence" should start in the bottom left instead of the top left. For example, given the plaintext "some plaintext.", a typical intermediate ciphertext (intermediate because it's not quite the ciphertext, but further along than plaintext) would be:

```code
s*** ***i***x**
*o*e*p*a*n*e*t*
**m***l***t***.
```
but the way required for this challenge is

```code
**m***l***t***.
*o*e*p*a*n*e*t*
s*** ***i***x**
```

## Input Format

`number_of_rails`|`plaintext`

## Constraints

2 <= `number_of_rails` <= 30

There will never be an asterisk (*) in the plaintext, so that's a safe character to use as a placeholder.

## Output Format
some permutation of the plaintext, "encrypted" in modified-rail-cipher fashion

## Sample Input

```
9|Trust me. Hey, Alan. What are you, uh, what are you doing back there, man?
```

## Sample Output

```
.thgne a wan a?mHha tibm eWr, oa ty ehadc,s,. ur keu ny eu rrAao, oteTluyh
```
