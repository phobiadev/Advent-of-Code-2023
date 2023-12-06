import re, math

lines = open("input.txt").read().splitlines()

times = list(map(int,re.findall("\d+",lines[0])))
records = list(map(int,re.findall("\d+",lines[1])))

total = 1

for i in range(len(times)):
    time, record = times[i], records[i]
    # small adjustment to make sure only distances greater than the record are counted
    sqrtDiscriminant = (time**2 - 4*(record+0.01))**(1/2)
    root1 = (time + sqrtDiscriminant)//2
    root2 = (time - sqrtDiscriminant)//2 # should be +1 but this cancels later
    total *= root1 - root2

print(int(total))