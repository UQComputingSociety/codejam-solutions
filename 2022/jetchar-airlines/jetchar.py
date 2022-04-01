
def JetChar(items, numPeople):
    d = float(7)
    n = numPeople
    s = 0

    items = items.split(" ")
    #print(items)
    # Convert items list to the number of characters in each
    char_nums = []
    for i in range(len(items)):
        char_nums.append(len(items[i]))

    items = char_nums
    #print (items)
    weighted = []
    # Determine the average item value
    for el in items:
        f = el/d
        s+= f
        weighted.append(f)

    avg_weight = s/n

    els = []
    for i in range(n):
        els.append(0)

    weighted.sort()
    new_items = weighted

    while (len(new_items) > 0):
        els.sort()
        els[0] += (new_items[len(new_items)-1])
        del new_items[len(new_items)-1]

    els.sort()
    #print(els)
    if (els[n-1] > 7):
        return(-1)
    else:
        return (els[0])

if __name__ == "__main__":
    items = input("Enter items: ")
    people = int(input("Enter number of people: "))

    print(JetChar(items, people))