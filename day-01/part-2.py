lines = open("input.txt").readlines()

nums = ["one","two","three","four","five","six","seven","eight","nine"]

def firstDigit(line):
    for i in range(len(line)):
        char = line[i]
        if char.isnumeric():
            return char
        for j, num in enumerate(nums):
            if (i + len(num)) < len(line):
                if line[i:i+len(num)] == num:
                    return str(j + 1)
        
def lastDigit(line):
    for i in range(len(line)-1,-1,-1):
        char = line[i]
        if char.isnumeric():
            return char
        for j, num in enumerate(nums):
            if i >= len(num):
                if line[i-len(num)+1:i+1] == num:
                    return str(j + 1)

total = 0

for line in lines:
    total += int(firstDigit(line) + lastDigit(line))

print(total)