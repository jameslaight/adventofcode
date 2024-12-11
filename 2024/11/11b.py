inp = [int(s) for s in open("2024/11/input.txt").read().split(" ")] #oh no

stones = {} #oh very clever, the order of the stones is a red herring
for s in inp:
    stones[s] = stones.setdefault(s, 0) + 1

for _ in range(75):
    new_stones = {}

    for n in stones:
        if n == 0:
            new_stones[n + 1] = new_stones.setdefault(n + 1, 0) + stones[n]
        elif len(str(n)) % 2 == 0: #this is a very annoying case
            s = str(n)
            half = len(s) // 2
            n1 = int(s[:half])
            n2 = int(s[half:])

            new_stones[n1] = new_stones.setdefault(n1, 0) + stones[n]
            new_stones[n2] = new_stones.setdefault(n2, 0) + stones[n]
        else:
            new_stones[n * 2024] = new_stones.setdefault(n * 2024, 0) + stones[n]

    stones = new_stones

total = 0
for n in stones:
    total += stones[n]
print(total)