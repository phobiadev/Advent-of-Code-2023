import math

lines = open("input.txt").read().splitlines()

time = int("".join(filter(lambda x: x.isdigit(),lines[0])))
record = int("".join(filter(lambda x: x.isdigit(),lines[1])))
    
sqrtDiscriminant = (time**2 - 4*record)**(1/2)
# small adjustment in case roots are integers
root1 = (time + sqrtDiscriminant)/2 - 0.01
root2 = (time - sqrtDiscriminant)/2 + 0.01

total = math.floor(root1) - math.ceil(root2) + 1

print(total)