disk = []
inp = [int(c) for c in open("2024/09/input.txt").read()]
if len(inp) % 2: #there must be a blank at the end for the algorithm to work
    inp.append(0) #append it if it's not there

for i in range(0, len(inp), 2):
   disk.append((i // 2, inp[i])) #file
   disk.append((-1, inp[i + 1])) #blank

for id in range(len(disk) // 2 - 1, -1, -1): #file ids in decreasing order
    for i in range(len(disk) - 2, -1, -2): #step backwards through files
        if disk[i][0] == id:
            file = disk[i] #save file for later
            file_index = i #find index of file

    found = False
    for i in range(1, len(disk), 2): #step forwards through blanks
        if i > file_index:
            break
        
        if disk[i][1] >= file[1]: #if blank is long enough
            found = True
            blank_index = i
            break

    if not found: #do not move
        continue

    collapse = 0 #collapse file and blanks either side into 1 blank
    for _ in range(3):
        collapse += disk.pop(file_index - 1)[1]
    disk.insert(file_index - 1, (-1, collapse))

    blank = disk[blank_index]
    disk[blank_index] = (blank[0], blank[1] - file[1]) #subtract file size from blank                                                                                           

    disk.insert(blank_index, file) #insert the file
    disk.insert(blank_index, (-1, 0)) #insert dummy (no space between)

total = 0
pos = 0
for d in disk:
    for i in range(d[1]):
        total += max(d[0], 0) * pos
        pos += 1

print(total)