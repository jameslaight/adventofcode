import re

file = open("1/input.txt")

total = 0
for line in file.readlines():
    line = line.replace("\n", "")
    line = re.sub("[^0-9]", "", line)
    total += int(line[0] + line[-1])

print(total)

file.close()