import sympy #and thus i am defeated on my quest to use no external libraries. this system of equations has forced my hand though

class Hailstone:
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz

        self.m = dy / dx #y = mx + c
        self.c = y - self.m * x

    def cross(self, other): #get x, y of where path crosses with other hailstone, if possible
        if self.m == other.m: #parallel, will never cross
            return None

        x = (other.c - self.c) / (self.m - other.m)
        y = self.m * x + self.c

        for h in [self, other]: #check both for time taken to get to positon (must check both as hailstones need not collide)
            t = (x - h.x) / h.dx #number of nanoseconds taken to get to position
            if t < 0: #if t is negative, collision occurred in the past, will never cross
                return None
        
        return (x, y)

file = open("24/input.txt")
hail = []
for line in file.read().splitlines():
    split = line.split(" @ ")
    pos = [int(i) for i in split[0].split(',')]
    dif = [int(i) for i in split[1].split(',')]

    hail.append(Hailstone(pos[0], pos[1], pos[2], dif[0], dif[1], dif[2]))
file.close()

xs, ys, zs, dxs, dys, dzs = [[] for i in range(6)] #initialise all to empty list

for i in range(3): #grab first 3 hailstones, store
    stone = hail[i]

    xs.append(stone.x)
    ys.append(stone.y)
    zs.append(stone.z)
    dxs.append(stone.dx)
    dys.append(stone.dy)
    dzs.append(stone.dz)

x = sympy.symbols("x")
y = sympy.symbols("y")
z = sympy.symbols("z")
dx = sympy.symbols("dx")
dy = sympy.symbols("dy")
dz = sympy.symbols("dz")

eqs = []

for i in range(3):
    eqs.append((y - ys[i]) * (dz - dzs[i]) - (z - zs[i]) * (dy - dys[i]))
    eqs.append((z - zs[i]) * (dx - dxs[i]) - (x - xs[i]) * (dz - dzs[i]))
    eqs.append((x - xs[i]) * (dy - dys[i]) - (y - ys[i]) * (dx - dxs[i]))

sols = sympy.solve(eqs, [x, y, z, dx, dy, dz], dict=True)[0]
print(sols[x] + sols[y] + sols[z])