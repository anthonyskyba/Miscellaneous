inputs = []
daysCounter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for i in range(int(input())):
    inputs.append(input())

for row in inputs:
    i = 0

    for char in row:
        i += 1

        if (char == "Y"):
            daysCounter[i] += 1

largest = 0
output = ""

for key in daysCounter:
   value = daysCounter[key]
   if (value > largest): largest = value

for key in daysCounter:
    if (daysCounter[key] == largest):
        if (len(output) == 0): output = str(key)
        else: output += ", " + str(key)

print(output)
