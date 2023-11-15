num1 = 20
num2 = 35

counter = 1
greatestCommonFactor = 1

while counter < min(num1, num2):
    counter += 1
    if num1 % counter == 0 and num2 % counter == 0:
        greatestCommonFactor = counter

print(greatestCommonFactor)
