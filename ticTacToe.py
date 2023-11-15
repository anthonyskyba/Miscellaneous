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

printGrid()

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

    if (grid[11] == symbol and grid[12] == symbol and grid[13] == symbol) or (grid[21] == symbol and grid[22] == symbol and grid[23] == symbol) or (grid[31] == symbol and grid[32] == symbol and grid[33] == symbol) or (grid[11] == symbol and grid[21] == symbol and grid[31] == symbol) or (grid[12] == symbol and grid[22] == symbol and grid[32] == symbol) or (grid[13] == symbol and grid[23] == symbol and grid[33] == symbol) or (grid[11] == symbol and grid[22] == symbol and grid[33] == symbol) or (grid[13] == symbol and grid[22] == symbol and grid[31] == symbol):
        print(symbol + " wins")
        return

    printGrid()
    activateRound()

activateRound()
