lines = open("2024/15/input.txt").read().splitlines()

grid = []
while True:
    line = lines.pop(0)

    if not line:
        break

    grid.append([c for c in line])

instructions = []
for line in lines:
    instructions.extend([c for c in line])

width = len(grid[0])
height = len(grid)

def shove(x, y, dx, dy):
    tx = x + dx
    ty = y + dy
    c = grid[ty][tx]
    
    if c == "O" and shove(tx, ty, dx, dy) or c == ".":
        grid[y][x], grid[ty][tx] = grid[ty][tx], grid[y][x] #swap positions

        return True
    else:
        return False
    
for cx in range(width):
    for cy in range(height):
        if grid[cy][cx] == "@":
            x = cx
            y = cy

imap = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
for instruction in instructions:
    dx, dy = imap[instruction]

    if shove(x, y, dx, dy):
        x += dx
        y += dy

total = 0
for x in range(width):
    for y in range(height):
        if grid[y][x] == "O":
            total += y * 100 + x

print(total)