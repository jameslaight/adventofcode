def hash(code):
    val = 0
    for c in code:
        val += ord(c)
        val *= 17
        val %= 256
    return val

file = open("15/input.txt")

codes = file.readline().replace("\n", "").split(",")

boxes = [[] for i in range(256)]

total = 0
for code in codes:
    if '=' in code:
        split = code.split('=')
        label = split[0]
        focal = int(split[1])

        box = boxes[hash(label)]
        for i in range(len(box)):
            if box[i][0] == label:
                box[i] = ((label, focal))
                break
        else:
            box.append((label, focal))
    else:
        label = code[:-1]

        box = boxes[hash(label)]
        for i in range(len(box)):
            if box[i][0] == label:
                box.pop(i)
                break

total = 0
for i in range(len(boxes)):
    box = boxes[i]

    for j in range(len(box)):
        total += (i + 1) * (j + 1) * box[j][1]
    
for box in boxes:
    print(box)
print(total)

file.close()