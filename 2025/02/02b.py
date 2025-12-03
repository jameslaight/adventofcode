def is_repeating(string, step): #checks if a string repeats every step (e.g. "abcabc" repeats with step 3)
    if len(string) % step != 0: #must be perfectly divisible
        return False
    
    sections = [""] * (len(string) // step) #empty string for each section

    for i in range(len(string)):
        sections[i // step] += string[i] #add each character to correct section

    return all([section == sections[0] for section in sections]) #return wether all sectios are equal to the first one (all equal)

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

        for step in range(1, len(strnum) // 2 + 1): #maximum value of step that is possible
            if is_repeating(strnum, step): #check if num repeats for step
                total += num
                break

print(total)