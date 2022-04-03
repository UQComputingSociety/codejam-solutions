# Day Of The Trifids (Cipher IV)

## Problem Statement

**Scenario**

The triffids have started attacking, and it seems they have one weakness... the Trifid cipher!!!! You must implement it so you can communicate without all those evil plants knowing how to defeat you...

**Task**

You must implement a [Trifid Cipher](https://en.wikipedia.org/wiki/Trifid_cipher). The cipher works by forming 3 squares, formed from the key. These squares are then used to get indices for letters of the plain-text message, which are then placed in their own squares, and substituted back into the encryption squares. Because that description is nowhere near sufficient, more specific details about the algorithm can be found here:

- http://practicalcryptography.com/ciphers/classical-era/trifid/
- https://en.wikipedia.org/wiki/Trifid_cipher
- https://cryptii.com/pipes/trifid-cipher

## Input Format

Two lines, the first being the key `k`, and the second the message to encrypt, `m`

## Constraints

- `len(k) == 27`
- `k` contains every letter of the alphabet, plus a single `.` (NOTE: `.` instead of `+`, which Wikipedia has)
- block size of 5
- `0 < len(m) <= 100`
- `m` contains no special characters (except for single spaces between words - see examples)


## Output Format
A single line containing the Trifid encrypted message

## Sample Input

```
XBQFKDJHVGELMONPCRS.UIWAYZT
BOY COMING UP WITH SENTENCES IS KINDA HARD
```

## Sample Output

```
DMROK CCMXU RUN.H WIDBZ OZSCG UGOEV UEACT
```
