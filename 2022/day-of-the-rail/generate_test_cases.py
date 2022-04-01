from random import randint

from rail import encode

in_format = "input{:02d}.txt"       # e.g. input00.txt
out_format = "output{:02d}.txt"     # e.g. output00.txt


excerpts = [
    "Many cats cannot properly digest cow's milk. Milk and milk products give them diarrhea. (from catfact.ninja)",
    "Pim, can we watch something else? No, shh. It's about to get really good. It's about to get really good.",
    "Trust me. Hey, Alan. What are you, uh, what are you doing back there, man?",
    "Although it seems like it's all crashing down I just want to ride my bike",
    "Through all the bullshit with the wind in my face Miss me with that nonsense",
    "I'm Mr. Frog. This is my show.  I ate the bug.",
    "[ Bug screams ] I ate the bug. This is the end.",
    "Would you like a peanut?  No, I'm all good, man.  Uh, my grandma actually passed on from eating a peanut",
    "I wanna be the very best Like no one ever was To catch them is my real test To train them is my cause",
    "Pokémon! Gotta catch 'em all! (A heart so true) Our courage will pull us through You teach me and I'll teach you Pokémon! Gotta catch'em all (gotta catch 'em all!)"]

for c, excerpt in enumerate(excerpts):

    rails = randint(2, 30)

    inf = open(f"tests/input/{in_format.format(c)}", 'w')
    outf = open(f"tests/output/{out_format.format(c)}", 'w')

    inf.write(f"{rails}|{excerpt}\n")

    outf.write(str(encode(rails, excerpt)))

    inf.close()
    outf.close()


