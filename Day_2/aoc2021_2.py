# Open file for reading
inputFile = open('input_2', 'rt')

# Put values into array
inputValues = []
for x in inputFile:
    item = x.split()
    inputValues.append([item[0], int(item[1])])

inputFile.close()

"""
PUZZLE ONE
"""
horizontal = 0
depth = 0

for x in inputValues:
    if(x[0] == 'forward'):
        horizontal += x[1]
    elif(x[0] == 'up'):
        depth -= x[1]
    elif(x[0] == 'down'):
        depth += x[1]

print("Horizontal: ", horizontal)
print("Depth: ", depth)
print("Puzzle 1 Answer: ", horizontal, " x ", depth, " = ", horizontal*depth)
