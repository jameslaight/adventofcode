import re

digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

file = open("1/input.txt")

total = 0
for line in file.readlines():
    line = line.replace("\n", "")

    new = ""

    for c in line:
        new += c
        
        for key in digits:
            new = new.replace(key, digits[key] + key) #placing the number in the 'same spot' as its word, without disrupting the word

    new = re.sub("[^0-9]", "", new)
    total += int(new[0] + new[-1])

print(total)

file.close()