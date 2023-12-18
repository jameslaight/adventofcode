file = open("16/input.txt")

overgrid = [list(line) for line in file.read().splitlines()]
height = len(overgrid)
width = len(overgrid[0])

def shoot(initial):
    grid = [line.copy() for line in overgrid]
    powered = [[False] * width for line in grid]

    lasers = [initial]

    count = 0
    while len(lasers) > 0:
        laser = lasers.pop()

        x = laser[0][0]
        y = laser[0][1]
        dx = laser[1][0]
        dy = laser[1][1]

        while x >= 0 and x < width and y >= 0 and y < height:
            if not powered[y][x]: #power if not powered
                powered[y][x] = True
                count += 1

            match grid[y][x]:
                case '\\':
                    dx, dy = dy, dx
                case '/':
                    dx, dy = -dy, -dx
                case '-':
                    if dy != 0:
                        grid[y][x] = '#'
                        for nx in (-1, 1):
                            lasers.append(((x + nx, y), (nx, 0)))
                        break
                case '|':
                    if dx != 0:
                        grid[y][x] = '#'
                        for ny in (-1, 1):
                            lasers.append(((x, y + ny), (0, ny)))
                        break
                case '#':
                    break

            x += dx
            y += dy

    return count

initials = []
for x in range(width):
    initials.append(((x, 0), (0, 1)))
    initials.append(((x, height - 1), (0, -1)))
for y in range(height):
    initials.append(((0, y), (1, 0)))
    initials.append(((width - 1, y), (-1, 0)))

best = 0
for initial in initials:
    best = max(shoot(initial), best)
print(best)

file.close()