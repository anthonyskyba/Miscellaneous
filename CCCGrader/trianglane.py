input()
grid = {}
counter = 0

while counter < 2:
    counter += 1
    row = input().split(" ")

    counter2 = 0
    for tile in row:
        counter2 += 1
        if tile == "0":
            grid[str(counter) + "x" + str(counter2)] = "dry"
        else:
            grid[str(counter) + "x" + str(counter2)] = "wet"

sides = 0

for coordinate in grid:
    if grid[coordinate] == "dry":
        continue

    potentialSides = 3
    firstDigit = int(coordinate.split("x")[0])
    secondDigit = int(coordinate.split("x")[1])

    if firstDigit == 1 and secondDigit % 2 == 1:
        try:
            if grid[str(firstDigit + 1) + "x" + str(secondDigit)] == "wet":
                potentialSides -= 1
        except:
            None
    elif firstDigit == 2 and secondDigit % 2 == 1:
        try:
            if grid[str(firstDigit - 1) + "x" + str(secondDigit)] == "wet":
                potentialSides -= 1
        except:
            None

    try:
        if grid[str(firstDigit) + "x" + str(secondDigit - 1)] == "wet":
            potentialSides -= 1
    except: 
        None

    try:
        if grid[str(firstDigit) + "x" + str(secondDigit + 1)] == "wet":
            potentialSides -= 1
    except:
        None

    sides += potentialSides

print(sides)
