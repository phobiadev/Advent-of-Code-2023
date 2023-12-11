pipes = open("input.txt").read().splitlines()

height = len(pipes)
width = len(pipes[0])

for i in range(height):
    for j in range(width):
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

abstract = [[0 for i in range(width)] for j in range(height)]
steps = 0
currentX, currentY = startX, startY
c = ""

while pipes[currentY][currentX] != "S" or steps == 0:
    direction = tiles[pipes[currentY][currentX]][direction]
    directionMeaning = directionMeanings[direction]

    currentX += directionMeaning[0]
    currentY += directionMeaning[1]
    steps += 1

    # creating abstracted grid, where tiles that are part of the loop are 1 and other tiles are 0 (makes ray casting more efficient)
    abstract[currentY][currentX] = 1
    
total = 0

# diagonal ray casting ↘
for i in range(height):
    for j in range(width):
        if not abstract[i][j]:
            crosses = 0
            x = j
            y = i
            while x < width  and y < height:
                c = pipes[y][x]
                # ↘ ray does not cross if tile is L or 7
                if abstract[y][x] and c not in "L7":
                    crosses += 1
                x += 1
                y += 1

            if crosses % 2 == 1:
                total += 1

print(total)