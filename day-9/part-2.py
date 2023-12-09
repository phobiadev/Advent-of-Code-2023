from itertools import pairwise

lines = open("input.txt")
lines = [[int(x) for x in line.split(" ")] for line in lines]
      
total = sum(line[0] for line in lines)

for line in lines:
    differences = line[::-1]
    while len(set(differences)) != 1:
        differences = [y-x for (x,y) in pairwise(differences)]
        total += differences[-1]
    
print(total)