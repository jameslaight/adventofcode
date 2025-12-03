lines = open("2025/02/input.txt").read().split(",")

ranges = []
for line in lines:
    split = line.split("-")
    nums = [int(s) for s in split]
    ranges.append(range(nums[0], nums[1] + 1))

total = 0
for r in ranges:
    for num in r:
        strnum = str(num)
        half = len(strnum) // 2 #index halfway through the string

        if strnum[:half] == strnum[half:]: #if number is repeated
            total += num

print(total)