file = open("10/input.txt")

pipes = [list(p) for p in file.read().splitlines()] #2d array of pipes
visited = [[False for x in y] for y in pipes] #create grid of false

def getPipe(x, y):
    if y >= 0 and y < len(pipes) and x >= 0 and x < len(pipes[y]):
        return pipes[y][x]
    else:
        return None

drs = {
    (1, 0): ('-', 'L', 'F'),
    (-1, 0): ('-', 'J', '7'),
    (0, 1): ('|', '7', 'F'),
    (0, -1): ('|', 'J', 'L')
} #drections pipes connect to

def isClockwise(dr, pipe): #given a pipe and a direction the pipe is moving TOWARDS, calculate whether the pipe is bending clockwise
    x = dr[0]
    y = dr[1]

    x, y = -y, x #clockwise transformation

    ret = pipe in drs[(x, y)]
    return ret #if pipe supports the clockwise direction we must be going clockwise

for y in range(len(pipes)):
    line = pipes[y]

    for x in range(len(line)):
        if getPipe(x, y) == 'S':
            start_x = x
            start_y = y

pool = [] #pipes that S could be
for dr in drs:
    connection = getPipe(start_x + dr[0], start_y + dr[1])

    if not connection in drs[(-dr[0], -dr[1])]: #if not connected in this drection, skip
        continue

    for possible_pipe in drs[dr]: #add all pipes S could be possibly be to a pool; if 2 of the same type are added, this is the type of S
        if possible_pipe in pool: #if already added, this is the start pipe!
            start_pipe = possible_pipe
        else:
            pool.append(possible_pipe) #add as possibility
pipes[start_y][start_x] = start_pipe

cur_x = start_x
cur_y = start_y
clockwise_corners = []
anticwise_corners = []
while True:
    pipe = getPipe(cur_x, cur_y)
    visited[cur_y][cur_x] = True #mark as visited

    for dr in drs:
        test_x = cur_x + dr[0]
        test_y = cur_y + dr[1]
        if pipe in drs[dr] and not visited[test_y][test_x]: #if pipe connects in the way described by dr
            if pipe in ('L', 'F', '7', 'J'):
                if isClockwise(dr, pipe):
                    clockwise_corners.append((cur_x, cur_y))
                else:
                    anticwise_corners.append((cur_x, cur_y))
            
            cur_x = test_x
            cur_y = test_y
            break
    else: #if natural exit, no pipe found ergo the path has been traversed
        break

if len(clockwise_corners) > len(anticwise_corners): #if this loop is traversed clockwise
    inner_corners = anticwise_corners #inner corners is the list with fewer corners
else:
    inner_corners = clockwise_corners

count = 0
for y in range(len(pipes)):
    inside = False
    for x in range(len(pipes[y])):
        pipe = pipes[y][x]
        if visited[y][x] and pipe == '|' or (x, y) in inner_corners:
            inside = not inside
        elif inside and not visited[y][x]:
            count += 1
            pipes[y][x] = 'I'
print(count)

file.close()