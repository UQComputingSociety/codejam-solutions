from dataclasses import dataclass
from collections import defaultdict
from typing import Set

@dataclass
class State:
    c: str
    n: int

    def __hash__(self) -> int:
        return id(self)

class Node:
    def __init__(self, val: str=None, prev: 'Node'=None, next: 'Node'=None):
        self.val = val
        self.prev = prev
        if prev:
            prev.next = self
        self.next = next
        if next:
            next.prev = self

    def insert_right(self, val):
        return Node(val, self)

    def __str__(self):
        x = [self]
        while x[-1].next:
            x.append(x[-1].next)
        return str([y.val for y in x])

J = 'J'
C = 'C'
Q = '?'

# x = Node(1)
# print(x)
# x.insert_right(100)
# print(x)

T = int(input())
for t in range(T):
    X, Y, S = input().strip().split()
    X, Y = int(X), int(Y)

    costs = defaultdict(int, {'CJ': X, 'JC': Y})

    x = 0

    blanks: Set[Node] = set()
    s = S
    # maps indices to the number of letters adjacent and left of that index
    # e.g. S = "CJJJ", C_left = [0, 0, 0, 0], J_left = [0, 0, 1, 2]
    l = head = Node(s[0])
    if l.val == Q: blanks.add(l)
    for c in s[1:]:
        if c == l.val:
            pass # don't add duplicate characters
        else:
            x += costs[l.val + c]
            l = l.insert_right(c)
            if l.val == Q: blanks.add(l)
    # print(head)
    # print(blanks)


    # print(costs)
    while True:
        node: Node = next(iter(blanks), None)
        if node is None: break
        # print(head)
        blanks.remove(node)

        min_change = float('inf')
        min_c = None
        for c in 'JC':
            change = 0
            if node.next:
                change += costs[c + node.next.val]
            if node.prev:
                change += costs[node.prev.val + c]

            if change < min_change:
                min_c = c
                min_change = change

        x += min_change
        node.val = min_c
    # print(head)


    print('Case #' + str(t+1) + ':', x)