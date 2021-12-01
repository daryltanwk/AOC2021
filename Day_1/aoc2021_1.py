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
