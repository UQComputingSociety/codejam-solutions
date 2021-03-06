import re
import sys

n = 0

text = sys.stdin.read()

# Words ending in 'h' have "aroo" appended to them
out = re.sub(r"(\w+h)\b", r"\g<1>aroo", text)
# Words ending in 'r' have "ino" appended to them
out = re.sub(r"(\w+[a-zA-Z]{3}r)\b", r"\g<1>ino", out)
# Words ending in 'd' have "ily-doodily" appended to them
out = re.sub(r"(\w+(?<!an)d)\b", r"\g<1>ily-doodily", out)
# Words ending in "es" have "ies" appended to them
out = re.sub(r"(\w+es)\b", r"\g<1>ies", out)

# Words beginning with 'd' have "diddly ding dong" prepended to them
out = re.sub(r"\b((?<!-)d|D)(\w+)", r"\g<1>iddly ding dong d\g<2>", out)
# Words beginning with 'n' have "noodly-" prepended to them
out = re.sub(r"\b((?<!-)n|N)(\w+)", r"\g<1>oodly-n\g<2>", out)
# Words beginning with 'r' have "riddly-" prepended to them
out = re.sub(r"\b((?<!-)r|R)(\w+)", r"\g<1>iddly-r\g<2>", out)

# "man" is replaced by "fella"
out = re.sub(r"\bman(\b|\')", r"fella\g<1>", out)
out = re.sub(r"\bMan(\b|\')", r"Fella\g<1>", out)
# "hello" is replaced by "howdy"
out = re.sub(r"\bhello(\b|\')", r"howdy\g<1>", out)
out = re.sub(r"\bHello(\b|\')", r"Howdy\g<1>", out)

sys.stdout.write(out)
