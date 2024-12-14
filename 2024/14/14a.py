width = 101
height = 103

quadrants = [0] * 4
for line in open("2024/14/input.txt"):
    line = line.replace("p=", "").replace(" v=", ",")
    x, y, dx, dy = [int(n) for n in line.split(",")]

    secs = 100
    x += dx * secs
    y += dy * secs
    x %= width
    y %= height

    quadrant = 0
    if width % 2 and x == width // 2: #being careful doesn't hurt
        continue
    elif x >= width // 2:
        quadrant += 2

    if height % 2 and y == height // 2:
        continue
    elif y >= height // 2:
        quadrant += 1

    quadrants[quadrant] += 1

total = 1
for quadrant in quadrants:
    total *= quadrant
print(total)