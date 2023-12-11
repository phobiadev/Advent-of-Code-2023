lines = open("input.txt").read().splitlines()
lines = [line.split(":")[1].strip().split(" ") for line in lines]

lines = [list(filter(lambda x: x != "",line)) for line in lines]

copies = [1]*len(lines)

for i in range(len(lines)):
    duplicates = len(lines[i])-len(set(lines[i]))
    for j in range(i+1,i+duplicates+1):
        copies[j] += copies[i]

total = sum(copies)

print(total)