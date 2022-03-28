
import random   # use random to test random lol

from rnjesus import rnjesus, count

in_format = "input{:02d}.txt"       # e.g. input00.txt
out_format = "output{:02d}.txt"     # e.g. output00.txt


NO_CASES = 50
r = 3.7783

for c in range(NO_CASES):

    x_0 = random.random()
    min = random.randint(0, 100)        
    max = random.randint(min, 1000)     
    n = random.randint(0, 100)

    inf = open(f"tests/input/{in_format.format(c)}", 'w')
    outf = open(f"tests/output/{out_format.format(c)}", 'w')

    inf.write(f"{x_0} {min} {max} {n}\r\n")

    for _ in range(n):

        outf.write(str(round(rnjesus(x_0, r, min, max), 5)) + "\r\n")

    inf.close()
    outf.close()


