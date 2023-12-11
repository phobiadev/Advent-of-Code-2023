lines = open("input.txt").read().splitlines()

width = len(lines[0])
height = len(lines)

expansion = 1000000
expansionRows = [i for i in range(height) if len(set(lines[i])) == 1]
expansionColumns = [i for i in range(width) if len(set([line[i] for line in lines])) == 1]

galaxies = [[x, y] for y in range(height) for x in range(width) if lines[y][x] == "#"]

def between(a,b):
    return range(min(a,b),max(a,b))

total = 0

for g1 in galaxies:
    for g2 in galaxies:
        rowIndexes = between(g1[1],g2[1])
        expandedRows = len([i for i in rowIndexes if i in expansionRows])
        total += expandedRows * expansion + len(rowIndexes) - expandedRows
        
        columnIndexes = between(g1[0],g2[0])
        expandedColumns = len([i for i in columnIndexes if i in expansionColumns])
        total += expandedColumns * expansion + len(columnIndexes) - expandedColumns
            
print(total // 2)