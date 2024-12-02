def copy_part(part):
    clone = {}

    for attr in part:
        clone[attr] = part[attr].copy()

    return clone

def check_part(part): #if part is None or has illegal bounds, return None, else return part
    if part == None:
        return None
    
    for attr in part:
        if part[attr][0] > part[attr][1]:
            return None
        
    return part

class Rule:
    def __init__(self, string):
        if ':' in string: #if has condition
            split = string.split(":")
            self.attr = split[0][0] #attribute
            self.con = split[0][1] #condition
            self.opr = int(split[0][2:]) #operand
            self.dest = split[1]
        else:
            self.con = None
            self.dest = string

    def process(self, part): #returns (accepted, rejected) (None if not applicable)
        accepted = copy_part(part)
        rejected = copy_part(part)
        
        if self.con == '<':
            accepted[self.attr][1] = self.opr - 1 #set max
            rejected[self.attr][0] = self.opr
        elif self.con == '>':
            accepted[self.attr][0] = self.opr + 1 #set min
            rejected[self.attr][1] = self.opr
        else: #unconditional (love)
            rejected = None

        accepted = check_part(accepted)
        rejected = check_part(rejected)
        
        return (accepted, rejected)

class Flow:
    def __init__(self, string):
        self.rules = [Rule(s) for s in string.split(",")]

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

part = {} #min at index 0, max at index 1
for attr in ('x', 'm', 'a', 's'): #this is the worst sorting system
    part[attr] = [1, 4000]

def process(flow, part):
    total = 0

    for rule in flow.rules:
        accepted, part = rule.process(part)

        if accepted != None:
            if rule.dest == 'A': #accepted, add total
                combos = 1 #add total number of combos
                for attr in accepted:
                    combos *= accepted[attr][1] - accepted[attr][0] + 1
                total += combos
            elif rule.dest != 'R': #not rejected, pass to rule.dest
                total += process(flows[rule.dest], accepted)

        if part == None:
            break

    return total

print(process(in_flow, part))