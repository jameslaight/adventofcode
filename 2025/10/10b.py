import z3

total = 0
for line in open("2025/10/input.txt").read().splitlines():
    split = line.split(" ")
    
    goal = [int(i) for i in split[-1][1:-1].split(",")]

    ops = [[int(i) for i in string[1:-1].split(",")] for string in split[1:-1]]

    eqs = [0] * len(goal) #equations, 0 as initial value for building purposes
    pos_constraints = [] #equations that force unknowns to be non-negative

    solver = z3.Optimize()

    symbols = []
    objective_function = 0
    for i, op in enumerate(ops):
        symbol = z3.Int("x" + str(i))
        symbols.append(symbol)

        objective_function += symbol
        pos_constraints.append(symbol >= 0)

    for op_index, op in enumerate(ops):
        for target in op:
            eqs[target] += symbols[op_index]

    eqs = [eq == goal[i] for i, eq in enumerate(eqs)] #set equations equal to their proper values
    eqs.extend(pos_constraints)
    solver.add(eqs)

    solver.minimize(objective_function)
    solver.check()

    total += solver.model().eval(objective_function).as_long()

print(total)