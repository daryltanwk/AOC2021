# Open file for reading

mapOfSea = [[0 for i in range(1000)] for j in range(1000)]

inputFile = open('input_5', 'rt')

for rawLine in inputFile:
    line = rawLine.strip().split(" -> ")
    start = [int(line[0].split(",")[0]), int(line[0].split(",")[1])]
    end = [int(line[1].split(",")[0]), int(line[1].split(",")[1])]
    """
    PUZZLE ONE
    """
    xDirection = 1 if start[0] < end[0] else -1
    yDirection = 1 if start[1] < end[1] else -1
    # Check if line is Horizontal (Y value does not change)
    if start[1] == end[1]:
        currentX = start[0]
        for x in range(abs(start[0]-end[0])+1):
            mapOfSea[currentX][start[1]] += 1
            currentX += xDirection

    # Check if line is Vertical (X value does not change)
    elif start[0] == end[0]:
        currentY = start[1]
        for x in range(abs(start[1]-end[1])+1):
            mapOfSea[start[0]][currentY] += 1
            currentY += yDirection

    ###
    # PUZZLE TWO START - COMMENT OUT THIS SECTION FOR PUZZLE ONE SOLUTION
    ###
    # Handle Diagonals (none of the above cases)
    else:
        currentX = start[0]
        currentY = start[1]
        for x in range(abs(start[0]-end[0])+1):
            mapOfSea[currentX][currentY] += 1
            currentX += xDirection
            currentY += yDirection
    ###
    # PUZZLE TWO END - COMMENT OUT THIS SECTION FOR PUZZLE ONE SOLUTION
    ###

inputFile.close()

puzzleCounter = 0
for a in mapOfSea:
    for b in a:
        if b >= 2:
            puzzleCounter += 1
print("Puzzle Answer:", puzzleCounter)
