import re
import math

file = open("6/input.txt")
lines = file.read().splitlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace(" ", "")

time = int(lines[0].replace("Time:", ""))
distance = int(lines[1].replace("Distance:", ""))

a = 1
b = -time
c = distance
sqrt_discriminant = math.sqrt(b*b - 4*a*c)

lower_speed = (-b - sqrt_discriminant) / 2 * a
lower_speed = math.floor(lower_speed + 1) #remove 1 then round down (removes non-integers and solution where we tie with other boat)

upper_speed = (-b + sqrt_discriminant) / 2 * a
upper_speed = math.ceil(upper_speed - 1) #similar logic

print(upper_speed - lower_speed + 1) #+1 because range is inclusive

file.close()