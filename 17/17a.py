import queue

file = open("17/input.txt")
grid = [[int(i) for i in j] for j in file.read().splitlines()]
width = len(grid[0])
height = len(grid)
file.close()

start = (0, 0)
end = (width - 1, height - 1)

states = queue.PriorityQueue() #format: (heat, (x_pos, y_pos), (x_dir, y_dir), consecutive_steps)
states.put((0, start, None, 0)) #initial state
seen = set()

while not states.empty():
    state = states.get()

    if state[1:] in seen:
        continue
    seen.add(state[1:])

    heat = state[0]
    x_pos = state[1][0]
    y_pos = state[1][1]
    drc = state[2]
    steps = state[3]

    if x_pos == end[0] and y_pos == end[1]:
        print(heat)
        break

    if drc != None:
        dirs = []
        x_dir = drc[0]
        y_dir = drc[1]

        dirs.append((y_dir, -x_dir))
        dirs.append((-y_dir, x_dir))

        if steps < 3:
            dirs.append(drc)
    else: #any dir to begin
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for drc_new in dirs:
        x_new = x_pos + drc_new[0]
        y_new = y_pos + drc_new[1]

        if x_new < 0 or x_new >= width or y_new < 0 or y_new >= height:
            continue

        heat_new = heat + grid[y_new][x_new]
        if drc_new == drc:
            steps_new = steps + 1
        else:
            steps_new = 1

        states.put((heat_new, (x_new, y_new), drc_new, steps_new))