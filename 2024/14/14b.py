width = 101
height = 103

robots = []
for line in open("2024/14/input.txt"):
    line = line.replace("p=", "").replace(" v=", ",")
    robots.append(tuple(int(n) for n in line.split(",")))

secs = 0
total_avg_neighbours = 0
while True:
    map = []
    for y in range(height): #create false map
        map.append([False] * width)

    for x, y, dx, dy in robots:
        x += dx * secs
        y += dy * secs
        x %= width
        y %= height

        map[y][x] = True

    max_neighbours = 0
    for nx in range(width):
        for ny in range(height):
            if not map[ny][nx]:
                continue

            neighbours = 0
            for ndx in range(-1, 1+1):
                for ndy in range(-1, 1+1):
                    if ndx == 0 and ndy == 0:
                        continue
                    
                    tx = nx + ndx
                    ty = ny + ndy

                    if tx >= 0 and tx < width and ty > 0 and ty < height and map[ty][tx]:
                        neighbours += 1

            max_neighbours = max(neighbours, max_neighbours)

    if max_neighbours >= 8:
        for y in range(height):
            for x in range(width):
                if map[y][x]:
                    print("X", end="")
                else:
                    print(".", end="")
            print("")

        i = input("is this a christmas tree? y/n\n") #this is a hilarious part 2

        if i == "y":
            break

    secs += 1

print(secs)