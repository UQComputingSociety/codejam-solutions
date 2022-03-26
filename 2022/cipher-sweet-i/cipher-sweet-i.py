def caesar(n: int, pt: str) -> str:
    """
    Takes the plaintext `pt` and outputs the encrypted ciphertext, rotated
    by `n` characters.
    """

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()

    ct = ""
    for c in pt:

        if c.isalpha():
            if c.upper() == c:
                ct += upper[(ord(c) - ord('A') + n) % 26]
            else:
                ct += lower[(ord(c) - ord('a') + n) % 26]
    return ct
   

if __name__ == "__main__":

    rotation = int(input())
    plaintext = input()

    print(caesar(rotation, plaintext))