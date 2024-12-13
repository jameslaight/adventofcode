import re #maths time (and regex time!)

lines = open("2024/13/input.txt").read().splitlines()

total = 0
while lines:
    read = []
    for i in range(3): #read 3 lines
        read.extend([int(i) for i in re.findall(r"\d+", lines.pop(0))])
    if lines:
        lines.pop(0) #consume empty line

    xa, ya, xb, yb, x, y = read

    numerator = x - y * xb / yb #rearranged a linear system of equations to get this
    denominator = xa - ya * xb / yb
    a = numerator / denominator
    b = (y - a * ya) / yb

    a = round(a) #round values to integers
    b = round(b)

    if a*xa + b*xb == x and a*ya + b*yb == y: #plug back in to check if these integer solutions work
        total += 3*a + b

print(total)