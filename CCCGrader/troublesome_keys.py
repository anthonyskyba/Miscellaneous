pressed = input()
produced = input()

silentKey = "-"
sillyKey = ""

pressedCounter = -1
producedCounter = -1
while producedCounter < len(produced) - 1:
    pressedCounter += 1
    producedCounter += 1

    if producedCounter == len(produced) - 1 and silentKey == "-" and len(pressed) > len(produced):
        silentKey = pressed[len(pressed) - 1]

    while pressed[pressedCounter] == silentKey:
        pressedCounter += 1

    if pressed[pressedCounter] == produced[producedCounter]:
        continue
    else:
        try:
            if produced[producedCounter] == pressed[pressedCounter + 1]:
                silentKey = pressed[pressedCounter]
                pressedCounter += 1
            else:
                sillyKey = pressed[pressedCounter] + " " + produced[producedCounter]
        except:
            sillyKey = pressed[pressedCounter] + " " + produced[producedCounter]

print(sillyKey)
print(silentKey)