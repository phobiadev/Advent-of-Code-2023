lines = open("input.txt").read().splitlines()

# set initial to north
grid = ["".join([line[i] for line in lines[::-1]]) for i in range(len(lines[0]))]

def load(grid):
    return sum((i + 1) for col in grid for i in range(len(col)) if col[i] == "O")

def tilt(grid):
    return ["#".join("".join(sorted(chunk)) for chunk in column.split("#")) for column in grid]

def rotate(grid):
    return ["".join([line[i] for line in grid[::-1]]) for i in range(len(grid[0]))]

def cycle(grid):
    for i in range(4):
        grid = tilt(grid)
        grid = rotate(grid)
    return grid

cycles = 1_000_000_000
# assuming sequence becomes periodic
seen = []
i = 0

while True:
    grid = cycle(grid)
    toString = "\n".join(grid)
    if toString in seen:
        n = seen.index(toString)
        break;
    seen.append(toString)
    i += 1

cycleLength = i - n
seenIndex = n + (cycles - n) % cycleLength - 1

print(load(seen[seenIndex].splitlines()))