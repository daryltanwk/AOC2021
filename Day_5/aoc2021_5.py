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
    # Check if line is Horizontal (X value does not change)
    if start[1] == end[1]:
        direction = 1 if start[0] < end[0] else -1
        currentX = start[0]
        for x in range(abs(start[0]-end[0])+1):
            mapOfSea[currentX][start[1]] += 1
            currentX += direction
    # Check if line is Vertical (Y value does not change)
    elif start[0] == end[0]:
        direction = 1 if start[1] < end[1] else -1
        currentY = start[1]
        for x in range(abs(start[1]-end[1])+1):
            mapOfSea[start[0]][currentY] += 1
            currentY += direction

inputFile.close()

puz1Counter = 0
for a in mapOfSea:
    for b in a:
        if b >= 2:
            puz1Counter += 1
print("Puzzle One Answer:", puz1Counter)
