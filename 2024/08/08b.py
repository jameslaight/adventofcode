nodes = {}

grid = [[c for c in line] for line in open("2024/08/input.txt").read().splitlines()]
width = len(grid[0])
height = len(grid)

def get(x, y):
    return grid[y][x]

for x in range(width):
    for y in range(height):
        node = get(x, y)

        if node != ".":
            if not node in nodes:
                nodes[node] = []

            nodes[node].append((x, y))

antinodes = set()
def in_bounds(x, y):
    return x >= 0 and x < width and y >= 0 and y < height

def anti(x, y):
    if in_bounds(x, y):
        antinodes.add((x, y))

for node in nodes:
    coords = nodes[node]

    for i in range(len(coords)): #for each pair
        for j in range(i + 1, len(coords)):
            node_i = coords[i]
            node_j = coords[j]
            delta = (node_i[0] - node_j[0], node_i[1] - node_j[1]) # i <-- j

            for sign in [-1, 1]: #it can go both ways
                m = 0 #magnitude
                while True:
                    x = node_i[0] + delta[0] * m * sign
                    y = node_i[1] + delta[1] * m * sign

                    if not in_bounds(x, y):
                        break
                    
                    anti(x, y)
                    m += 1

print(len(antinodes))