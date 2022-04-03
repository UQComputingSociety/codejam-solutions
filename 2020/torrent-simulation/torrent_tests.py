
import random

def make_test():
    N = 10
    P = 9
    print(N)
    print(P)
    pieces = list(range(P)) + list(range(P)[:3])*2
    
    N2 = 4
    assert N2 * P >= len(pieces)

    computers = [set() for x in range(N2)]
    while pieces:
        p = pieces.pop()
        random.choice([c for c in computers if p not in c]).add(p)

    computers.extend(set() for x in range(N - N2))

    # for c in random.sample(computers, 5):
    #     c.update(range(P))

    random.shuffle(computers)
    for c in computers:
        print(' '.join(str(x) for x in c))


if __name__ == "__main__":
    make_test()