class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

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

networks_remaining = len(boxes) #number of networks, last connection is made when this = 1
for connection in connections:
    subsumer = connection.box1
    head_subsumed = connection.box2

    if head_subsumed in network_pointers[subsumer]: #if already in network, skip
        continue

    networks_remaining -= 1

    if networks_remaining == 1:
        print(subsumer.x * head_subsumed.x) #<-- the answer
        break

    for subsumed in network_pointers[head_subsumed]:
        network_pointers[subsumer].add(subsumed) #add subsumed to subsumer's network
        network_pointers[subsumed] = network_pointers[subsumer] #update pointer for subsumed's network