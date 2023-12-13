notes = open("input.txt").read().split("\n\n")
notes = [note.splitlines() for note in notes]

def mirror(note):
    for i in range(1,len(note)):
        left = note[:i]
        right = note[i:]

        if len(left) < len(right):
            right = right[:len(left)]
        elif len(left) > len(right):
            left = left[len(left) - len(right):]
        right = right[::-1]

        if left == right:
            return i
    return 0

total = 0
for note in notes:
    m = mirror(note) *100
    if not m:
        m = mirror(["".join([row[i] for row in note]) for i in range(len(note[0]))])
    total += m

print(total)