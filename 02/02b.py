file = open("2/input.txt")

total = 0
for line in file.readlines():
    split = line.replace("\n", "").split(": ")
    id = int(split[0].replace("Game ", ""))
    seqs = split[1].split("; ")

    max = {}
    for seq in seqs:
        for hand in seq.split(", "):
            split = hand.split(" ")
            count = int(split[0])
            colour = split[1]

            if not colour in max or count > max[colour]:
                max[colour] = count

    power = 1
    for colour in max:
        power *= max[colour]
    total += power

print(total)

file.close()