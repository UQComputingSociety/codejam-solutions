# Based64

## Problem Statement

The bro on the corner said they were selling encoding algorithms. The menu was pretty good:

1. [Yiew Yiew Encoding](https://en.wikipedia.org/wiki/Uuencoding) ........ $3
2. [MEME encoding](https://en.wikipedia.org/wiki/MIME)            ........ $1
3. [Mos Def](https://en.wikipedia.org/wiki/MOS_Technology_file_format) ........ $4

But the bro whispered and said that if I followed them down the corridor, they'd lead me to where the real special encoding algorithms are. Mentioned something about a Based64. Idk what that means bro.

Based64 is an algorithm that follows from [Base64](https://en.wikipedia.org/wiki/Base64). The encoding process is the same, with the only difference being that some of the characters you map to are emojified!

The list of symbols (in numerical order) is given in `constraints` as `mapping_array`, and the padding character is given in `constraints` as `padding_character`. Use these, and the base64 specification, to implement your own based64.

## Input Format

A single string, s, to be encoded

## Constraints

0 < len(s) <= 1000

mapping_array: \['A','B','C',':D','E','F','G','>:DD','I','J','K',':33','M','N','O','P','Q',';)','S','T','U',':oo','W','X','Y','Z','a','b','c','d','-.-','f','g',":'((",'i','j','k','l',':cc','n','o','p','q',':?','s','t','u','v','w','@.@','y','z','0','1',':L','3','4','5','8==D','7','8','9','69','M.M'\]

padding_character: "O.O"

Hackerrank. Apparently emojis themselves aren't allowed as input here, so we have to settle for ASCII-based emojis instead ://


## Output Format
Single line containing the Based64 encoded string

## Sample Input

```
Just tell me it's real, just tell me it's real
```

## Sample Output

```
Sn:oozdCB0ZW@.@sIG1lIGl0J3Mgc:cc:oo:'((bCwgan:oozdCB0ZW@.@sIG1lIGl0J3Mgc:cc:oo:'((bAO.OO.O
```
