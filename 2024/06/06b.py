grid = [[c for c in line] for line in open("2024/06/input.txt").read().splitlines()] #nice
width = len(grid[0])
height = len(grid)

def get(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        return grid[y][x]
    else:
        return ""
    
def repl(x, y, v):
    grid[y][x] = v

def get_visited(px, py, dx, dy): #refactor
    visited = set()
    disited = set()
    while True:
        disit = (px, py, dx, dy)
        if disit in disited: #time loop??
            return set()

        visited.add((px, py))
        disited.add(disit)

        next = get(px + dx, py + dy)
        if next:
            if next == "#":
                dx, dy = -dy, dx
            else:
                px += dx
                py += dy
        else:
            break

    return visited

for x in range(width): #find start
    for y in range(height):
        if get(x, y) == '^':
            start_x = x
            start_y = y

total = 0
candidates = get_visited(start_x, start_y, 0, -1) #only need to try squares that the guard visits
for candidate in candidates: #otherwise i could be here a while
    if candidate == (start_x, start_y): #can't put object on guard 
        continue #for obvious reasons

    repl(candidate[0], candidate[1], "#")

    if not get_visited(start_x, start_y, 0, -1): #returns falsey if repeating
        total += 1

    repl(candidate[0], candidate[1], ".")

print(total)