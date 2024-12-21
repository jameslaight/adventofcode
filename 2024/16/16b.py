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
states.put((0, ((start_x, start_y),), start_x, start_y, 1, 0)) #cost, path, x, y, dx, dy
seen = set()
pending_seen = set()
highest_cost = 0 #pending_seens is pushed to seen every time highest_cost rises
finish = False
traversed = set()
while not states.empty():
    state = states.get()
    cost, path, x, y, dx, dy = state

    if cost > highest_cost:
        if finish:
            break

        highest_cost = cost
        seen = seen.union(pending_seen)

    if state[2:] in seen:
        continue
    pending_seen.add(state[2:])

    if x == end_x and y == end_y:
        for p in path:
            traversed.add(p)

        finish = True
        continue

    if get(x + dx, y + dy) != "#":
        appended_path = path + ((x + dx, y + dy),)
        states.put((cost + 1, appended_path, x + dx, y + dy, dx, dy)) #step
    states.put((cost + 1000, path, x, y, dy, -dx)) #clockwise
    states.put((cost + 1000, path, x, y, -dy, dx)) #anticlockwise

print(len(traversed))