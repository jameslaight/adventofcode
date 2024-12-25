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
max_cheat = 20
for y in range(height): #well this got harder
    for x in range(width):
        for dy in range(-max_cheat, max_cheat + 1):
            for dx in range(-max_cheat, max_cheat + 1):
                cheat_distance = abs(dx) + abs(dy)
                if cheat_distance > max_cheat:
                    continue

                tx = x + dx
                ty = y + dy

                if get(x, y) != "#" and get(tx, ty) != "#": #if is shortcut
                    distance = sheat[y][x] + cheat_distance + eheat[ty][tx]

                    if distance <= honourable - 100:
                        good += 1

print(good)