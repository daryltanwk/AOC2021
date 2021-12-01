# Open file for reading
inputFile = open('input_1', 'rt')

# Put values into array
inputValues = []
for x in inputFile:
    inputValues.append(int(x))

inputFile.close()
"""
PUZZLE ONE
"""
increaseCount = 0

for currentIndex in range(len(inputValues)-1):
    if inputValues[currentIndex+1]-inputValues[currentIndex] > 0:
        increaseCount += 1

print("Increase Count: ", increaseCount)

"""
PUZZLE TWO
"""
increaseCount2 = 0
for currentIndex2 in range(len(inputValues)-3):
    currentSum = inputValues[currentIndex2]+inputValues[currentIndex2+1]+inputValues[currentIndex2+2]
    nextSum = inputValues[currentIndex2+1]+inputValues[currentIndex2+2]+inputValues[currentIndex2+3]

    if nextSum - currentSum > 0:
        increaseCount2 += 1

print("Increase Count 2: ", increaseCount2)
