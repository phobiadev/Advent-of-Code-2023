import re

grid = open("input.txt").read().splitlines()
gridLength = len(grid)
lineLength = len(grid[0])

def findNumbers(line):
    return [{"span":list(m.span()),"value":int(m.group())} for m in re.finditer(r'\d+', line)]
    
def partNumberSum(lineIndex):
    candidates = findNumbers(grid[lineIndex])
    lineSum = 0

    for candidate in candidates:
        valid = False
        for i in range(max(0, lineIndex - 1), min(gridLength, lineIndex + 2)):
            for c in grid[i][max(0, candidate["span"][0] - 1) : min(lineLength, candidate["span"][1] + 1)]:
                if c not in "1234567890.":
                    valid = True
        if valid:
            lineSum += candidate["value"]

    return lineSum

total = 0

for i in range(gridLength):
    total += partNumberSum(i)

print(total)