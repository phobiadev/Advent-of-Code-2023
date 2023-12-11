lines = open("input.txt").read().splitlines()
lines = [line.split(":")[1].strip().split(" ") for line in lines]

# removing empty spaces used in input formatting
lines = [list(filter(lambda x: x != "",line)) for line in lines]

total = 0

for line in lines:
    duplicates = len(line) - len(set(line))
    if duplicates > 0:
        total += (2**(duplicates-1))

print(total)