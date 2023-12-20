file = open("18/input.txt")
lines = file.read().splitlines()
file.close()

x = 0
y = 0
xs = []
ys = []
double_area = 0
for line in lines:
    code = line.split(" ")[2]
    drc = code[-2]
    dist = int(code[2:-2], 16)

    match drc:
        case '3':
            y -= dist
        case '1':
            y += dist
        case '2':
            x -= dist
        case '0':
            x += dist
    
    xs.append(x)
    ys.append(y)

    double_area += dist

for i in range(len(xs)):
    t = (i + 1) % len(xs)

    double_area += xs[i] * ys[t] - ys[i] * xs[t]

area = abs(double_area // 2) + 1
print(area)