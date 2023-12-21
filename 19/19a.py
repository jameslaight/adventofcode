class Rule:
    def __init__(self, string):
        if ':' in string: #if has condition
            split = string.split(":")
            self.var = split[0][0] #variable
            self.con = split[0][1] #condition
            self.opr = int(split[0][2:]) #operand
            self.dest = split[1]
        else:
            self.con = None
            self.dest = string

    def test(self, part):
        if self.con == '<':
            return part[self.var] < self.opr
        elif self.con == '>':
            return part[self.var] > self.opr
        else: #unconditional (love)
            return True

class Flow:
    def __init__(self, string):
        self.rules = [Rule(s) for s in string.split(",")]

    def process(self, part): #returns destination
        for rule in self.rules:
            if rule.test(part):
                return rule.dest
            
        raise RuntimeError("Flow failed to process part.") #this shouldn't run

file = open("19/input.txt")
lines = file.read().splitlines()
file.close()

in_flow = None
flows = {}
while lines[0]: #read flows
    line = lines.pop(0)
    line = line[:-1] #shave off }
    split = line.split("{")
    name = split[0]
    flow = Flow(split[1])

    if name == "in":
        in_flow = flow
    flows[name] = flow

lines.pop(0) #blank line

total = 0
for line in lines: #remaining lines are parts
    part = {}
    
    for attr in line[1:-1].split(","):
        split = attr.split("=")
        part[split[0]] = int(split[1])

    flow = in_flow
    while True:
        dest = flow.process(part)

        if dest == 'A':
            for attr in part: #accepted, sum attributes
                total += part[attr]

            break
        elif dest == 'R':
            break
        else:
            flow = flows[dest]

print(total)