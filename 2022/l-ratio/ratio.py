from typing import List
import sys

def print_ratios(front:  List[int], rear: List[int]):
    for i, f in enumerate(front):
        print(i + 1, ":", sep="", end=" ")
        print([round(f / r, 2) for r in rear], sep=", ")

def main():
    # the following is used instead of input() because input() ends when it reads newlines.
    lines = sys.stdin.read().splitlines()
    front = [int(elem) for elem in lines[1].split(" ")]
    rear = [int(elem) for elem in lines[2].split(" ")]
    print_ratios(front, rear)

if __name__ == "__main__":
    main()
