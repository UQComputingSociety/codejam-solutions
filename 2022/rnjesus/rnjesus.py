
count = 1 # n = 1 initially, start here every iteration - memoryless sequence generation

def logistic_map(x: float, r: float) -> float:
    """
    computes the next value of the logistic_map given the current value `x`
    """

    return r * x * (1 - x)

def rnjesus(seed: float, r: float, min: float = 0, max: float = 1) -> float:
    """
    generate a random number between `min` and `max`, with seed `seed`
    """
    global count

    x = seed

    for n in range(count):

        x = logistic_map(x, r)

    count += 1
    return min + (max - min) * x

if __name__ == "__main__":
    line = input("").split()

    seed, min, max, n = float(line[0]), float(line[1]), float(line[2]), int(line[3])

    r = 3.7783

    for i in range(n):

        print(round(rnjesus(seed, r, min, max), 5))
