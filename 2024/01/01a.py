left = []
right = []
for line in open("2024/01/input.txt").readlines():
    split = line.split("   ")
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)

#i thought it was distance between the numbers in the list i am a fool
#i was wondering why day 1 was so hard