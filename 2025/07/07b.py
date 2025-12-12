grid = open("2025/07/input.txt").read().splitlines()

width = len(grid[0])
height = len(grid)

beams = {} #number of timelines each col holds

for i in range(width):
    beams[i] = 0

beams[grid[0].index("S")] = 1

for row in range(height):
    for i in range(width):
        if grid[row][i] == "^":
            beam = beams[i]
            beams[i] = 0
            beams[i - 1] += beam
            beams[i + 1] += beam

print(sum(beams.values()))