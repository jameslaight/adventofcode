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

dynamic_programming = {}
def traverse(device, checkpoints): #don't store checkpoints separately, no loops ergo only one order they can be visited
    args = (device, checkpoints)
    if args in dynamic_programming:
        return dynamic_programming[args]

    if device.name == "out":
        if checkpoints >= 2:
            return 1
        else:
            return 0
    elif device.name in ["dac", "fft"]:
        checkpoints += 1

    routes = sum([traverse(out, checkpoints) for out in device.out])
    dynamic_programming[args] = routes
    return routes

print(dynamic_programming)