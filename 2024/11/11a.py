stones = [int(s) for s in open("2024/11/input.txt").read().split(" ")] #looks easier today

for _ in range(25):
    i = 0 #manual iterator (curse you concurrent modification)
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0: #this is a very annoying case
            s = str(stones[i])
            half = len(s) // 2
            n1 = int(s[:half])
            n2 = int(s[half:])

            stones[i] = int(n2)
            stones.insert(i, int(n1))
            i += 1 #manually shunt the iterator forward due to length change
        else:
            stones[i] *= 2024

        i += 1 #next stone

print(len(stones))