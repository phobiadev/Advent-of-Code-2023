hands = open("input.txt").read().splitlines()
hands = [hand.split(" ") for hand in hands]

cards = list("AKQJT98765432")
cardDict = {}
for i, card in enumerate(cards[::-1]):
    cardDict[card] = i+1

def getType(hand):
    # 7: five of a kind, 6: four of a kind, 5: full house, etc.
    uniques = list(set(hand))
    noofUniques = len(uniques)

    if noofUniques == 1:
        return 7
    if noofUniques == 2:
        countUnique = hand.count(uniques[0])
        if countUnique == 1 or countUnique == 4:
            return 6
        return 5
    if noofUniques == 3:
        structure = sorted([hand.count(uniques[i]) for i in range(3)])
        if structure == [1,1,3]:
            return 4
        return 3
    if noofUniques == 4:
        return 2
    return 1

def getHandValue(hand):
    # assigns a value to a hand based on each card (right to left in increasing importance) and its type
    total = 0
    for i, card in enumerate(hand[::-1]):
        total += cardDict[card] * (16**i)
    total += getType(hand) * (16**5)
    return total

sortedHands = sorted(hands, key=lambda hand: getHandValue(hand[0]))

total = 0
for i in range(len(hands)):
    total += (i + 1) * int(sortedHands[i][1])

print(total)