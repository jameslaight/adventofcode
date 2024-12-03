import re #feel like i'm gonna need this

total = 0
line = open("2024/03/input.txt").read().replace("\n", "")
for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
    total += int(x) * int(y)
    
print(total) #that was short