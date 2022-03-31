
def condensed_formula(chain: str, positions: list) -> str:
    """Converts a string of carbon, hydrogen and oxygen atoms to an alcohol condensed formula.

    Args:
        chain (str): length of chain
        positions (list): array of positions
    """
    #chain = input()
    #positions = list(map(int, input().rstrip().split()))

    c = 0
    h = 0
    x = 0

    new_arr = []

    for el in chain:
        if el == "C":
            c += 1
        elif el == "H":
            h += 1
        elif el == "O":
            x += 1
        else:
            return "invalid"

    # test edge cases:
    # check if there are any oxygens
    if ((x == 0) or (c == 0) or (h == 0)):
        return "invalid"

    # check if each position is valid:
    for num in positions:
        if (num == 0):
            return "invalid"
        elif (num > c):
            return "invalid"

    if (len(positions) <= c):
        if (h != (2*c + 2)):
            return "invalid"
        for i in range(c):
            if (i == 0 or i == c-1):
                new_arr.append("CH3")
            else:
                new_arr.append("CH2")

        for num in positions:
            if "(OH)" in new_arr[num-1]:
                return "invalid"
            if (num == 1 or num == c):
                new_arr[num-1] = "CH2(OH)"
            elif num-1 > c:
                return "invalid"
            else:
                new_arr[num-1] = "CH(OH)"

        return "".join(new_arr)
    return "invalid"

if __name__ == "__main__":

    chain = input()
    positions = list(map(int, input().rstrip().split()))

    print(condensed_formula(chain, positions))