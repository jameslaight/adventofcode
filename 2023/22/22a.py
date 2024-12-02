def parse(coords):
    return tuple(int(i) for i in coords.split(','))

stack = {} #(x, y) mapped to HEIGHT (z) OF THAT COORDINATE
brick_stack = {} #TOPMOST BRICK at (x, y), described as 2 coordinates
falling = {} #LOWEST Z VALUE mapped to LIST OF BRICKS AT THAT VALUE
maximum_z = 0 #HIGHEST MINIMUM Z VALUE of all falling bricks

file = open("22/input.txt")
for line in file.read().splitlines(): #read in bricks
    s1, s2 = line.split("~")
    c1 = parse(s1)
    c2 = parse(s2)
    
    brick = (c1, c2)
    low_z = min(c1[2], c2[2])

    maximum_z = max(low_z, maximum_z) #track highest low_z found

    if low_z in falling:
        falling[low_z].append(brick)
    else:
        falling[low_z] = [brick]
file.close()

removeable = set() #bricks that can be REMOVED (i.e. are not the only dependency of any other brick)
for z in range(maximum_z + 1): #drop bricks which intersect this z value (they cannot interfere with each other, otherwise they would be overlapping in space)
    if z not in falling: #no bricks to drop, next
        continue

    bricks = falling[z] #grab list of falling bricks that intersect this z value
    for brick in bricks:
        c1, c2 = brick

        init_x = min(c1[0], c2[0])
        x_length = abs(c1[0] - c2[0]) + 1
        x_range = range(init_x, init_x + x_length)

        init_y = min(c1[1], c2[1])
        y_length = abs(c1[1] - c2[1]) + 1
        y_range = range(init_y, init_y + y_length)

        z_length = abs(c1[2] - c2[2]) + 1

        high_z = 0 #search STACK to find highest Z value that brick can fall on
        for x in x_range:
            for y in y_range:
                high_z = max(stack[(x, y)] if (x, y) in stack else 0, high_z) #find height at stack (0 if no blocks dropped here)

        dependencies = set() #bricks this brick will FALL ON
        for x in x_range: #drop the block at height = high_z, setting all coordinates on stack and brick_stack
            for y in y_range:
                coords = (x, y)
                if coords in stack and stack[coords] == high_z: #if BRICK HERE is at height BRICK IS FALLING ON
                    dependencies.add(brick_stack[coords]) #this brick is DEPENDENT on the former brick (if all dependencies are removed, brick will fall)

                stack[coords] = high_z + z_length #add height of block to stack
                brick_stack[coords] = brick

        removeable.add(brick) #assume this brick is removeable, for now
        if len(dependencies) == 1: #if this brick is dependent on exactly one brick
            for d in dependencies: #(excuse this line, can't get only element in a set :( oh well)
                if d in removeable:
                    removeable.remove(d) #should that brick be removed this one would fall so it is NOT REMOVEABLE

print(len(removeable))