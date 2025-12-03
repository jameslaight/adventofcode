lines = open("2025/01/input.txt").read().splitlines()

zero = 0
pos = 50

for line in lines:
    dir = line[0]
    steps = int(line[1:])

    lastpos = pos
    if dir == "L":
        pos -= steps
    elif dir == "R":
        pos += steps

    if pos >= 100:
        zero += pos // 100
    elif pos <= 0:
        zero += -pos // 100

        if lastpos != 0: #edge case: pos can go negative without passing 0 if last pos was 0
            zero += 1

    pos %= 100

print(zero)