from collections import deque #first import, here's to many more

disk = [int(c) for c in open("2024/09/input.txt").read()] #that's a big input, gotta be efficient

files = deque()
id = 0
for i in range(0, len(disk), 2):
    files.extend([id] * disk[i])
    id += 1

#the plan is to pop from the left of files during files (in disk), and from the right during gaps
total = 0
pos = 0
gap = False
for d in disk:
    for _ in range(d):
        if not files:
            break

        if gap:
            popped = files.pop()
        else:
            popped = files.popleft()

        total += popped * pos
        pos += 1

    if not files:
        break

    gap = not gap

print(total)