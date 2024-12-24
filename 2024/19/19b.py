file = open("2024/19/input.txt")

combos = set(file.readline().strip().split(", "))

largest = 0
for combo in combos:
    largest = max(len(combo), largest)

file.readline() #consume input

dynamic_programming_woo = {}
def permute(pattern):
    if pattern in dynamic_programming_woo:
        return dynamic_programming_woo[pattern]

    if not pattern:
        return 1
    
    ways = 0
    for i in range(min(len(pattern), largest)):
        if pattern[:i+1] in combos:
            ways += permute(pattern[i+1:])
        
    dynamic_programming_woo[pattern] = ways
    return ways

total = 0
for line in file.read().splitlines():
    total += permute(line)

print(total) #nevermind there's the dynamic programming