file = open("15/input.txt")

codes = file.readline().replace("\n", "").split(",")

total = 0
for code in codes:
    value = 0
    for c in code:
        value += ord(c)
        value *= 17
        value %= 256
    total += value

print(total)

file.close()