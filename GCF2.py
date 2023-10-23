inputs = []
numbers = 2
counter = 1
output = 1

for i in range(int(input("How many numbers do you want?\n"))):
    inputs.append(int(input("Enter a number:\n")))

while counter < min(inputs):
    counter2 = 0
    counter += 1

    for i in inputs:
        if (i % counter == 0):
            counter2 += 1

        if (counter2 == len(inputs)):
            output = counter

print(output)
