file = open("21/input.txt")
grid = file.read().splitlines()
file.close()

drcs = [(1, 0), (0, 1), (-1, 0), (0, -1)] #directions

width = len(grid[0])
height = len(grid)

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return '!'
    
    return grid[y][x]

def find_start():
    for y in range(height):
        for x in range(width):
            if get(x, y) == 'S':
                return (x, y)
    
    return None

spots = set()
steps = set()
scan = set([find_start()])
next_scan = set()
even = True #alternates each step
count = 0
for i in range(64 + 1): #need to add 1 to process initial '0 step' stage
    for s in scan:
        spots.add(s)
        if even:
            count += 1
            steps.add(s)

        for drc in drcs:
            coords = (s[0] + drc[0], s[1] + drc[1])

            if get(coords[0], coords[1]) == '.' and not coords in spots:
                next_scan.add(coords)

    scan = next_scan
    next_scan = set()
    even = not even

print(count)