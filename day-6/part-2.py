import math

lines = open("input.txt").read().splitlines()

time = int("".join(filter(lambda x: x.isdigit(),lines[0])))
record = int("".join(filter(lambda x: x.isdigit(),lines[1])))

# small adjustment to make sure only distances greater than the record are counted    
sqrtDiscriminant = (time**2 - 4*(record+0.01))**(1/2)
root1 = (time + sqrtDiscriminant)//2
root2 = (time - sqrtDiscriminant)//2 # should be +1 but this cancels late
total = root1 - root2

print(int(total))