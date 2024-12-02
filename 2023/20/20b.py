from math import lcm #did not like this one. too many assumptions about import format

class Module:
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def pulse(self, source, type): #give boolean and source, returns pulse this module wants to send to its outputs - False for low, True for high
        return type #by default, broadcast type to outputs

class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)

        self.on = False

    def pulse(self, source, type): #polymorphism!
        if not type: #if low pulse
            self.on = not self.on #flip state

            return self.on
        
        return None

class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)

        self.memory = {}

    def pulse(self, source, type):
        self.memory[source] = type #update memory

        for i in self.inputs: #send high if all not all inputs are high
            if not self.fetch(i):
                return True

        return False #send low if all inputs are high

    def fetch(self, source): #return True if last pulse from source was high, else False
        return source in self.memory and self.memory[source]
    
file = open("20/input.txt")
lines = file.read().splitlines()
file.close()

modules = {}

for line in lines: #first pass, creating modules
    name = line.split(" -> ")[0]

    if name[0] == '%':
        name = name[1:]
        module = FlipFlop(name)
    elif name[0] == '&':
        name = name[1:]
        module = Conjunction(name)
    else:
        module = Module(name)

    modules[name] = module

    if name == "broadcaster":
        broadcaster = module

for line in lines: #second pass, linking modules
    split = line.split(" -> ")
    name = split[0]
    if name[0] in ('%', '&'):
        name = name[1:]

    module = modules[name]
    input_names = split[1].split(", ")

    for i in input_names:
        if i in modules:
            input_module = modules[i]
        else: #discovered new module that is an output only, add to list
            input_module = Module(i)
            modules[i] = input_module

        module.outputs.append(input_module)
        input_module.inputs.append(module)

broadcaster = modules["broadcaster"]
goal_module = modules["rx"].inputs[0]
presses = 0
periods = {}
while len(periods) < len(goal_module.inputs): #until all periods collected
    queue = [(broadcaster, False)]
    presses +=1 #button press

    while len(queue) > 0:
        module, type = queue.pop(0)

        for output in module.outputs:
            result = output.pulse(module, type)

            if result == None: #ignored
                continue

            if output == goal_module and type: #if given to conjunction that connects to rx and high, save the period
                if not module in periods:
                    periods[module] = presses

            queue.append((output, result))

print(lcm(*periods.values()))