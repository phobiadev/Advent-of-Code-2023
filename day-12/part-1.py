from functools import cache

lines = open("input.txt").read().splitlines()
structures = [tuple(map(int,line.split(" ")[1].split(","))) for line in lines]
lines = [line.split(" ")[0] for line in lines]

@cache
def countArrangements(line, structure):  
    line = line.strip(".")

    if len(structure) == 0:
        return int(all(s != '#' for s in line))
    if len(line) < sum(structure):
        return 0

    current = 0

    if "." not in line[:structure[0]] and ((len(line) == structure[0]) or (len(line) > structure[0] and line[structure[0]] != "#")):
        current = countArrangements(line[structure[0]+1:],structure[1:])
    
    # entire structure can occur again?
    if line[0] == "?":
        current += countArrangements(line[1:], structure)

    return current

print(sum(countArrangements(lines[i],structures[i]) for i in range(len(lines))))