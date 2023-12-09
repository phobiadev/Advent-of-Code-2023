from itertools import pairwise

lines = open("input.txt")
lines = [[int(x) for x in line.split(" ")] for line in lines]
    
total = 0

for line in lines:
    differences = line
    prediction = line[-1]
    while len(set(differences)) != 1:
        differences = [y-x for (x,y) in pairwise(differences)]
        prediction += differences[-1]
    total += prediction
    
print(total)