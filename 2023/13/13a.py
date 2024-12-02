file = open("13/input.txt")

grids = []

grid = []
for line in file.read().splitlines():
    if line:
        grid.append(list(line))
    else:
        grids.append(grid)
        grid = []
if grid:
    grids.append(grid)

total = 0
for grid in grids:
    width = len(grid[0])
    height = len(grid)

    for col in range(1, width): #check COLUMN reflection, line of reflection is to the LEFT the indexed column
        left_col = col - 1
        right_col = col
        reflection = True

        while reflection and left_col >= 0 and right_col < width:
            for row in range(height): #scan row along the two columns to check they are equal
                if grid[row][left_col] != grid[row][right_col]:
                    reflection = False
                    break

            left_col -= 1
            right_col += 1

            if not reflection: #break out of loop
                break

        if reflection:
            total += col #add columns to the left of line of relection to total

    for row in range(1, height): #do it again
        above_row = row - 1
        below_row = row
        reflection = True

        while reflection and above_row >= 0 and below_row < height:
            for col in range(width): #scan column along the two rows to check they are equal
                if grid[above_row][col] != grid[below_row][col]:
                    reflection = False
                    break

            above_row -= 1
            below_row += 1

            if not reflection: #break out of loop
                break

        if reflection:
            total += row * 100 #add rows above line of relection * 100 to total

print(total)

file.close()