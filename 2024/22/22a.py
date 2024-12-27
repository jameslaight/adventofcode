total = 0 #this looks suspiciously easy

for line in open("2024/22/input.txt").read().splitlines():
    number = int(line)

    for _ in range(2000):
        number ^= number * 64
        number %= 16777216
        number ^= number // 32
        number %= 16777216
        number ^= number * 2048
        number %= 16777216

    total += number

print(total)