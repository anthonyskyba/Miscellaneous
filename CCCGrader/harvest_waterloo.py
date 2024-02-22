# exceeded time limit for subtask 4

rows = int(input())
columns = int(input())
grid = {}

for row in range(rows):
    counter = -1
    for char in input():
        counter += 1
        grid[str(counter + 1) + "x" + str(row + 1)] = char


a = int(input()) + 1
b = int(input()) + 1

visited = []
totalValue = 0

def search(x, y):
    global totalValue
    
    currentPos = (str(x) + "x" + str(y))
    visited.append(currentPos)
    pumpkin = grid[currentPos]

    if pumpkin == "S":
        totalValue += 1
    elif pumpkin == "M":
        totalValue += 5
    elif pumpkin == "L":
        totalValue += 10

    up = str(x) + "x" + str(y - 1)
    down = str(x) + "x" + str(y + 1)
    left = str(x - 1) + "x" + str(y)
    right = str(x + 1) + "x" + str(y)

    try:
        if grid[up] != "*" and not up in visited:
            search(x, y - 1)
    except:
        None

    try:
        if grid[down] != "*" and not down in visited:
            search(x, y + 1)
    except:
        None

    try:
        if grid[left] != "*" and not left in visited:
            search(x - 1, y)
    except:
        None

    try:
        if grid[right] != "*" and not right in visited:
            search(x + 1, y)
    except:
        None

search(b, a)

print(totalValue)