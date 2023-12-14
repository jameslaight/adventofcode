file = open("14/input.txt")

grid = []
for line in file.read().splitlines():
    grid.append(list(line))

total = 0
height = len(grid)
for row in range(height):
    for col in range(len(grid[row])):
        if grid[row][col] != 'O':
            continue

        new_row = row
        while new_row > 0:
            if grid[new_row - 1][col] == '.':
                new_row -= 1
            else:
                break

        grid[row][col] = '.'
        grid[new_row][col] = 'O'

        total += height - new_row

print(total)

file.close()