grid = [[c for c in line.strip()] for line in open("2024/04/input.txt").readlines()] #love lines like this

goal = "MAS" #what

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
        mas = 0

        for dx in range(-1, 1+1, 2):
            for dy in range(-1, 1+1, 2):
                for distance in range(0, len(goal)): #legendary quintuple count-controlled for loop stack
                    if not get(x + dx * (distance - 1), y + dy * (distance - 1)) == goal[distance]:
                        break
                else:
                    mas += 1

        if mas == 2:
            found += 1

print(found)