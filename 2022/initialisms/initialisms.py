inp = input()
out = ""

for word in inp.split():
    if word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        out += word[0]
print(out)