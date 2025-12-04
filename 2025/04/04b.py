grid = [[c == '@' for c in line] for line in open("2025/04/input.txt").read().splitlines()]
width = len(grid[0])
height = len(grid)

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return False

    return grid[y][x]

total = 0
any_removed = True

while any_removed:
    any_removed = False

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if get(x, y):
                count = 0

                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0: #do not check same square
                            continue

                        if get(x + dx, y + dy):
                            count += 1

                if count < 4:
                    any_removed = True
                    total += 1
                    grid[y][x] = False

print(total)