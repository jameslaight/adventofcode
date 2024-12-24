file = open("2024/17/input.txt")
for i in range(4): #input consumption
    line = file.readline()

program = [int(i) for i in file.readline().split()[1].split(",")]

def reveng(number, targets):
    if not targets:
        return number
    
    number = number * 8
    
    target = targets[-1]
    targets = targets[:-1]

    for i in range(8):
        a = number + i

        b = a % 8
        b ^= 1
        c = a // (2**b)
        b ^= 5
        b = b ^ c
        
        if b % 8 == target:
            answer = reveng(number + i, targets)
            
            if answer != None: #check if this path is possible
                return answer
        
    return None

print(reveng(0, program))