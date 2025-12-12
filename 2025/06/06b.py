import re

lines = open("2025/06/input.txt").read().splitlines()

nums = []
to_add = []
for col in range(len(lines[0])):
    string = ""

    for row in range(len(lines) - 1):
        c = lines[row][col]

        string += c
    string = string.strip()

    if not string: #empty column, add to_add to nums and reset
        nums.append(to_add)
        to_add = []
        continue

    to_add.append(int(string))

nums.append(to_add) #add final

grand_total = 0
ops = re.split(" +", lines[-1])
for i in range(len(ops)):
    op = ops[i]
    
    if op == "*":
        total = 1

        for num in nums[i]:
            total *= num

        grand_total += total
    elif op == "+":
        grand_total += sum(nums[i])

print(grand_total)