connections = set()
tonnections = []

for line in open("2024/23/input.txt").read().splitlines():
    c1, c2 = line.split("-")

    if c1 > c2:
        c1, c2 = c2, c1 #sort alphabetically

    connections.add((c1, c2))

    if c1[0] == "t" or c2[0] == "t":
        tonnections.append((c1, c2))

lans = set()
for i in range(len(tonnections)):
    for j in range(i+1, len(tonnections)):
        c1, c2 = tonnections[i], tonnections[j]

        cs = []
        shared = None
        for c in c1, c2:
            for cc in c:
                if cc in cs:
                    shared = cc
                else:
                    cs.append(cc)

        if shared == None:
            continue

        t1, t2 = c1[0] if c1[0] != shared else c1[1], c2[0] if c2[0] != shared else c2[1]
        if t1 > t2:
            t1, t2 = t2, t1
        
        if (t1, t2) in connections:
            end = tuple(sorted([t1, t2, shared]))
            lans.add(end)

print(len(lans))