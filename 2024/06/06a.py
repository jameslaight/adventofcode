grid = [[c for c in line] for line in open("2024/06/input.txt").read().splitlines()] #nice
width = len(grid[0])
height = len(grid)

def get(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        return grid[y][x]
    else:
        return ""

for x in range(width): #find start
    for y in range(height):
        if get(x, y) == '^':
            px = x
            py = y

dx = 0
dy = -1
visited = set()
while True:
    visited.add((px, py))

    next = get(px + dx, py + dy)
    if next:
        if next == "#":
            dx, dy = -dy, dx
        else:
            px += dx
            py += dy
    else:
        break

print(len(visited))