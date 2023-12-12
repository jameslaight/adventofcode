class Rng: #naive solution is too slow! time to get smart about this
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def map(self, map_start, map_end, map_increase): #returns a list of new rng objects
        new_start = max(self.start, map_start)
        new_end = min(self.end, map_end)

        if new_start > new_end: #out of range, this operation does nothing
            return [] #return empty for fail
        
        result = [Rng(new_start + map_increase, new_end + map_increase)] #this part has been mapped

        if new_start > self.start: #leftover on the left
            result.append(Rng(self.start, new_start - 1))
        if new_end < self.end: #leftover on the right (or should i say rightover)
            result.append(Rng(new_end + 1, self.end))

        return result

file = open("5/input.txt")

lines = file.read().splitlines()

line = lines.pop(0)
line = line.replace("seeds: ", "")
split = line.split(" ")

data = []
while len(split) > 0:
    start = int(split.pop(0))
    stretch = int(split.pop(0))

    data.append(Rng(start, start + stretch - 1))

while len(lines) > 0:
    for i in range(2):
        lines.pop(0) #remove blank line and extraneous header

    new_data = [] #where new rngs will go
    while True:
        if len(lines) == 0 or not lines[0]: #EOF (stop) or blank line (find next header)
            break

        line = lines.pop(0)

        split = line.split(" ")
        dest = int(split[0])
        start = int(split[1])
        stretch = int(split[2]) #whoops i can't name this 'range'

        i = 0
        while i < len(data): #i need precise control of this loop which is why the index is strange, but loops over data to map all of its values
            d = data[i]

            mapping = d.map(start, start + stretch - 1, dest - start)

            if mapping: #mapping succeeded (in range)
                new_data.append(mapping[0]) #first part is mapped, put into new data

                data.extend(mapping[1:]) #leftover parts, put this data

                data.pop(i) #remove original data at this point
            else:
                i += 1 #i only moves if nothing has been removed

    data.extend(new_data)

result = 0
for d in data:
    if d.start < result or result == 0:
        result = d.start
print(result)

file.close()