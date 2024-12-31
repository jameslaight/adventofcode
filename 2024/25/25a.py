locks, keys = [], []

width = 5
height = 7

lines = open("2024/25/input.txt").read().splitlines()

while lines:
    pins = [0] * width
    lock = lines[0] == "#" * width #detect lock/key

    for i in range(height):
        line = lines.pop(0)

        for j in range(width):
            if line[j] == "#":
                pins[j] += 1

    if lock:
        locks.append(pins)
    else:
        keys.append(pins)

    if lines:
        lines.pop(0) #consume empty line

total = 0
for lock in locks:
    for key in keys:
        for i in range(width):
            if lock[i] + key[i] > height:
                break
        else: #no break means key fits in lock
            total += 1

print(total)