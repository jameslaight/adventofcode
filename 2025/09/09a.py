squares = [([int(i) for i in line.split(",")]) for line in open("2025/09/input.txt").read().splitlines()]

best = 0
for i in range(len(squares)):
    for j in range(i + 1, len(squares)):
        sq_i, sq_j = squares[i], squares[j]

        width = abs(sq_i[0] - sq_j[0]) + 1 #+1 for fencepost problem
        height = abs(sq_i[1] - sq_j[1]) + 1
        area = width * height #shocking
        best = max(best, area)

print(best)