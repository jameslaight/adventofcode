grid = [[c for c in line] for line in open("2024/12/input.txt").read().splitlines()]
width = len(grid[0])
height = len(grid)

def get(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        return grid[y][x]
    else:
        return "."
    
def remove(x, y):
    grid[y][x] = "."

cost = 0
for x in range(width):
    for y in range(height):
        crop = get(x, y)

        if crop == ".":
            continue

        stack = [] #floodfill time
        stack.append((x, y))
        edges = set()
        area = 0
        scanned = set()
        scanned.add((x, y))
        while stack:
            lx, ly = stack.pop()
            remove(lx, ly)
            area += 1

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx = lx + dx
                ny = ly + dy

                if not (nx, ny) in scanned:
                    if get(nx, ny) == crop:
                        stack.append((nx, ny))
                        scanned.add((nx, ny))
                    else:
                        edges.add((lx, ly, dx, dy))

        categories = [] #categorise the edges
        for edge in edges:
            new_category = [edge]

            merging = []
            for category in categories: #find all categories to merge
                for other in category:
                    distance = abs(edge[0] - other[0]) + abs(edge[1] - other[1]) == 1
                    facing_same_direction = edge[2:4] == other[2:4]
                    if distance == 1 and facing_same_direction: #other is adjacent edge
                        merging.append(category)
                        break

            for merger in merging:
                new_category.extend(merger)
                categories.remove(merger)

            categories.append(new_category) #almost forgot this

        cost += area * len(categories)

print(cost) #can't believe i got this so fast