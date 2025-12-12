grid = open("2025/07/input.txt").read().splitlines()

width = len(grid[0])
height = len(grid)

beams = set() #cols the beams are on
beams.add(grid[0].index("S"))

splits = 0
for row in range(height):
    for beam in list(beams):
        if grid[row][beam] == "^":
            beams.remove(beam)
            beams.add(beam - 1)
            beams.add(beam + 1)

            splits += 1

print(splits)