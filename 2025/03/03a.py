banks = [[int(c) for c in line] for line in open("2025/03/input.txt").read().splitlines()]

def jolt(bank, batteries): #i feel like this will be useful
    batsAfter = batteries - 1

    if batsAfter < 0:
        return 0

    best = -1
    for i in range(len(bank) - batsAfter): #look for leftmost max value
        battery = bank[i]

        if best == -1 or battery > best:
            best = battery
            bestpos = i

    return best * 10 ** batsAfter + jolt(bank[bestpos + 1:], batsAfter)

total = 0
for bank in banks:
    total += jolt(bank, 2)

print(total)