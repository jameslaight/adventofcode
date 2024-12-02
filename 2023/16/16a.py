file = open("16/input.txt")

grid = [list(line) for line in file.read().splitlines()]
height = len(grid)
width = len(grid[0])

powered = [[False] * width for line in grid]

lasers = [((0, 0), (1, 0))]

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

print(count)

file.close()