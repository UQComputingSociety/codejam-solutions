# Horse Code

## Problem Statement

People are starting to get quite suspicious of the horses at the UQ Gatton Campus. They have intercepted some Morse code messages from the stables, but they are riddled with Horse code!

Horse code is quite primitive, and contains these 5 phrases:

- tbh - thoroughbred horse
- smh - shaking my hooves
- gtfo - galloping through fields occasionally
- idc - i don't canter
- btw - big trough of water


Translate a string of Horse code into English

## Input Format

- There is one line of input containing a string of morse code represented by "." and "-". Words are separated by '/' and letters are separated by a space.
- The next 26 lines of input contain string representations of Morse for each letter a-z.

## Constraints

The length of the string is less than 5000 characters

## Output Format
One line containing the decoded message in all lowercase

## Sample Input

```
../.- --/.-/- -... ..../.- -. -../../.-.. .. -.- ./--. - ..-. ---
.-
-...
-.-.
-..
.
..-.
--.
....
..
.---
-.-
.-..
--
-.
---
.--.
--.-
.-.
...
-
..-
...-
.--
-..-
-.--
--..
```

## Sample Output

```
i am a thoroughbred horse and i like galloping through fields occasionally

```

