import queue #can solve this by brute force but might as well try and make it faster

grid = []
size = 71
for i in range(size):
    grid.append([False] * size)

overpath = None
lines = open("2024/18/input.txt").read().splitlines()
for i in range(len(lines)):
    split = lines[i].split(",")
    drop_x, drop_y = [int(c) for c in split]
    grid[drop_y][drop_x] = True

    if overpath != None and not (drop_x, drop_y) in overpath: #if byte wasn't dropped on our path we don't care
        continue

    escape = False
    states = queue.PriorityQueue()
    states.put((0, set(), 0, 0))
    seen = set()
    while not states.empty():
        state = states.get()

        if state[2:] in seen:
            continue
        seen.add(state[2:])

        cost, path, x, y = state

        if x == size - 1 and y == size - 1:
            escape = True
            overpath = path
            break

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            tx = x + dx
            ty = y + dy

            if tx >= 0 and tx < size and ty >= 0 and ty < size and not grid[ty][tx]:
                new_path = set(path)
                new_path.add((tx, ty))
                states.put((cost + 1, new_path, x + dx, y + dy))

    if not escape:
        print(str(drop_x) + "," + str(drop_y))
        break