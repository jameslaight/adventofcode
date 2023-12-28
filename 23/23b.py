#PART 2
#guess i'll just remove the slope code and see what happens
#update: well the program is a tad slower now but it works :D

class Node:
    def __init__(self, directions):
        self.directions = directions #dx, dy of paths surrounding the node
        self.connected = []

class Connection:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance

file = open("23/input.txt")
grid = file.read().splitlines()
file.close()

width = len(grid[0])
height = len(grid)

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return '#' #assume wall past edges of grid

    return grid[y][x]

nodes = {} #coordinates mapped to nodes on grid
for y in range(height): #find junctions, turn them into nodes
    for x in range(width):
        if get(x, y) == '#':
            continue

        dx = 1
        dy = 0

        directions = [] #open paths surrounding this square
        for i in range(4): #check cardinal directions
            if get(x + dx, y + dy) != '#':
                directions.append((dx, dy))

            dx, dy = dy, -dx

        if len(directions) != 2: #if any number of directions other than 2 exist, this is a junction/dead end and thus a node
            node = Node(directions)
            nodes[(x, y)] = node
            
            if y == 0: #special nodes
                start = node
            elif y == height - 1:
                end = node

for coords in nodes: #explore all paths of each node to find its connected nodes
    node = nodes[coords]

    for direction in node.directions: #for each valid direction from the node, find its connected node
        dx, dy = direction

        x, y = coords
        distance = 0
        while not (x, y) in nodes or nodes[(x, y)] == node: #until a node other than this one is visited
            if get(x + dx, y + dy) == '#': #if a wall is ahead, a 90 degree turn needs to be made, however we don't know which way
                for tx, ty in [(-dy, dx), (dy, -dx)]: #try the two possible 90 degree turns
                    if get(x + tx, y + ty) != '#': #turn towards the empty path
                        dx, dy = tx, ty
                        break

            x += dx #move
            y += dy
            distance += 1

        found = nodes[(x, y)] #connected node in this direction
        node.connected.append(Connection(found, distance)) #connect node

def traverse(node, visited): #traverse all connected nodes, returning smallest distance to exit
    if node == end: #exit condition (no distance to end)
        return 0

    best = 0 #longest route to exit

    visited = visited.copy()
    visited.append(node) #mark current node as visited

    for con in node.connected:
        if con.destination in visited: #as long as the same node is never visited twice, we will never step on the same tile twice
            continue

        distance = con.distance + traverse(con.destination, visited)

        best = max(distance, best)

    return best

print(traverse(start, []))