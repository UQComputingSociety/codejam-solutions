import queue
import sys


def neighbours(coord: "tuple[int, int]") -> "tuple[tuple[int, int], ...]":
    y, x = coord

    output = [cell for cell in ((y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)) if cell[0] in range(0, 20) and cell[1] in range(0, 20)]

    output = [cell for cell in output if grid[cell[1]][cell[0]] != "-"]
    return output


def heuristic(coord: "tuple[int, int]", goal: "tuple[int, int]") -> "int":
    yc, xc = coord
    yg, xg = goal

    return abs(xc - xg) + abs(yc - yg)


input = sys.stdin.read()

grid = [row.split(",") for row in input.split("\n")]

start = [(x, y) for x in range(0, 20) for y in range(0, 20) if grid[y][x] == '1'][0]
end = [(x, y) for x in range(0, 20) for y in range(0, 20) if grid[y][x] == '2'][0]

search_frontier = queue.PriorityQueue()
search_frontier.put((0, start))

path_so_far = {start: None}
cells_so_far = {start: 0}

while not search_frontier.empty():
    _, current = search_frontier.get()

    if current == end:
        break

    for cell in neighbours(current):
        new_cost = cells_so_far[current] + 1

        if cell not in cells_so_far or new_cost <= cells_so_far[cell]:
            cells_so_far[cell] = new_cost
            search_priority = new_cost + heuristic(cell, end)
            search_frontier.put((search_priority, cell))
            path_so_far[cell] = current

answer = []
x = end
while x != start:
    answer += [x]
    x = path_so_far[x]
answer += [start]
answer.reverse()

sys.stdout.write(str(answer)[1:-1].replace(' ', ""))