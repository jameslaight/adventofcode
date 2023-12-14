def cycle(grid):
    height = len(grid)
    width = len(grid[0])

    for i in range(4): #4 scans then rotations
        for row in range(height):
            for col in range(width):
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

        rot_grid = [[None] * width for i in range(height)]

        for y in range(height): #rotate the grid clockwise
            for x in range(width):
                c = grid[y][x]
                new_x = -y + height - 1 #add height - 1 to push into correct coordinate space
                new_y = x
                rot_grid[new_y][new_x] = c

        grid = rot_grid

    return grid

file = open("14/input.txt")

grid = []
for line in file.read().splitlines():
    grid.append(list(line))

cycles_left = 1000000000 #!!! this number is huge, need to deal with somehow
savestates = {} #states of the grid mapped to the cycles_left when they were found
while cycles_left > 0:
    state = tuple([tuple(row) for row in grid])

    if state in savestates: #if position found before, reduce cycles left as states will now repeat
        difference = savestates[state] - cycles_left #period of the repeat states
        cycles_left %= difference #subtract difference from cycles left as many times as possible

        savestates = {} #clear savestates
    else:
        savestates[state] = cycles_left

    grid = cycle(grid)
    cycles_left -= 1

height = len(grid)
total = 0
for row in range(height):
    for col in range(len(grid[row])):
        if grid[row][col] == 'O':
            total += height - row

print(total)

file.close()