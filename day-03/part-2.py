grid = open("input.txt").read().splitlines()
gridLength = len(grid)
lineLength = len(grid[0])

def getNumber(line,i):
    start = i
    end = i
    while start >= 0 and line[start].isdigit():
        start -= 1 # stops 1 after beginning of number due to pre-controlled loop
    while end < lineLength and line[end].isdigit():
        end += 1
    return int(line[start+1 : end])

def getAdjacentNumbers(i,j):
    adjacentNumbers = [] 
    for k in range(max(0, i - 1), min(gridLength, i + 2)):
        for l in range(max(0, j - 1), min(lineLength, j + 2)):
            if grid[k][l].isdigit():
                number = getNumber(grid[k], l)
                if number not in adjacentNumbers:
                    adjacentNumbers.append(number)
    return adjacentNumbers

total = 0

for i in range(gridLength):
    for j in range(lineLength):
        if grid[i][j] == "*":
            adjacentNumbers = getAdjacentNumbers(i,j)
            if len(adjacentNumbers) == 2:
                total += (adjacentNumbers[0] * adjacentNumbers[1])

print(total)