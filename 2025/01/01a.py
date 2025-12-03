lines = open("2025/01/input.txt").readlines()

zero = 0
pos = 50

for line in lines:
    dir = line[0]
    steps = int(line[1:])

    if dir == "L":
        pos -= steps
    elif dir == "R":
        pos += steps

    pos %= 100

    if pos == 0:
        zero += 1

print(zero)