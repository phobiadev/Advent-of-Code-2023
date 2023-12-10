pipes = open("input.txt").read().splitlines()

for i in range(len(pipes)):
    for j in range(len(pipes[0])):
        if pipes[i][j] == "S":
            startX = j
            startY = i
            break;

tiles = {
    "|": {"S":"S","N":"N"}, 
    "-": {"E":"E","W":"W"},
    "L": {"S":"E","W":"N"},
    "J": {"E":"N","S":"W"},
    "7": {"E":"S","N":"W"},
    "F": {"N":"E","W":"S"},
    "S": {"N":"N","S":"S","E":"E","W":"W"}
    }

directionMeanings = {
    "N": (0,-1),
    "E": (1,0),
    "S": (0,1),
    "W": (-1,0)
}

for d in directionMeanings.keys():
    m = directionMeanings[d]
    try: # in case "S" tile on border
        if d in tiles[pipes[startY + m[1]][startX + m[0]]].keys():
            direction = d
            break;
    except:
        continue

steps = 0
currentX, currentY = startX, startY

while pipes[currentY][currentX] != "S" or steps == 0:
    direction = tiles[pipes[currentY][currentX]][direction]
    directionMeaning = directionMeanings[direction]

    currentX += directionMeaning[0]
    currentY += directionMeaning[1]
    steps += 1

print(steps // 2)