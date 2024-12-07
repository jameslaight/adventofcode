def valid(target, operands): #it's a recurison day
    if (operands[0] > target): #impossible if an operand is larger than target (efficiency)
        return False

    if (len(operands) == 1): #base case, kinda important
        return target == operands[0]
    
    rest = operands[2:]
    plus = [operands[0] + operands[1]]
    plus.extend(rest)
    prod = [operands[0] * operands[1]]
    prod.extend(rest)
    conc = [int(str(operands[0]) + str(operands[1]))]
    conc.extend(rest)

    return valid(target, plus) or valid(target, prod) or valid(target, conc)
     
total = 0
for line in open("2024/07/input.txt").read().splitlines():
    split = line.split(": ")
    target = int(split[0])
    operands = [int(n) for n in split[1].split(" ")]

    if valid(target, operands):
        total += target

print(total)