def JetChar():
    # greedy algorithm problem.

    n = int(input())

    # parse input and store in (start, end) format in a list
    suitcases = []
    for _ in range(n):
        start, end = map(int, input().split())
        suitcases.append((start, end))

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
