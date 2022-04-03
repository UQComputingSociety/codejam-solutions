# Howdy Neighbourino

## Problem Statement

Ned Flanders is a character from The Simpsons, with a very distinctive style of speech. You'll need to apply these rules to Ned Flanders-ise the given text:

- Words ending in 'h' have "aroo" appended to them: e.g. "torch" -> "torcharoo"
- Words with at least 5 letters ending in 'r' have "ino" appended to them: e.g. "farmer" -> "farmerino". 
- Words ending in 'd' (**except "and"**) have "ily-doodily" appended to them: e.g. "feed" -> "feedily-doodily"
- Words ending in "es" have "ies" appended to them: e.g. "mules" -> "mulesies"
- Words beginning with 'd' have "diddly ding dong" prepended to them: e.g. "dog" -> "diddly ding dong dog"
- Words beginning with 'n' have "noodly-" prepended to them: e.g. "night" -> "noodly-night"
- Words beginning with 'r' have "riddly-" prepended to them: e.g. "right" -> "riddly-right"
- "man" is replaced by "fella" - **note that variations should still be replaced, i.e. man's**
- "hello" is replaced by "howdy"
- Replacing or prepending to the start of a capitalised word must move the capitalisation: e.g. "Dog" -> "Diddly ding dong dog"
- A word can have multiple translations applied to it.

## Input Format

Plain ascii text

## Constraints

No newlines (or other control characters) will be present in the input.

## Output Format
Plain ascii text

## Sample Input

```
The birch canoe slid on the smooth planks.
```

## Sample Output

```
The bircharoo canoe slidily-doodily on the smootharoo planks.
```
