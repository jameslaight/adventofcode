import time

for i in range(1, 23 + 1):
    print("Gathering star " + str(i))
    time.sleep(i / 23 / 2)

print("Decorating tree...")
for i in range(3, 1 - 1, -1):
    print(str(i) + "!")
    time.sleep(1)

print("""VICTORY!
It's a shame that AoC is only 12 puzzles a year now. It feels way less like a gauntlet now, but I think this year
was easier than others anyway.
Still, the puzzles were enjoyable and I can work on my personal projects for a little longer this Christmas!
I still plan to keep on winning, here's to a 3 streak and hopefully longer...
      
Favourite puzzle: Day 11, Reactor (Although not the hardest, I always enjoy using dynamic programming)
Worst puzzle: Day 12, Christmas Tree Farm (I know the last puzzle is usually a joke but c'mon)
Longest puzzle: Day 10, Factory (My library didn't support integer programming and I had to learn Z3)
Hardest puzzle: Day 9, Move Theater (I made an entirely wrong solution before settling on my current method)""")

#i'll be back...