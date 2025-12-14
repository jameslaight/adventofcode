def between(a, x, b): #returns whether x is between a and b
    if b < a:
        a, b = b, a

    return a < x and b > x

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, kind, p, b1, b2):
        if b1 > b2:
            b1, b2 = b2, b1 #b1 is always smaller than b2

        self.kind = kind #x for vertical, y for horizontal
        self.p = p #primary (position of fixed axis the line runs along)
        self.b1 = b1 #boundary 1 (beginning of line on non-primary axis)
        self.b2 = b2 #boundary 2 (end of line on non-primary axis)

    def intersects(self, v1, v2):
        if self.kind == "x": #assign primaries from vectors based on kind
            v1p, v2p, v1b, v2b = v1.x, v2.x, v1.y, v2.y
        else:
            v1p, v2p, v1b, v2b = v1.y, v2.y, v1.x, v2.x

        if v1p > v2p: #v1p is smaller
            v1p, v2p = v2p, v1p
        if v1b > v2b: #v1b is smaller
            v1b, v2b = v2b, v1b

        if not between(v1p, self.p, v2p): #not between primaries, not intersecting
            return False
        
        return between(self.b1 - 1, v1b, self.b2) or between(self.b1, v2b, self.b2 + 1) #check boundaries

squares = []
for line in open("2025/09/input.txt").read().splitlines():
    x, y = [int(i) for i in line.split(",")]
    squares.append(Vector(x, y))
count = len(squares)

lines = []
for i in range(count): #create lines
    before = squares[i]
    after = squares[(i + 1) % count]

    if before.x == after.x:
        lines.append(Line("x", before.x, before.y, after.y))
    else:
        lines.append(Line("y", before.y, before.x, after.x))

best = 0
for i in range(count): #calculate best valid area
    for j in range(i + 1, count):
        sq_i, sq_j = squares[i], squares[j]

        width = abs(sq_i.x - sq_j.x) + 1 #+1 for fencepost problem
        height = abs(sq_i.y - sq_j.y) + 1
        area = width * height #shocking

        if area <= best: #if cannot beat best skip
            continue

        if any(line.intersects(sq_i, sq_j) for line in lines): #if any lines are intersected skip
            continue

        best = area

print(best)