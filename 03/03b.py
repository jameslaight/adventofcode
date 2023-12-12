import re

file = open("3/input.txt")

lines = file.readlines()

height = len(lines)

for y in range(height):
    lines[y] = lines[y].replace("\n", "")

width = len(lines[0])

sum = 0
for y in range(height):
    line = lines[y]

    for x in range(width):
        c = line[x]

        if c == "*":
            ratio = 1
            found = 0

            consumed = [] #make sure same coordinate is not read twice
            for dy in range(-1, 1 + 1):
                for dx in range(-1, 1 + 1):
                    ty = y + dy
                    tx = x + dx

                    if (tx, ty) in consumed:
                        continue

                    if ty < 0 or ty >= height or tx < 0 or tx >= width:
                        continue

                    if re.match("[^0-9]", lines[ty][tx]):
                        continue

                    while tx - 1 >= 0 and re.match("[0-9]", lines[ty][tx - 1]):
                        tx -= 1

                    number = ""
                    while tx < width and re.match("[0-9]", lines[ty][tx]):
                        number += lines[ty][tx]
                        consumed.append((tx, ty))
                        tx += 1 #forgot this, no wonder the program was hanging

                    ratio *= int(number)
                    found += 1

            if found >= 2:
                sum += ratio

print(sum)

file.close()