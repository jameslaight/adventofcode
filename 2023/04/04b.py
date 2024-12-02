file = open("4/input.txt")

sum = 0
lines = file.readlines()
cards = {}

for i in range(len(lines)):
    cards[i] = 1

for index in range(len(lines)):
    line = lines[index] 
    line = line.replace("\n", "").replace("  ", " ") #pesky double spaces >:(
    line = line.split(": ")[1]
    split = line.split(" | ")

    winning = [int(i) for i in split[0].split(" ")]
    have = [int(i) for i in split[1].split(" ")]

    won = 0
    for w in winning:
        if w in have:
            won += 1

    for i in range(cards[index]):
        for j in range(1, won + 1):
            cards[index + j] += 1

sum = 0
for index in cards:
    sum += cards[index]

print(sum)

file.close()