def read(pad):
    out = {}

    for x in range(len(pad[0])):
        for y in range(len(pad)):
            out[pad[y][x]] = (x, y)

    return out

numpad = read((("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), ("", "0", "A")))
dirpad = read((("", "^", "A"), ("<", "v", ">")))

dynamic_programming_2 = {}
def abstract(route, pads):
    if not pads: #base case
        return len(route)
    
    state = (route, len(pads))
    if state in dynamic_programming_2:
        return dynamic_programming_2[state]

    pad = pads[0]
    pads = pads[1:]

    total_distance = 0
    
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

        best_distance = min([abstract(possible_route, pads) for possible_route in possible_routes]) #length of shortest route

        total_distance += best_distance
        x, y = tx, ty #update position

    dynamic_programming_2[state] = total_distance
    return total_distance

total = 0
for line in open("2024/21/input.txt").read().splitlines():
    route = abstract(line, [numpad] + [dirpad] * 25) #oh COME ON
    num = int(line[:-1])
    total += route * num

print(total)