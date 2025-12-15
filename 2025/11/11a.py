class Device:
    def __init__(self, name):
        self.name = name
        self.out = []

lines = open("2025/11/input.txt").read().splitlines()

device_map = {}

for line in lines:
    names = line.replace(":", "").split(" ")

    for name in names:
        if not name in device_map:
            device = Device(name)
            device_map[name] = device

for line in lines:
    split = line.split(": ")
    name = split[0]
    out = [device_map[name] for name in split[1].split(" ")]
    device_map[name].out.extend(out)

def traverse(device):
    return 1 if device.name == "out" else sum([traverse(out) for out in device.out])

print(traverse(device_map["you"]))