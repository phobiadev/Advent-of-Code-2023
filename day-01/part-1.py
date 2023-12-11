lines = open("input.txt").readlines()

def firstDigit(line):
    for char in line:
        if char.isnumeric():
            return char

total = 0

for line in lines:
    total += int(firstDigit(line) + firstDigit(line[::-1]))

print(total)