left = []
right = []
for line in open("2024/01/input.txt").readlines():
    split = line.split("   ")
    left.append(int(split[0]))
    right.append(int(split[1]))

right_counts = {}
for r in right:
    if r in right_counts:
        right_counts[r] += 1
    else:
        right_counts[r] = 1

left.sort()
right.sort()

total = 0
for l in left:
    if l in right_counts:
        total += l * right_counts[l]

print(total)