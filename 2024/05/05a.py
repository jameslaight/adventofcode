after = {}

lines = open("2024/05/input.txt").read().splitlines()
while (line := lines.pop(0)):
    split = line.split("|")
    b = int(split[0])
    a = int(split[1])

    if b in after:
        after[b].append(a)
    else:
        after[b] = [a]

total = 0
for line in lines:
    printed = []

    valid = True
    for num in [int(n) for n in line.split(",")]:
        for p in printed:
            if num in after and p in after[num]:
                valid = False
                break

        if not valid:
            break

        printed.append(num)
    else:
        total += printed[(len(printed)) // 2]

print(total)