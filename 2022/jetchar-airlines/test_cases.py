# yayy it's everyone's favourite time when creating a problem
# time to create test cases!!!


import random

CASES = 50
MAX_SUITCASES = 99
MAX_END_TIME = 299

IN_FORMAT = "input{:02d}.txt"
OUT_FORMAT = "output{:02d}.txt"


def JetCharTest(n, suitcases):
    # modified function that takes parameters rather than prompts for input

    # sort by ending time
    suitcases.sort(key=lambda x: x[1])

    current_suitcase_end = -1
    out = 0
    for i in range(n):
        if suitcases[i][0] >= current_suitcase_end:  # suitcase can be stolen
            # earliest ending suitcase that can be stolen
            current_suitcase_end = suitcases[i][1]
            out += 1

    return out


for i in range(45, 51):
    # generate number of suitcases
    n = random.randrange(MAX_SUITCASES)

    inf = open(f"tests/input/{IN_FORMAT.format(i)}", "w")
    outf = open(f"tests/output/{OUT_FORMAT.format(i)}", "w")

    inf.write(f"{n}\n")

    suitcases = []
    for i in range(n):
        # for each suitcase, generate a start time and end time
        start = random.randrange(MAX_END_TIME-1)  # don't start at 299
        end = random.randrange(start+1, MAX_END_TIME)

        suitcases.append((start, end))

        inf.write(f"{start} {end}\n")
    outf.write(str(JetCharTest(n, suitcases)))

    inf.close()
    outf.close()
