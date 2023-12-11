lines = open("input.txt").read().splitlines()

width = len(lines[0])

newLines = []
for line in lines:
    if line == "."*width:
        newLines += [["."]*width,["."]*width]
    else:
        newLines.append(list(line))

height = len(newLines)

i = 0
while i < width:
    if all(
        line[i] == "."
        for line in newLines
    ):
        for j in range(height):
            newLines[j].insert(i,".")
        i += 1
        width += 1
    i += 1

galaxies = [[x, y] for y in range(height) for x in range(width) if newLines[y][x] == "#"]

total = 0
for g1 in galaxies:
    for g2 in galaxies:
        total += abs(g1[0] - g2[0])
        total += abs(g1[1] - g2[1])

print(total // 2)