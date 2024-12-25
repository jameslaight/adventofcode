grid = []

for line in open("2024/20/input.txt").read().splitlines():
    grid.append(line)

width = len(grid[0])
height = len(grid) #how many times we gonna do this

def get(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        return grid[y][x]
    else:
        return "#"

def flood(x, y):
    heats = []
    for _ in range(height):
        heats.append([-1] * width)

    queue = [(0, x, y)]
    while queue:
        heat, x, y = queue.pop(0)

        if heats[y][x] != -1: #already seen
            continue

        heats[y][x] = heat

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            tx = x + dx
            ty = y + dy

            if get(tx, ty) != "#":
                queue.append((heat + 1, tx, ty))

    return heats

for y in range(height):
    for x in range(width):
        if get(x, y) == "S":
            sx = x
            sy = y
        elif get(x, y) == "E":
            ex = x
            ey = y

sheat = flood(sx, sy)
eheat = flood(ex, ey)

honourable = sheat[ey][ex]
good = 0
for y in range(height): #gonna find all .#. patterns (possibly changing direction)
    for x in range(width):
        if get(x, y) == "#":
            continue

        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for dx, dy in dirs:
            tx = x + dx
            ty = y + dy

            for d2x, d2y in dirs: #looking at the input i don't think this is needed, but completeness :>
                t2x = tx + d2x
                t2y = ty + d2y

                if get(tx, ty) == "#" and get(t2x, t2y) != "#": #if is shortcut
                    distance = sheat[y][x] + 1 + eheat[t2y][t2x]

                    if distance <= honourable - 100:
                        good += 1

print(good)