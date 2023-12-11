f = open("input.txt").read()
lines = f.splitlines()

seeds = [int(seed) for seed in lines[0].split(": ")[1].split(" ")]
seedRanges = [seeds[i:i+2] for i in range(0,len(seeds),2)]
groups = [group.split("\n")[1:] for group in f.split("\n\n")[1:]]
groups =  [[list(map(int,line.split(" "))) for line in group] for group in groups]

def getDestination(group,source):
    for line in group:
        if source >= line[1] and source < (line[1]+line[2]):
            return source + (line[0]-line[1]) # difference
    return source

def getLocation(seed):
    x = seed
    for group in groups:
        x = getDestination(group,x)
    return x

# getting the rough minimum location and corresponding seed, checking every {est} seeds in each range
est = 100000
minimum = 100000000
minSeed = 0
for seedRange in seedRanges:
    for seed in range(seedRange[0],seedRange[0]+seedRange[1]+1,est):
        location = getLocation(seed)
        if location < minimum:
            minimum = location
            minSeed = seed

# going through seeds from {est} before the estimated minimum's seed to {est} after to refine and complete search
for seed in range(minSeed-est,minSeed+est):
    location = getLocation(seed)
    if location < minimum:
        minimum = location

print(minimum)