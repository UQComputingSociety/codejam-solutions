from typing import List

def print_ratios(front:  List[int], rear: List[int]):
    for i, f in enumerate(front):
        print(i + 1, ":", sep="", end=" ")
        print([round(f / r, 2) for r in rear], sep=", ")

def main():
    #TODO get input
    front = []
    rear = []
    print_ratios(front, rear)
    """
    print_ratios([30, 40, 50], [30, 27, 25, 22, 20, 15, 10])
    print_ratios([38, 48], [30, 27, 25, 18, 15, 12])
    print_ratios([44], [16])
    """

if __name__ == "__main__":
    main()
