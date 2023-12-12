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

    number = ""
    adj = False
    for x in range(width):
        c = line[x]

        if (re.match("[0-9]", c)):
            number += c

            if not adj:
                for dy in range(-1, 1 + 1):
                    for dx in range(-1, 1 + 1):
                        ty = y + dy
                        tx = x + dx

                        if ty >= 0 and ty < height and tx >= 0 and tx < width:
                            if re.match("[^0-9\.]", lines[ty][tx]):
                                adj = True


        if re.match("[^0-9]", c) or (x == width - 1 and number):
            if adj:
                sum += int(number)

            number = ""
            adj = False

print(sum)

file.close()