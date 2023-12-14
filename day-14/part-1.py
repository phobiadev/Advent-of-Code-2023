lines = open("input.txt").read().splitlines()

# get columns to tilt
grid = ["".join([line[i] for line in lines[::-1]]) for i in range(len(lines[0]))]

def load(grid):
    return sum((i + 1) for col in grid for i in range(len(col)) if col[i] == "O")

def tilt(grid):
    return ["#".join("".join(sorted(chunk)) for chunk in column.split("#")) for column in grid]

grid = tilt(grid)
print(load(grid))