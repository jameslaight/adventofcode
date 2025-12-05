lines = open("2025/05/input.txt").read().splitlines()

class Range():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def in_range(self, val):
        return val >= self.min and val <= self.max

ranges = []
while lines[0]:
    line = lines.pop(0)
    split = [int(i) for i in line.split("-")]
    ranges.append(Range(split[0], split[1]))

lines.pop(0) #consume blank line

total = 0
for line in lines:
    val = int(line)

    for r in ranges:
        if r.in_range(val):
            total += 1
            break

print(total)