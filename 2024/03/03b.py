import re #feel like i'm gonna need this

total = 0
line = open("2024/03/input.txt").read().replace("\n", "")
split = re.split(r"do(n't)?\(\)", line) #i have a funny idea

split.insert(0, None) #insert None at start to indicate do()

for i in range(0, len(split), 2):
    if not split[i]: #split[i] is None if instruction is do()
        for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", split[i + 1]):
            total += int(x) * int(y)
    
print(total)