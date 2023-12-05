f = open("input.txt").read()
lines = f.splitlines()

seeds = [int(seed) for seed in lines[0].split(": ")[1].split(" ")]
groups = [group.split("\n")[1:] for group in f.split("\n\n")[1:]]
groups =  [[list(map(int,line.split(" "))) for line in group] for group in groups]

def getDestination(group,source):
    for line in group:
        if source >= line[1] and source < (line[1]+line[2]):
            return source + (line[0]-line[1]) # difference
    return source

minimum = 10000000000
for seed in seeds:
    x = seed
    for group in groups:
        x = getDestination(group,x)
    if x < minimum:
        minimum = x

print(minimum)