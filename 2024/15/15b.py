lines = open("2024/15/input.txt").read().splitlines() #PART 2 IS EVIL

grid = []
while True:
    line = lines.pop(0)

    if not line:
        break

    grid_line = []
    for c in line:
        if c == "@":
            grid_line.extend("@.")
        elif c == "O":
            grid_line.extend("[]")
        else:
            grid_line.extend(c * 2)

    grid.append(grid_line)

instructions = []
for line in lines:
    instructions.extend([c for c in line])

width = len(grid[0])
height = len(grid)

def can_move(x, y, dx, dy):
    tx = x + dx
    ty = y + dy
    c = grid[ty][tx]

    if c == "#":
        return False
    elif c == '.':
        return True
    elif dy == 0:
        return can_move(tx, ty, dx, dy)
    else:
        ddx = 1 if c == "[" else -1 #ternary operator: python edition
        return can_move(tx, ty, dx, dy) and can_move(tx + ddx, ty, dx, dy)

def shove(x, y, dx, dy):
    tx = x + dx
    ty = y + dy
    c = grid[ty][tx]

    if c == "[" or c == "]":
        ddx = 1 if c == "[" else -1
        shove(tx + ddx, ty, dx, dy) #shove outermost first! things get wacky otherwise
        shove(tx, ty, dx, dy)

    grid[y][x], grid[ty][tx] = grid[ty][tx], grid[y][x]
    
for cx in range(width):
    for cy in range(height):
        if grid[cy][cx] == "@":
            x = cx
            y = cy

imap = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
for instruction in instructions:
    dx, dy = imap[instruction]

    if can_move(x, y, dx, dy):
        shove(x, y, dx, dy)

        x += dx
        y += dy

total = 0
for x in range(width):
    for y in range(height):
        if grid[y][x] == "[":
            total += y * 100 + x

print(total) #i'm surprised i got this so fast