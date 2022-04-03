x = 0

def reversort(L):
    global x
    for i in range(len(L)):
        j = i + 1 + min(enumerate(L[i:]), key=lambda x: x[1])[0]

        x += j - i
        L[i:j] = L[i:j][::-1]
        # print(i, j, L)
    return L

T = int(input())
for t in range(T):
    N = int(input())
    L = [int(x) for x in input().split()]
    # print(L)
    x = -1
    (reversort(L))
    print('Case #' + str(t+1) + ':', x)