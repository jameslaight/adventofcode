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
    nums = [int(n) for n in line.split(",")]

    swap = False
    for i in range(len(nums)): #find 2 nums to swap
        for j in range(i+1, len(nums)):
            if nums[j] in after and nums[i] in after[nums[j]]:
                nums[i], nums[j] = nums[j], nums[i]
                swap = True

    if swap:
        total += nums[len(nums) // 2]

print(total)