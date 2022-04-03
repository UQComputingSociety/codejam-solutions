# Alcohols

## Problem Statement

On a Sunday afternoon, your chemist friend decides to take you out for some alcohol. Disappointingly, they bring you to the UQ chemistry lab and presents you with this problem: 

Alcohol molecules are made of a combination of carbon (C) and hydrogen (H) atoms and hydroxyl (OH) groups. The 'backbone' of the molecule is a chain of carbon atoms numbered 1 to n from left to right, where n is the number of carbons. Each carbon is connected to 1-2 other carbons and 2-3 Hydrogen atoms/hydroxyl groups to have a total of 4 links. The scientists want you to convert the string of atoms to a condensed formula which shows these links E.g. "CH3CH2(OH)" is a molecule with 2 hydrogens and a hydroxyl group linked with carbon at position 2 and 3 hydrogens at carbon position 1.

Given an unordered string of Hydrogen (H), Carbon (C) and Oxygen (O) atoms, and the positional number/s of the hydroxyl group/s, create the condensed formula of the 'straight-chained alcohol molecule' as represented below:

## Input Format

- First line: an unordered string of C's, H's and O's, representative of their respective atoms
- Second line: integers separated by a single space, representing the positional number of the OH group (the carbon position number it is linked to)

**Hackerrank adds a third input 'positions_count'. Please comment out this line.**

## Constraints

- Only one molecule is to be created
- For *n* C's, positions are numbered *1, 2, ..., n* respectively, left to right (no reversals or branches)
- Each carbon can only have 0 or 1 hydroxyl group linked
- If an alcohol molecule can be made but there are atoms (C, H, O) leftover, it is deemed invalid

## Output Format
A string containing the condensed formula (see examples).

## Sample Input

```
CHHCHHHCHHCOHHHOO
1 3 4
```

## Sample Output

```
CH2(OH)CH2CH(OH)CH2(OH)
```
