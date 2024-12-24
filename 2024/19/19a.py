file = open("2024/19/input.txt")

combos = set(file.readline().strip().split(", "))

largest = 0
for combo in combos:
    largest = max(len(combo), largest)

file.readline() #consume input

def is_possible(pattern):
    if not pattern:
        return True
    
    for i in range(min(len(pattern), largest)):
        if pattern[:i+1] in combos and is_possible(pattern[i+1:]):
            return True
        
    return False

total = 0
for line in file.read().splitlines():
    if is_possible(line):
        total += 1

print(total) #that ran INSTANTLY i was expecting to have to use dynamic programming