# The Accountant

## Problem Statement

Ben Affleck's only gone and done it... After almost assassinating his brother and being caught by the feds, he returned to his slow life of being an accountant. But all that fighting put him on edge in the office. Unable to focus, he would make many mistakes - but some mistakes are too heinous to forgive. Mr Affleck, in his accounting reports, has been misaligning his columns! Separated by dot points (.), he has become known the the Official Accounting Administration Wing of the Government (OAAWG) as a serial whitespace offender... And must be stopped at all costs.

A squad of agents sent to his house discovered it abandoned, with accounting reports containing misaligned data everywhere... This crime against humanity must be repaired. Can you save the accounting reports, and stop the world plunging into economic disaster?

**Your Task**

You will be given a misprinted accounting report containing an item being bought, a series of possibly misprinted .'s, and a final value 

You must also make sure that the sum of the entries of the report balances with the value given at the end!

## Input Format

The report contains three sections: Revenue, Expenses, Total. Each section is separated by 50 '-'s. Each section will have a left column, and a right column (item, price), and wlil have an incorrect number of '.'s padding the two. There are `n_r` entries in `revenue`, and `n_e` entries in `expenses`. See the example down below.

## Constraints

- each section will always be correctly separated by 50 -'s
- 0 < n_r <= 100
- 0 < n_e <= 100
- 0 < price_i <= 10000


## Output Format
The report contains three sections: Revenue, Expenses, Total. Each section is separated by 50 '-'. In `revenue` and `expenses`, the item description (left column) must be left-aligned, and its cost (right colum) right-aligned with respect to the 50 -'s in each section, with dot points (.) filling in the space in between. In `total`, the balance of all the values is printed out, right-aligned with the rest of the costs. See the example down below.

## Sample Input

```
Revenue
--------------------------------------------------
Lotus Seed...................................$6733
Galangal.............................$2449

Expenses
--------------------------------------------------
Chayote...........................$5637
Cucumber.........................$7551
Iceberg....................$2263

Total
--------------------------------------------------
                                            $-6302
```

## Sample Output

```
Revenue
--------------------------------------------------
Lotus Seed...................................$6733
Galangal.....................................$2449

Expenses
--------------------------------------------------
Chayote......................................$5637
Cucumber.....................................$7551
Iceberg......................................$2263

Cost
--------------------------------------------------
                                            $-6269
```

