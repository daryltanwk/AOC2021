# Open file for reading
inputFile = open('input_4', 'rt')

# Number Calling Order
numCallOrder = []
rawNumberCallingOrder = inputFile.readline().split(",")
for x in rawNumberCallingOrder:
    numCallOrder.append(int(x))

# Bingo Cards
curCard = -1
bingoCards = [[]]

for x in inputFile:
    if len(x) == 1:
        bingoCards.append([])
        curCard += 1
    elif len(x) == 15:
        rawRow = x.split()
        row = []
        for y in rawRow:
            row.append(int(y))
        bingoCards[curCard].append(row)
bingoCards.pop()
inputFile.close()


def callNextNumber(card, num):
    results = []
    for row in range(5):
        for digit in range(5):
            if num == card[row][digit]:
                results.append([row, digit])
    return results


def checkWin(card):
    result = [False, "NA"]
    # Row Check
    for x in card:
        if x == ["x", "x", "x", "x", "x"]:
            return [True, "Row"]
    # Column Check
    for x in range(5):
        colResult = ""
        for y in range(5):
            colResult += str((card[y][x]))
        if colResult == "xxxxx":
            return [True, "Col"]
    return result


def calculatePoints(winningCard, lastNum):
    points = 0
    for x in range(5):
        for y in range(5):
            if isinstance(winningCard[x][y], int):
                points += winningCard[x][y]
    return (points*lastNum)


def playCard(card, numOrder):
    roundsToWin = 0
    for x in numOrder:
        callResult = callNextNumber(card, x)
        roundsToWin += 1
        if(callResult != []):
            for y in callResult:
                card[y[0]][y[1]] = "x"
                if checkWin(card)[0]:
                    return [roundsToWin, calculatePoints(card, x), checkWin(card)[1], card]
    return False


"""
PUZZLE ONE & TWO
"""
cardResults = []
cardIndex = 0
for idx, card in enumerate(bingoCards):
    cardResults.append(playCard(card, numCallOrder))
    cardResults[idx].append(idx)

sortedCardResults = sorted(cardResults)
firstPlace = sortedCardResults.pop(0)
lastPlace = sortedCardResults.pop()

print("First Card to Win:", firstPlace[4], "with", firstPlace[1], "points in", firstPlace[0], "rounds by", firstPlace[2])
for x in firstPlace[3]:
    for y in range(5):
        print(str((x[y])).rjust(3), end="")
    print("")
print("")
print("Last Card to Win:", lastPlace[4], "with", lastPlace[1], "points in", lastPlace[0], "rounds by", lastPlace[2])
for x in lastPlace[3]:
    for y in range(5):
        print(str((x[y])).rjust(3), end="")
    print("")
