file = open("5/input.txt")

lines = file.read().splitlines()

line = lines.pop(0)
line = line.replace("seeds: ", "")
data = [int(s) for s in line.split(" ")]

while len(lines) > 0:
    for i in range(2):
        lines.pop(0) #remove blank line and extraneous header

    new_data = [d for d in data] #copy array, this is where i'll put new data (can't just put it directly in, operations will chain)
    while True:
        if len(lines) == 0 or not lines[0]: #EOF (stop) or blank line (find next header)
            break

        line = lines.pop(0)

        split = line.split(" ")
        dest = int(split[0])
        start = int(split[1])
        stretch = int(split[2]) #whoops i can't name this 'range'

        for i in range(len(data)):
            d = data[i]

            if d >= start and d < start + stretch:
                new_data[i] = dest + (d - start)

    data = new_data

print(min(data))

file.close()