from enum import Enum, auto
from typing import Tuple

class Direction(Enum):
    UP = auto() # auto-assign whatever integer to it, don't care.
    DOWN = auto()

# I DONT KNOW HOW TO WRITE GENERATORS, THIS IS A PRIME CASE FOR THEM
def next_head_pos(nr: int, current: int, dir: Direction) -> Tuple[int, Direction]:
    if dir == Direction.DOWN:
        if current == nr - 1:
            return (current - 1, Direction.UP)
        else:
            return (current + 1, Direction.DOWN)
    elif dir == Direction.UP:
        if current == 0:
            return (current + 1, Direction.DOWN)
        else:
            return (current - 1, Direction.UP)
    else:
        # scuffed error checking lol
        raise AssertionError("invalid args to next_head_pos")
        return (69, Direction, Direction.DOWN)

if __name__ == "__main__":

    line = input().split(",")
    num_rails, plaintext = int(line[0]), line[1]

    cols = [["." for i in range(num_rails)] for j in range(len(plaintext))]

    # think of head like a "write head", i.e. where stuff is being written currently.
    head = (num_rails, Direction.UP)

    for i, col in enumerate(cols):
        head = next_head_pos(num_rails, *head)
        col[head[0]] = plaintext[i]

    # uncomment this block to get a visual representation of the rail fence
    """
    for r in range(num_rails):
        for c in range(len(plaintext)):
            print(cols[c][r], end="")
        print()
    """
    for r in range(num_rails):
        for c in range(len(plaintext)):
            if (t := cols[c][r]) != '.': # uses the controversial assignment expression from PEP 572
                print(t, end="")
    print()

