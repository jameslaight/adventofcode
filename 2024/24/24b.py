states = {}
gates = []
zs = set()

file = open("2024/24/input.txt")
swapped = ["djg", "z12", "sbg", "z19", "mcq", "hjm", "dsd", "z37"] #solved by hand

while line := file.readline().strip(): #walrus!
    name, init = line.split(": ")
    states[name] = init == "1"

for line in file.read().splitlines():
    in1, op, in2, _, out = line.split() #this feels like python abuse
    
    if out in swapped:
        index = swapped.index(out)
        out = swapped[index + 1 if index % 2 == 0 else index - 1]

    gates.append((op, in1, in2, out))

    if out[0] == "z":
        zs.add(out)

def get(n1, o, n2):
    for op, in1, in2, out in gates:
        if o != op:
            continue

        if in1 == n1 and in2 == n2 or in1 == n2 and in2 == n1:
            return out

i = 0
carry = None
while True:
    if i < 10:
        x = "x0" + str(i)
        y = "y0" + str(i)
        z = "z0" + str(i)
    else:
        x = "x" + str(i)
        y = "y" + str(i)
        z = "z" + str(i)

    if carry:
        xxy = get(x, "XOR", y)
        xay = get(x, "AND", y)

        if xxy == None:
            print("done")
            break

        if get(xxy, "XOR", carry) != z:
            print("(z) " + xxy + " XOR " + carry + " != " + z)
            break

        if not (cac := get(xxy, "AND", carry)):
            print("(cac) " + xxy + " AND " + carry + " no result")
            break

        if not (carry := get(cac, "OR", xay)):
            print("(carry) " + cac + " XOR " + xay + " no result")
            break
    else:
        if get(x, "XOR", y) != z:
            print("x")
            break

        if not (carry := get(x, "AND", y)):
            pass

    print(z + " is correct, carry bit is " + carry)
    i += 1

print(",".join(sorted(swapped)))