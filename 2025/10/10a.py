def press(state, goal, ops, current):
    if current >= len(ops):
        if state == goal:
            return 0
        else:
            return len(ops) #maximum penalty

    op = ops[current]

    new_state = list(state)
    for i in op:
        new_state[i] ^= True #flip boolean

    apply = press(new_state, goal, ops, current + 1) + 1
    dont = press(state, goal, ops, current + 1)

    return min(apply, dont)

total = 0
for line in open("2025/10/input.txt").read().splitlines(): #joltage is suspicious
    split = line.split(" ")
    
    goal = [c == "#" for c in split[0][1:-1]]

    ops = [[int(i) for i in string[1:-1].split(",")] for string in split[1:-1]]

    total += press([False] * len(goal), goal, ops, 0)

print(total)