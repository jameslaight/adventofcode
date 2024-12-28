all = set()
connections = {}

def connect(s, d):
    all.add(s)
    all.add(d)

    if s not in connections:
        connections[s] = set()

    connections[s].add(d)

for line in open("2024/23/input.txt").read().splitlines():
    c1, c2 = line.split("-")

    connect(c1, c2)
    connect(c2, c1)

dynamic_programming_3 = {}
def grow(computers):
    if computers in dynamic_programming_3:
        return dynamic_programming_3[computers]

    mutuals = set(connections[computers[0]])

    for i in range(1, len(computers)):
        mutuals = mutuals.intersection(connections[computers[i]])

    biggest = computers
    for mutual in mutuals:
        computers_copy = computers + (mutual,)
        computers_copy = tuple(sorted(computers_copy))
        result = grow(computers_copy)

        if len(result) > len(biggest):
            biggest = result

    dynamic_programming_3[computers] = biggest
    return biggest

biggest = []
for a in all:
    result = grow((a,))
    if len(result) > len(biggest):
        biggest = result

print(",".join(list(biggest)))