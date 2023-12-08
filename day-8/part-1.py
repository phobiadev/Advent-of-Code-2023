lines = open("input.txt").read().splitlines()
instructions = lines[0]

nodes = {}
for line in lines:
    nodes[line[:3]] = {"L":line[7:10],"R":line[12:15]}

steps = 0
current = "AAA"
instructionIndex = 0

while current != "ZZZ":
    current = nodes[current][instructions[instructionIndex]]
    if instructionIndex == len(instructions)-1:
        instructionIndex = 0
    else:
        instructionIndex += 1
    steps += 1

print(steps)