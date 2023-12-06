import re, math

lines = open("input.txt").read().splitlines()

times = list(map(int,re.findall("\d+",lines[0])))
records = list(map(int,re.findall("\d+",lines[1])))

total = 1

for i in range(len(times)):
    time, record = times[i], records[i]
    sqrtDiscriminant = (time**2 - 4*record)**(1/2)
    # small adjustments in case roots are integers
    root1 = (time + sqrtDiscriminant)/2 - 0.01
    root2 = (time - sqrtDiscriminant)/2 + 0.01
    total *= math.floor(root1) - math.ceil(root2) + 1

print(total)