file = open("8/input.txt")

paths = {}

lines = file.read().splitlines()

path = lines[0]
lines = lines[2:] #take first 2 lines off

for line in lines:
    split = line.split(" = ")
    name = split[0]
    split = split[1][1:-1].split(", ") #take brackets off
    left = split[0]
    right = split[1]

    paths[name] = (left, right)

cur = "AAA"
steps = 0
while True:
    for dir in path:
        steps += 1

        if dir == 'L':
            cur = paths[cur][0]
        else:
            cur = paths[cur][1]

        if (cur == "ZZZ"):
            break
    else: #allows for double break
        continue

    break

print(steps)

file.close()