from math import lcm

lines = open("input.txt").read().splitlines()
instructions = lines[0]

nodes = {}
for line in lines[2:]:
    nodes[line[:3]] = {"L":line[7:10],"R":line[12:15]}

stepsList = []
starts = list(filter(lambda node: node[-1] == "A",nodes.keys()))
instructionIndex = 0

for i in range(len(starts)):
    steps = 0
    current = starts[i]
    while current[-1] != "Z":
        current = nodes[current][instructions[instructionIndex]]
        if instructionIndex == len(instructions)-1:
            instructionIndex = 0
        else:
            instructionIndex += 1
        steps += 1
    stepsList.append(steps)

print(lcm(*stepsList))