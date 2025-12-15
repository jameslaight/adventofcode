sizes = [] #this problem is dumb

lines = open("2025/12/input.txt").read().splitlines()

while lines[0][-1] == ":":
    lines.pop(0) #consume the name

    size = 0
    while line := lines.pop(0): #walrus!
        size += line.count("#")

    sizes.append(size)

total = 0
for line in lines:
    split = line.split(": ")

    width, height = [int(i) for i in split[0].split("x")]
    area = width * height #again
    counts = [int(i) for i in split[1].split(" ")]

    needed = 0
    for i in range(len(counts)):
        needed += counts[i] * sizes[i]

    if needed <= area:
        total += 1

print(total)