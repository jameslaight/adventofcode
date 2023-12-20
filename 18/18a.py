file = open("18/input.txt")
lines = file.read().splitlines()
file.close()

x = 0
y = 0
xs = []
ys = []
double_area = 0
for line in lines:
    split = line.split(" ")
    drc = split[0]
    dist = int(split[1])

    match drc:
        case 'U':
            y -= dist
        case 'D':
            y += dist
        case 'L':
            x -= dist
        case 'R':
            x += dist
    
    xs.append(x)
    ys.append(y)

    double_area += dist

for i in range(len(xs)):
    t = (i + 1) % len(xs)

    double_area += xs[i] * ys[t] - ys[i] * xs[t]

area = abs(double_area // 2) + 1
print(area)