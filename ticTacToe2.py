validCoordinates = [11, 12, 13, 21, 22, 23, 31, 32, 33]
grid = {}
counter2 = 0
symbol = "X"

for coordinate in validCoordinates:
    grid[coordinate] = "_"

def printGrid():
    string = ""
    counter = 0 

    for coordinate in grid:
        string += grid[coordinate]
        string += " "
        counter += 1
        if counter == 3:
            string += "\n"
            counter = 0

    print(string)

def winCondition():
    rowsCounter = 0
    rowsLength = 3

    columnCounter = 0
    columnLength = 3

    for count in range(1, int((len(grid) / rowsLength)) + 1):
        rowsMatch = None
        for position in range(1, rowsLength + 1):
            element = grid[int(str(count) + str(position))]
            if element == "_":
                break
            if rowsCounter == 0:
                rowMatch = element
                rowsCounter += 1
            elif rowMatch == element:
                rowsCounter += 1

    for count in range(1, int((len(grid) / columnLength)) + 1):
        columnMatch = None
        for position in range(1, columnLength + 1):
            element = grid[int(str(position) + str(count))]
            if element == "_":
                break
            if columnCounter == 0:
                columnMatch = element
                columnCounter += 1
            elif columnMatch == element:
                columnCounter += 1

    return rowsCounter == rowsLength or columnCounter == columnLength

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
