file = open("4/input.txt")

sum = 0
for line in file.readlines():
    line = line.replace("\n", "").replace("  ", " ")
    line = line.split(": ")[1]
    split = line.split(" | ")

    winning = [int(i) for i in split[0].split(" ")]
    have = [int(i) for i in split[1].split(" ")]

    value = 0
    for w in winning:
        if w in have:
            if value == 0:
                value = 1
            else:
                value *= 2

    sum += value

print(sum)

file.close()