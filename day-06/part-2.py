import math

lines = open("input.txt").read().splitlines()

time = int("".join(filter(lambda x: x.isdigit(),lines[0])))
record = int("".join(filter(lambda x: x.isdigit(),lines[1])))

# small adjustment to make sure only distances greater than the record are counted    
sqrtDiscriminant = (time**2 - 4*(record+0.01))**(1/2)
# root being subtracted should be 1 larger (ceil not floor) but this cancels out with making the range inclusive by adding 1
total = (time + sqrtDiscriminant)//2 - (time - sqrtDiscriminant)//2

print(int(total))