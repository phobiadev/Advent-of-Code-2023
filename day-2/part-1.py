# The nicest way of solving this problem would probably have involved a dictionary of colour values for each game, and checking wih the max() function for each colour, but this seemed easier (and faster?)

lines = open("input.txt").readlines()
lines = ["".join(line.split(": ")[1:]) for line in lines]

maxes = [12,13,14]
colours = ["red","green","blue"]

total = 0

for i in range(len(lines)):
    valid = True
    for j in range(3):
        for k in range(1,50):
            if f"{maxes[j]+k} {colours[j]}" in lines[i]:
                valid = False
                break;
    if valid:
        total += (i+1)

print(total)