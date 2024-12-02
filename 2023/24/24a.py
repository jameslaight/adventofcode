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

bound_min = 200000000000000 #big
bound_max = 400000000000000

count = 0
for i in range(len(hail)):
    for j in range(i + 1, len(hail)):
        a = hail[i]
        b = hail[j]

        result = a.cross(b)

        if result != None:
            x, y = result
            
            if x >= bound_min and x <= bound_max and y >= bound_min and y <= bound_max:
                count += 1

print(count)