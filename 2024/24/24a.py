states = {}
gates = []
zs = set()

file = open("2024/24/input.txt")

while line := file.readline().strip(): #walrus!
    name, init = line.split(": ")
    states[name] = init == "1"

for line in file.read().splitlines():
    in1, op, in2, _, out = line.split() #this feels like python abuse
    gates.append((op, in1, in2, out))

    if out[0] == "z":
        zs.add(out)

while gates:
    i = 0
    while i < len(gates): #foreach avoiding concurrent modification
        op, in1, in2, out = gates[i]
        
        if out in states: #gate has output set
            gates.remove(gates[i])
            continue

        i += 1

        if not (in1 in states and in2 in states): #not ready to compute
            continue

        if op == "OR":
            result = states[in1] or states[in2]
        elif op == "AND":
            result = states[in1] and states[in2]
        elif op == "XOR":
            result = states[in1] ^ states[in2]
        
        states[out] = result

result = 0
for z in zs:
    if states[z]:
        result += 2 ** int(z[1:])
print(result)