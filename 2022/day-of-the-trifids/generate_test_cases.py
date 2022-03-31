
import random  

import day_of_the_trifids

in_format = "input{:02d}.txt"       # e.g. input00.txt
out_format = "output{:02d}.txt"     # e.g. output00.txt

sentences = [
    "HOW ARE YOU TODAY",
    "BOY COMING UP WITH SENTENCES IS KINDA HARD",
    "WOULDNT IT BE NICE IF THE WORLD HAD NO PUNCTUATION",
    "THE BEATLES BEAT THE STONES",
    "SHORT",
    "BLAHAJ",
    "A",
    "HOW DO YOU DO.",
    "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
    "HOMER SIMPSON"
]

alphas = [
    "ZYXWVUTSRQPONMLKJIHGFEDCBA.",
    "XBQFKDJHVGELMONPCRS.UIWAYZT",
    "BXRGKLJPVFEDUOYHCQZ.MIWANST"
]

NO_CASES = len(sentences)

for c in range(NO_CASES):

    x_0 = random.random()
    min = random.randint(0, 100)        
    max = random.randint(min, 1000)     
    n = random.randint(1, 100)

    inf = open(f"tests/input/{in_format.format(c)}", 'w')
    outf = open(f"tests/output/{out_format.format(c)}", 'w')

    sentence = sentences[c]
    key = alphas[c % 3]

    inf.write(f"{key}\r\n{sentence}\r\n")

    outf.write(f"{day_of_the_trifids.day_of_the_trifids(key, sentence.replace(' ', ''))}\r\n")

    inf.close()
    outf.close()


