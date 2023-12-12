def find_next(seq): #it's recursion! i love recursion
    if seq == [0]:
        return 0
    
    under_seq = []

    for i in range(len(seq) - 1):
        under_seq.append(seq[i + 1] - seq[i])

    return seq[-1] + find_next(under_seq)

file = open("9/input.txt")

sum = 0
for line in file.read().splitlines():
    seq = [int(i) for i in line.split(" ")]
    sum += find_next(seq)

print(sum)

file.close()