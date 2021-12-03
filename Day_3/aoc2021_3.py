# Open file for reading
inputFile = open('input_3', 'rt')

# Put values into array
inputValues = []
for x in inputFile:
    inputValues.append(x.strip("\n"))

inputFile.close()
rowLength = len(inputValues[0])


def mostCommonDigit(inputList, pos):
    zeroCount = 0
    oneCount = 0
    for w in inputList:
        if w[pos] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        return "0"
    elif oneCount > zeroCount:
        return "1"
    else:
        return "x"


def evalRating(type, inputList, targetBit=0):
    if len(inputList) == 1:
        return inputList
    mcb = mostCommonDigit(inputList, targetBit)
    if type == "oxy":
        typeBit = "0" if mcb == "0" else "1"
    elif type == "co2":
        typeBit = "1" if mcb == "0" else "0"
    newList = list(filter(lambda x: x[targetBit] == typeBit, inputList))
    return evalRating(type, newList, targetBit+1)


"""
PUZZLE ONE
"""
gammaVal = ""
epsilonVal = ""

for y in range(0, rowLength):
    gammaVal += mostCommonDigit(inputValues, y)

for y in gammaVal:
    if y == "0":
        epsilonVal += "1"
    else:
        epsilonVal += "0"

print("Gamma: ", gammaVal, "(", int(gammaVal, 2), ")")
print("Epsilon: ", epsilonVal, "(", int(epsilonVal, 2), ")")
print("Puzzle One Answer:", int(gammaVal, 2)*int(epsilonVal, 2), "\n\n")

"""
PUZZLE TWO
"""

oxyVal = evalRating("oxy", inputValues)
co2Val = evalRating("co2", inputValues)

print("Oxy:", oxyVal[0], "(", int(oxyVal[0], 2), ")")
print("CO2:", co2Val[0], "(", int(co2Val[0], 2), ")")
print("Puzzle Two Answer:", int(oxyVal[0], 2)*int(co2Val[0], 2))
