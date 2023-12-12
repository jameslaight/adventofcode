file = open("12/input.txt")

def permute(seq, nums): #IT'S SO CLEAN I LOVE IT
    if len(nums) == 0: #no nums left, this is a permutation if there are no #s left in seq
        if not '#' in seq: #no faulty, this is a permutation (return 1)
            return 1
        else: #faulty, this is not a permutation (return 0)
            return 0

    num = nums[0]

    if num > len(seq): #no room for next block!
        return 0 #no permutations

    count = 0

    for i in range(num): #check if next block of # can go here
        if seq[i] == '.': #break if operational, block cannot go here
            break
    else: #if next block of # can go here
        if len(seq) == num or seq[num] != '#': #must be end of string or non-faulty spring after faulty block
            new_nums = nums.copy()
            new_nums.pop(0) #pop size of block just 'added'
            count += permute(seq[num + 1:], new_nums) #slice sequence and recurse deeper

    if seq[0] != '#': #if next is not faulty, assume for this path it is functional
        count += permute(seq[1:], nums) #slice sequence and recurse deeper

    return count #return number of permutations

total = 0
for line in file.read().splitlines():
    split = line.split()
    seq = split[0]
    nums = [int(i) for i in split[1].split(",")]

    total += permute(seq, nums)

print(total)

file.close()