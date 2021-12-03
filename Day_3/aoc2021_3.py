# Open file for reading
inputFile = open('input_3', 'rt')

# Put values into array
inputValues = []
for x in inputFile:
    inputValues.append(x.strip("\n"))

inputFile.close()

"""
PUZZLE ONE
"""
gammaVal = ""
epsilonVal = ""
for y in range(0, 12):
    zeroCount = 0
    oneCount = 0
    for z in inputValues:
        if z[y] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount > oneCount:
        gammaVal += "0"
    else:
        gammaVal += "1"

for y in gammaVal:
    if y == "0":
        epsilonVal += "1"
    else:
        epsilonVal += "0"

print("Gamma: ", gammaVal, "(", int(gammaVal, 2), ")")
print("Epsilon: ", epsilonVal, "(", int(epsilonVal, 2), ")")
print("Puzzle One Answer:", int(gammaVal, 2)*int(epsilonVal, 2))
