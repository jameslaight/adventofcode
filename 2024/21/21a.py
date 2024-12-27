def read(pad):
    out = {}

    for x in range(len(pad[0])):
        for y in range(len(pad)):
            out[pad[y][x]] = (x, y)

    return out

numpad = read((("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), ("", "0", "A")))
dirpad = read((("", "^", "A"), ("<", "v", ">")))

def abstract(route, pads):
    if not pads: #base case
        return route

    pad = pads[0]
    pads = pads[1:]

    new_route = ""
    
    x, y = pad["A"] #start on A
    gap_x, gap_y = pad[""] #gap must be avoided (for some reason??)

    for target in route:
        tx, ty = pad[target]
        dx, dy = tx - x, ty - y

        allowed_axes = [] #False in here means x first is okay, True in here means y first is okay
        if (tx, y) != (gap_x, gap_y): #if moving x axis first would not cross the gap
            allowed_axes.append(False)
        if (x, ty) != (gap_x, gap_y): #if moving y axis first would not cross the gap
            allowed_axes.append(True)

        possible_routes = []
        for y_first in allowed_axes:
            possible_route = ""

            for _ in range(2):
                if y_first:
                    possible_route += ("^" if dy < 0 else "v") * abs(dy)
                else:
                    possible_route += ("<" if dx < 0 else ">") * abs(dx)

                y_first = not y_first

            possible_route += "A"
            possible_routes.append(possible_route)

        best_possible_route_length = -1
        for possible_route in possible_routes:
            possible_route = abstract(possible_route, pads)

            if best_possible_route_length == -1 or len(possible_route) < best_possible_route_length:
                best_possible_route = possible_route
                best_possible_route_length = len(possible_route)

        new_route += best_possible_route
        x, y = tx, ty #update position

    return new_route

total = 0
for line in open("2024/21/input.txt").read().splitlines(): #this problem scares me
    route = abstract(line, [numpad, dirpad, dirpad])
    num = int(line[:-1])
    total += len(route) * num

print(total)