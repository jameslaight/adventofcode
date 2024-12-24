registers = [] #so basically program a computer, got it

file = open("2024/17/input.txt") #input parsing (why)
for i in range(3):
    line = file.readline()
    registers.append(int(line.split()[2]))

file.readline() #consume blank line

program = []
split = file.readline().split()[1].split(",")
for i in range(0, len(split), 2):
    program.append((int(split[i]), int(split[i + 1])))

def combo(operand):
    if operand <= 3:
        return operand
    else:
        return registers[operand - 4]

pc = 0 #program counter!
out = []
while pc < len(program): #HLT at end of program
    opcode, operand = program[pc]
    pc += 1

    #prepare for IF STATEMENTS
    if opcode == 0: #adv
        registers[0] = registers[0] // (2 ** combo(operand))
    elif opcode == 1: #bxl
        registers[1] = registers[1] ^ operand
    elif opcode == 2: #bst
        registers[1] = combo(operand) % 8
    elif opcode == 3: #jnz
        if registers[0] != 0:
            pc = operand
    elif opcode == 4: #bxc
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5: #out
        out.append(combo(operand) % 8)
    elif opcode == 6: #bdv
        registers[1] = registers[0] // (2 ** combo(operand))
    elif opcode == 7: #cdv
        registers[2] = registers[0] // (2 ** combo(operand))

first = True
for o in out:
    if first:
        first = False
    else:
        print(",", end="")
    
    print(o, end="")