import re, math

lines = open("input.txt").read().splitlines()

times = list(map(int,re.findall("\d+",lines[0])))
records = list(map(int,re.findall("\d+",lines[1])))

total = 1

for i in range(len(times)):
    time, record = times[i], records[i]
    # small adjustment to make sure only distances greater than the record are counted
    sqrtDiscriminant = (time**2 - 4*(record+0.01))**(1/2)
    # root being subtracted should be 1 larger (ceil not floor) but this cancels out with making the range inclusive by adding 1
    total *= (time + sqrtDiscriminant)//2 - (time - sqrtDiscriminant)//2

print(int(total))