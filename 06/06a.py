import re

file = open("6/input.txt")
lines = file.read().splitlines()

for i in range(len(lines)):
    lines[i] = re.sub("  +", " ", lines[i])

times = [int(t) for t in lines[0].replace("Time: ", "").split()]
distances = [int(d) for d in lines[1].replace("Distance: ", "").split()]

result = 1
for i in range(len(times)): #number of races
    ways = 0

    time = times[i]
    for speed in range(time + 1):
        distance = speed * (time - speed)

        if distance > distances[i]:
            ways += 1

    result *= ways

print(result)

file.close()