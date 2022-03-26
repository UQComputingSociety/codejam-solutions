s = input()
out = ""

for word in s.split():
    if word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        out += word[0]
print(out)
