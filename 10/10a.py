file = open("10/input.txt")

pipes = [list(p) for p in file.read().splitlines()] #2d array

def getPipe(x, y):
    if y >= 0 and y < len(pipes) and x >= 0 and x < len(pipes[y]):
        return pipes[y][x]
    else:
        return '.'

dirs = {
    (1, 0): ('-', 'L', 'F'),
    (-1, 0): ('-', 'J', '7'),
    (0, 1): ('|', '7', 'F'),
    (0, -1): ('|', 'J', 'L')
} #directions pipes connect to

for y in range(len(pipes)):
    line = pipes[y]

    for x in range(len(line)):
        if getPipe(x, y) == 'S':
            start_x = x
            start_y = y

pool = [] #pipes that S could be
for dir in dirs:
    connection = getPipe(start_x + dir[0], start_y + dir[1])

    if not connection in dirs[(-dir[0], -dir[1])]: #if not connected in this direction, skip
        continue

    for possible_pipe in dirs[dir]: #add all pipes S could be possibly be to a pool; if 2 of the same type are added, this is the type of S
        if possible_pipe in pool: #if already added, this is the start pipe!
            start_pipe = possible_pipe
        else:
            pool.append(possible_pipe) #add as possibility
pipes[start_y][start_x] = start_pipe

cur_x = start_x
cur_y = start_y
steps = 0
while True:
    pipe = getPipe(cur_x, cur_y)
    pipes[cur_y][cur_x] = 'S' #mark visited nodes with S
    steps += 1

    for dir in dirs:
        test_x = cur_x + dir[0]
        test_y = cur_y + dir[1]
        if pipe in dirs[dir] and getPipe(test_x, test_y) != 'S': #if pipe connects in the way described by dir
            cur_x = test_x
            cur_y = test_y
            break
    else: #if natural exit, no pipe found ergo the path has been traversed
        break

print(steps // 2) #midway point

file.close()