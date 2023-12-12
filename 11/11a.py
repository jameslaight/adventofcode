class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

file = open("11/input.txt")

grid = [list(line) for line in file.read().splitlines()]

gals = []
for y in range(len(grid)): #find all galaxies
    for x in range(len(grid[y])):
        if grid[y][x] == '#':
            gals.append(Galaxy(x, y))

x_penalty = 0
scanned = []
for x in range(len(grid[0])): #penalise x based on empty columns
    gal_found = False #whether galaxy on this column

    for gal in gals:
        if not gal in scanned and gal.x == x: #if non-scanned galaxy on this column
            gal.x += x_penalty #penalise
            scanned.append(gal) #set scanned
            gal_found = True

    if not gal_found: #empty row, penalise x
        x_penalty += 1

y_penalty = 0 #we do it again for y
scanned = []
for y in range(len(grid)): #penalise y based on empty rows
    gal_found = False #whether galaxy on this row

    for gal in gals:
        if not gal in scanned and gal.y == y: #if non-scanned galay on this row
            gal.y += y_penalty #penalise
            scanned.append(gal) #set scanned
            gal_found = True

    if not gal_found: #empty row, penalise y
        y_penalty += 1

sum = 0
for i in range(len(gals)):
    for j in range(i + 1, len(gals)): #for each pair of galaxies
        a = gals[i]
        b = gals[j]
        sum += abs(a.x - b.x) + abs(a.y - b.y) #taxicab distance between galaxies

print(sum)

file.close()