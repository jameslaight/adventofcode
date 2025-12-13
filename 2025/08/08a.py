class Box:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

class Connection:
    def __init__(self, box1, box2):
        self.box1 = box1
        self.box2 = box2
        self.distSqrd = (box1.x - box2.x)**2 + (box1.y - box2.y)**2 + (box1.z - box2.z)**2

boxes = []
connections = []
for line in open("2025/08/input.txt").read().splitlines():
    split = [int(i) for i in line.split(",")]
    box = Box(split[0], split[1], split[2])

    for other in boxes:
        connections.append(Connection(box, other))

    boxes.append(box)

connections.sort(key=lambda con: con.distSqrd)

network_pointers = {box: set([box]) for box in boxes} #assign each box a set representing its network

for i in range(1000):
    connection = connections[i]
    subsumer = connection.box1
    head_subsumed = connection.box2

    for subsumed in network_pointers[head_subsumed]:
        network_pointers[subsumer].add(subsumed) #add subsumed to subsumer's network
        network_pointers[subsumed] = network_pointers[subsumer] #update pointer for subsumed's network

networks = [] #no duplicates
for network in network_pointers.values():
    if network not in networks:
        networks.append(network)

networks.sort(key=lambda net: len(net), reverse=True) #order distinct networks largest to smallest

product = 1
for i in range(3):
    product *= len(networks[i])
print(product)