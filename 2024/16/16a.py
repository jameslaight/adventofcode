import queue #i love priority queues

grid = [[c for c in line] for line in open("2024/16/input.txt").read().splitlines()]

def get(x, y):
    return grid[y][x]

width = len(grid[0])
height = len(grid)

for x in range(width):
    for y in range(height):
        if get(x, y) == "S":
            start_x = x
            start_y = y
        elif get(x, y) == "E":
            end_x = x
            end_y = y

states = queue.PriorityQueue()
states.put((0, start_x, start_y, 1, 0)) #cost, x, y, dx, dy
seen = set()
while states:
    state = states.get()
    cost, x, y, dx, dy = state

    if state[1:] in seen:
        continue
    seen.add(state[1:])    

    if x == end_x and y == end_y:
        print(cost)
        break

    if get(x + dx, y + dy) != "#":
        states.put((cost + 1, x + dx, y + dy, dx, dy)) #step
    states.put((cost + 1000, x, y, dy, -dx)) #clockwise
    states.put((cost + 1000, x, y, -dy, dx)) #anticlockwise