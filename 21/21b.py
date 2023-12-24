file = open("21/input.txt")
pane = file.read().splitlines()
file.close()

drcs = [(1, 0), (0, 1), (-1, 0), (0, -1)] #directions

pane_width = len(pane[0])
pane_height = len(pane)
square = 5 #size of the grid square of panes
grid = [[None] * pane_width * square for i in range(pane_height * square)]

width = len(grid[0])
height = len(grid)

for grid_y in range(square): #build grid out of a square by square grid of panes
    for grid_x in range(square):
        for pane_y in range(pane_height):
            for pane_x in range(pane_width): #many a for (my brain hurts)
                x = grid_x * pane_width + pane_x
                y = grid_y * pane_height + pane_y

                c = pane[pane_y][pane_x]

                if c == 'S':
                    if grid_x == square // 2 and grid_y == square // 2: #middle square keeps the S
                        start = (x, y)
                    else:
                        c = '.'

                grid[y][x] = c #place into grid

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return '!'
    
    return grid[y][x]

sols = []
for i in range(3):
    spots = set()
    steps = set()
    scan = set([start])
    next_scan = set()
    even = True #alternates each step
    count = 0

    test_steps = i * pane_width + 65 + 1 #adding width each time, add 1 to process initial '0 step' stage
    for j in range(test_steps):
        for s in scan:
            spots.add(s)

            if even ^ test_steps % 2 == 0:
                count += 1
                steps.add(s)

            for drc in drcs:
                coords = (s[0] + drc[0], s[1] + drc[1])

                if get(coords[0], coords[1]) == '.' and not coords in spots:
                    next_scan.add(coords)

        scan = next_scan
        next_scan = set()
        even = not even

    sols.append(count)

p, q, r = sols
a = (p + r) // 2 - q #quadratic formula finding hijinks
b = q - a - p
c = p

goal = 26501365
x = goal // pane_width #number of grids to travel, fitting into the above formula
print(a * x**2 + b * x + c)