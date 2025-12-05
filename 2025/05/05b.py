#that sounds pretty easy- oh wait a second
lines = open("2025/05/input.txt").read().splitlines()

class Range():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def in_range(self, val):
        return val >= self.min and val <= self.max
    
    def overlaps(self, other):
        return self.in_range(other.max) or other.in_range(self.max)

    def merge(self, other):
        return Range(min(self.min, other.min), max(self.max, other.max))

ranges = []
while lines[0]:
    line = lines.pop(0)
    split = [int(i) for i in line.split("-")]
    ranges.append(Range(split[0], split[1]))

i = 0
while i < len(ranges):
    range_i = ranges[i]

    for range_j in list(ranges):
        if range_i == range_j: #no self-comparison
            continue

        if range_i.overlaps(range_j):
            ranges[i] = range_i.merge(range_j)
            ranges.remove(range_j)
            break
    else: #increment if break not triggered
        i += 1

total = 0 #time to total the ranges
for r in ranges:
    total += r.max - r.min + 1 #+1 because both ends are inclusive

print(total)