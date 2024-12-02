max = {"red": 12, "green": 13, "blue": 14}

file = open("2/input.txt")

total = 0
for line in file.readlines():
    split = line.replace("\n", "").split(": ")
    id = int(split[0].replace("Game ", ""))
    seqs = split[1].split("; ")

    for seq in seqs:
        possible = True
        for hand in seq.split(", "):
            split = hand.split(" ")
            count = int(split[0])
            colour = split[1]

            if count > max[colour]:
                possible = False
                break

        if not possible:
            break
    else:
        total += id

print(total)

file.close()