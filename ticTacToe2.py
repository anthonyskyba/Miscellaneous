print("minimum size is 1x1\nmaximum size is until it breaks")
height = int(input("enter height of board:\n"))
width = int(input("enter width of board:\n"))
winLength = int(input("enter amount of symbols in a row needed to win:\n"))

validCoordinates = [11]
grid = {}
counter2 = 0
symbol = "X"

# add all possible coordinates to validCoordinates
while len(validCoordinates) != height * width:
    coordinate = list(str(validCoordinates[0]))
    firstDigit = int(coordinate[0])
    secondDigit = int(coordinate[1])

    if secondDigit == width:
        # start a new row
        validCoordinates = [int(str(firstDigit + 1) + "1")] + validCoordinates
    else:
        # increment current row
        validCoordinates = [int(str(firstDigit) + str(secondDigit + 1))] + validCoordinates

# sort the coordinates and assign them all to "_"
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

# horizontal = "rows" or "columns"
# diagonal = "TLtoBR" or "TRtoBL"
# coordinate = user's input
def winCondition(coordinate, horizontal, diagonal):
    global symbol
    matches = 0
    counter = 0
    counter2 = 0
    num1 = int(list(str(coordinate))[0])
    num2 = int(list(str(coordinate))[1])

    # loop through how many matches we need
    while counter <= winLength - 1:
        # increment the coordinate 
        if horizontal == "rows":
            counter += 1
        elif horizontal == "columns":    
            counter2 += 1
        elif diagonal == "TLtoBR":
            counter -= 1
            counter2 -= 1
        elif diagonal == "TRtoBL":
            counter += 1
            counter2 -= 1

        try:
            key = int(str(num1 + counter2) + str(num2 + counter))
        except:
            key = None
        
        # check if not on edge and if square to the right matches
        if key in grid and grid[key] == symbol:
            matches += 1
        else:
            try:
                key = int(str(num1 - counter2) + str(num2 - counter))
            except:
                key = 0

            # check if not on edge and if square to the left matches
            if key in grid and grid[key] == symbol:
                matches += 1
            else:
                break
    
    # return true if all matches succeeded
    if matches == winLength - 1:
        return True
    return False

repeatSymbol = False
def activateRound():
    global symbol
    global repeatSymbol

    # repeat the symbol if invalid coordinate
    if (!repeatSymbol):
        repeatSymbol = False
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"

    validChar = False
    tie = False
    userInput = int(input("Enter a coordinate:\n"))

    # check for invalid coordinate entered
    for coordinate in validCoordinates:
        if coordinate == userInput:
            validChar = True
            # check if square is available
            if grid[coordinate] == "_":
                grid[coordinate] = symbol
            else:
                repeatSymbol = True
                print("coordinate is occupied")

    # check if there are any empty squares remaining
    for key in grid:
        tie = True
        if grid[key] == "_":
            tie = False
            break

    if tie:
        print("tie")
        return

    if !validChar:
        print("invalid coordinate")
        repeatSymbol = True

    printGrid()

    if winCondition(userInput, "rows", None) or winCondition(userInput, "columns", None) or winCondition(userInput, None, "TLtoBR") or winCondition(userInput, None, "TRtoBL"):
        print(symbol + " wins")
        return

    activateRound()

printGrid()
activateRound()
