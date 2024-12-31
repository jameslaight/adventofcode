import time

for i in range(1, 49 + 1):
    print("Recording star " + str(i))
    time.sleep(i / 49 / 2)

print("Wrapping!")
for i in range(3, 1 - 1, -1):
    print(str(i) + "!")
    time.sleep(1)

print("""VICTORY!
Again! This year felt a lot easier, mostly because I knew some of the tricks AoC uses.
I was also grateful for the lack of cycle questions.
Dynamic programming and recursion remain some of the most entertaining ways to solve problems.
I'll be back next year...
      
Favourite puzzle: Day 21, Keypad Conundrum (This puzzle was hilarious to read as the problem slowly got worse and worse)
Worst puzzle: Day 14, Restroom Redoubt (Part 2 was a cool idea in theory but I pretty much had to blindly guess)
Longest puzzle: Day 17, Chronospatial Computer (This took so long to reverse engineer, misreading the program didn't help)
Hardest puzzle: Day 17, Again (Reverse engineering then writing a program from scratch to take advantage was difficult)""")

#see ya next time