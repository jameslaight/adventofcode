reports = []
for line in open("2024/02/input.txt").readlines():
    reports.append([int(l) for l in line.split()])

safe = 0
for report in reports:
    report_safe = False
    for r in range(len(report) + 1):
        modded = list(report) #copy
        if r < len(report):
            modded.pop(r)

        increasing = None

        for i in range(1, len(modded)):
            dif = modded[i] - modded[i - 1]

            if abs(dif) < 1 or abs(dif) > 3:
                break

            local_increasing = dif > 0
            if increasing == None:
                increasing = local_increasing
            elif increasing != local_increasing:
                break
        else:
            report_safe = True
            break
    
    if report_safe:
        safe += 1

print(safe)