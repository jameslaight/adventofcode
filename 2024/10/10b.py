grid = [[int(c) for c in line] for line in open("2024/10/input.txt").read().splitlines()] #day 10 destroyed me last year

width = len(grid[0]) #so many grids
height = len(grid)

def get(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        return grid[y][x]
    else:
        return -1 #should work
    
def hike(x, y, p, v):
    p = p.copy()
    p.append((x, y))

    if v > 9: #peak found
        r = set()
        r.add(tuple(p))
        
        return r #base case

    paths = set()

    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if get(x + dx, y + dy) == v:
            h = hike(x + dx, y + dy, p, v + 1)
            paths = paths.union(h)

    return paths

total = 0
for x in range(width):
    for y in range(height):
        if get(x, y) == 0:
            total += len(hike(x, y, [], 1))

print(total)