grid = [[c for c in line.strip()] for line in open("2024/04/input.txt").readlines()] #love lines like this

goal = "XMAS" #ain't that the way

width = len(grid)
height = len(grid[0])

def get(x, y): #helper metho is helpful
    if x >= 0 and x < width and y >= 0 and y < height:
        return grid[x][y]
    else:
        return '.'

found = 0
for x in range(width):
    for y in range(height):
        for dx in range(-1, 1+1):
            for dy in range(-1, 1+1):
                for distance in range(len(goal)): #legendary quintuple count-controlled for loop stack
                    if not get(x + dx * distance, y + dy * distance) == goal[distance]:
                        break
                else:
                    found += 1

print(found)