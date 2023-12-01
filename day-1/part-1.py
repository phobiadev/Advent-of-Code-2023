lines = open("input.txt").readlines()

total = 0

def firstDigit(line):
    for char in line:
        if char.isnumeric():
            return char

def lastDigit(line):
    for char in line[::-1]:
        if char.isnumeric():
            return char

for line in lines:
    total += int(firstDigit(line) + lastDigit(line))

print(total)