class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, other):
        self.connections.append(other)
        other.connections.append(self)

    def disconnect(self, other):
        self.connections.remove(other)
        other.connections.remove(self)

file = open("25/input.txt") #we're almost there!
lines = file.read().splitlines()
file.close()

nodes = {}

def get_node(name):
    if name in nodes:
        return nodes[name]
    else:
        node = Node(name)
        nodes[name] = node
        return node

for line in lines: #read input into nodes
    split = line.split(": ")

    first = get_node(split[0])

    for second in [get_node(s) for s in split[1].split()]:
        first.connect(second)

class Connection:
    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b

    def __eq__(self, other): #either way round
        return (self.node_a == other.node_a and self.node_b == other.node_b) or (self.node_a == other.node_b and self.node_b == other.node_a)

    def __hash__(self):
        return hash((self.node_a, self.node_b)) + hash((self.node_b,self.node_a)) #funny hash algorithm

edges = {} #count of edges that are traversed
for start in nodes.values(): #breadth first search all
    added = set()
    added.add(start)
    queue = [start]

    paths = {start: []} #maps nodes to lists of connections required to get there

    while len(queue) > 0:
        current = queue.pop(0)
        
        for con in current.connections:
            if not con in added:
                queue.append(con)
                added.add(con)

                obj = Connection(current, con)
                path = paths[current].copy() #grab the path here
                path.append(obj) #append the connection to it
                paths[con] = path #assign it to be the new path of con
                
                for p in path:
                    if p in edges:
                        edges[p] += 1
                    else:
                        edges[p] = 1

for i in range(3): #remove the most-traversed edge, 3 times, to cut the graph in two
    best = None
    best_count = 0

    for edge in edges:
        count = edges[edge]
        if count > best_count: #always > 0
            best = edge
            best_count = count

    best.node_a.disconnect(best.node_b)
    del edges[best]

start = list(nodes.values())[0] #arbitrary node to find section from
section = set()
section.add(start)

queue = [start]
while len(queue) > 0: #time to rewrite BFS i guess
    current = queue.pop(0)

    for con in current.connections:
        if not con in section:
            queue.append(con)
            section.add(con)

section_size = len(section)
print(section_size * (len(nodes) - section_size)) #final answer!