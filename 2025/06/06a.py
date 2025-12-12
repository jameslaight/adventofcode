import re

lines = [re.sub(" +", " ", line).strip() for line in open("2025/06/input.txt").read().splitlines()]

problems = len(lines[0].split(" "))
nums = [[] for _ in range(problems)]

for i in range(len(lines) - 1):
    split = lines[i].split(" ")

    for j in range(len(split)):
        nums[j].append(int(split[j]));

grand_total = 0
ops = lines[-1].split(" ")
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