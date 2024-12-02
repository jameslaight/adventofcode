import time

for i in range(1, 49 + 1):
    print("Inputting star " + str(i))
    time.sleep(i / 49 / 2)

print("Pressing the big red button!")
for i in range(3, 1 - 1, -1):
    print(str(i) + "!")
    time.sleep(1)

print("""VICTORY!
This is the first year of AOC I've won!
I've definitely learned a LOT, mostly new algorithms.
Also, I have acquired an entirely new appreciation for recursion.
(I used to dislike it, but now I understand to fully appreciate recursion you have to appreciate recursion first)
'Til next year! I plan keep this streak going as long as I can...

Favourite puzzle: Day 12, Hot Springs (Recursion is divine. On the other hand, I now fear the characters ?#.)
Worst puzzle: Day 8, Haunted Wasteland (How does that work?? Oh, I can just use LCM. Wait. How does that work??)
Longest puzzle: Day 10, Pipe Maxe (I initially tried to write floodfill and its answer was off by 5 ;_;)
Hardest puzzle: Day 21, Step Counter (WHY do you need to walk 26501365 steps? And EXACTLY that many, as well??)""")

#until next time...