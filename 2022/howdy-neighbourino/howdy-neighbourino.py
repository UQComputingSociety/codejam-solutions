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
out = re.sub(r"man", r"fella", out)
out = re.sub(r"Man", r"Fella", out)
# "hello" is replaced by "howdy"
out = re.sub(r"hello", r"howdy", out)
out = re.sub(r"Hello", r"Howdy", out)

sys.stdout.write(out)
