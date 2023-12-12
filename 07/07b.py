class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

file = open("7/input.txt")

hands = []
for line in file.read().splitlines():
    split = line.split(" ")
    
    cards = split[0]
    bid = int(split[1])

    counts = {} #count cards types, except jokers
    jokers = 0 #number of jokers
    for c in cards:
        if c == 'J':
            jokers += 1
        elif c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    sorted_count = sorted(counts.values(), reverse=True) #sort the values to check for hand types
    if len(sorted_count) > 0: #ensure there is a most common card (aside from jokers)
        sorted_count[0] += jokers #best hand is always made by making all jokers the most common card
    else: #if hand is entirely jokers just set the count
        sorted_count.append(jokers)

    if sorted_count[0] == 5:
        id = 'a'
    elif sorted_count[0] == 4:
        id = 'b'
    elif sorted_count[0] == 3 and sorted_count[1] == 2:
        id = 'c'
    elif sorted_count[0] == 3:
        id = 'd'
    elif sorted_count[0] == 2 and sorted_count[1] == 2:
        id = 'e'
    elif sorted_count[0] == 2:
        id = 'f'
    else:
        id = 'g'

    cards = id + cards #affix ID to cards

    for sub in [("K", "B"), ("Q", "C"), ("J", "Z"), ("T", "D")]: #replace symbols with alphabet (J is now Z)
        cards = cards.replace(sub[0], sub[1])
    for i in range(2, 9 + 1): #replace 2-9 with numbers N-E (reverse to have large numbers have larger ASCII values)
        cards = cards.replace(str(i), chr(78 - i))

    hands.append(Hand(cards, bid))

hands.sort(key=lambda h: h.cards, reverse=True) #sort in ASCENDING order to apply bids going upwards

total = 0
multiplier = 1
for hand in hands:
    total += hand.bid * multiplier
    multiplier += 1

print(total)

file.close()