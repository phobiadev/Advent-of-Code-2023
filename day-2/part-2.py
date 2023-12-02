# (see part 1)

lines = open("input.txt").readlines()

colours = ["red","green","blue"]

total = 0

for i in range(len(lines)):
    power = 1
    for j in range(3):
        minRequired = 0
        for k in range(1,50):
            if f"{k} {colours[j]}" in lines[i]:
                minRequired = k
        power *= minRequired
    total += power

print(total)