reports = []
for line in open("2024/02/input.txt").readlines():
    reports.append([int(l) for l in line.split()])

safe = 0
for report in reports:
    increasing = None
    dampened = False

    for i in range(1, len(report)):
        dif = report[i] - report[i - 1]

        if abs(dif) < 1 or abs(dif) > 3:
            if dampened:
                dampened = True
                continue
            
            break

        local_increasing = dif > 0
        if increasing == None:
            increasing = local_increasing
        elif increasing != local_increasing:
            break
    else:
        safe += 1

print(safe)