print("minimum size is 1x1")
height = int(input("enter height of board:\n"))
width = int(input("enter width of board:\n"))
winLength = int(input("enter amount of symbols in a row needed to win:\n"))

validCoordinates = [11]
grid = {}
counter2 = 0
symbol = "X"

while len(validCoordinates) != height * width:
    coordinate = list(str(validCoordinates[0]))
    firstDigit = int(coordinate[0])
    secondDigit = int(coordinate[1])

    if secondDigit == width:
        validCoordinates = [int(str(firstDigit + 1) + "1")] + validCoordinates
    else:
        validCoordinates = [int(str(firstDigit) + str(secondDigit + 1))] + validCoordinates

for coordinate in reversed(validCoordinates):
    grid[coordinate] = "_"

def printGrid():
    string = ""
    counter = 0 

    for coordinate in grid:
        string += grid[coordinate]
        string += " "
        counter += 1
        if counter == width:
            string += "\n"
            counter = 0

    print(string)

def winCondition():
    rowsCounter = 0
    columnCounter = 0

    for count in range(1, int((len(grid) / width)) + 1):
        rowsMatch = None
        for position in range(1, width + 1):
            element = grid[int(str(count) + str(position))]
            if rowsCounter == winLength: return True
            if element == "_": continue

            if rowsCounter == 0:
                rowMatch = element
                rowsCounter += 1
            elif rowMatch == element:
                rowsCounter += 1
            else:
                rowMatch = element
                rowsCounter = 0

    for count in range(1, int((len(grid) / height)) + 1):
        columnMatch = None
        for position in range(1, height + 1):
            element = grid[int(str(position) + str(count))]
            if columnCounter == winLength: return True
            if element == "_": continue

            if columnCounter == 0:
                columnMatch = element
                columnCounter += 1
            elif columnMatch == element:
                columnCounter += 1
            else:
                columnMatch = element
                columnCounter = 0

    if columnCounter == winLength or rowsCounter == winLength: return True
    return False

def activateRound():
    global symbol

    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"

    validChar = False
    tie = False
    userInput = int(input("Enter a coordinate:\n"))

    for coordinate in validCoordinates:
        if coordinate == userInput:
            validChar = True
            grid[coordinate] = symbol

    for key in grid:
        tie = True
        if grid[key] == "_":
            tie = False
            break
    
    if tie == True:
        print("tie")
        return

    if validChar == False:
        print("invalid coordinate")

    printGrid()

    # if (grid[11] == symbol and grid[12] == symbol and grid[13] == symbol) or (grid[21] == symbol and grid[22] == symbol and grid[23] == symbol) or (grid[31] == symbol and grid[32] == symbol and grid[33] == symbol) or (grid[11] == symbol and grid[21] == symbol and grid[31] == symbol) or (grid[12] == symbol and grid[22] == symbol and grid[32] == symbol) or (grid[13] == symbol and grid[23] == symbol and grid[33] == symbol) or (grid[11] == symbol and grid[22] == symbol and grid[33] == symbol) or (grid[13] == symbol and grid[22] == symbol and grid[31] == symbol):
    if winCondition():
        print(symbol + " wins")
        return

    activateRound()

printGrid()
activateRound()
