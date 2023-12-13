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
        reflection_fails = 0 #reflection fails are now counted. if there is exactly one reflection fail, one symbol could be flipped to give the reflection 

        while reflection_fails <= 1 and left_col >= 0 and right_col < width:
            for row in range(height): #scan row along the two columns to check they are equal
                if grid[row][left_col] != grid[row][right_col]:
                    reflection_fails += 1
                    
                    if reflection_fails > 1:
                        break

            left_col -= 1
            right_col += 1

            if reflection_fails > 1: #break out of loop
                break

        if reflection_fails == 1:
            total += col #add columns to the left of line of relection to total

    for row in range(1, height): #do it again
        above_row = row - 1
        below_row = row
        reflection_fails = 0

        while reflection_fails <= 1 and above_row >= 0 and below_row < height:
            for col in range(width): #scan column along the two rows to check they are equal
                if grid[above_row][col] != grid[below_row][col]:
                    reflection_fails += 1

                    if reflection_fails > 1:
                        break

            above_row -= 1
            below_row += 1

            if reflection_fails > 1: #break out of loop
                break

        if reflection_fails == 1:
            total += row * 100 #add rows above line of relection * 100 to total

print(total)

file.close()