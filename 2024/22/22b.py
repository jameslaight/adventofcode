bananas = {}
for line in open("2024/22/input.txt").read().splitlines():
    number = int(line)
    last4difs = (number % 10,)

    seen = set()
    for _ in range(2000):
        cache = number

        number ^= number * 64
        number %= 16777216
        number ^= number // 32
        number %= 16777216
        number ^= number * 2048
        number %= 16777216

        dif = number % 10 - cache % 10
        
        if len(last4difs) == 4:
            last4difs = last4difs[1:] + (dif,)
        else:
            last4difs += (dif,)

        if len(last4difs) == 4:
            if last4difs in seen:
                continue
            seen.add(last4difs)

            if not last4difs in bananas:
                bananas[last4difs] = number % 10
            else:
                bananas[last4difs] += number % 10

print(max(bananas.values()))