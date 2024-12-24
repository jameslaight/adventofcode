import queue

grid = []
size = 71
for i in range(size):
    grid.append([False] * size)

lines = open("2024/18/input.txt").read().splitlines()
for i in range(1024):
    split = lines[i].split(",")
    x, y = [int(c) for c in split]
    grid[y][x] = True

states = queue.PriorityQueue()
states.put((0, 0, 0))
seen = set()
while not states.empty():
    state = states.get()

    if state[1:] in seen:
        continue
    seen.add(state[1:])

    cost, x, y = state

    if x == size - 1 and y == size - 1:
        print(cost)
        break

    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        tx = x + dx
        ty = y + dy

        if tx >= 0 and tx < size and ty >= 0 and ty < size and not grid[ty][tx]:
            states.put((cost + 1, x + dx, y + dy))