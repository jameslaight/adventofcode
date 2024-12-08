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
def anti(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        antinodes.add((x, y))

for node in nodes:
    coords = nodes[node]

    for i in range(len(coords)): #for each pair
        for j in range(i + 1, len(coords)):
            node_i = coords[i]
            node_j = coords[j]
            delta = (node_i[0] - node_j[0], node_i[1] - node_j[1]) # i <-- j

            anti(node_i[0] + delta[0], node_i[1] + delta[1]) # a <-- i <-- j
            anti(node_j[0] - delta[0], node_j[1] - delta[1]) #       i <-- j <-- a

print(len(antinodes))