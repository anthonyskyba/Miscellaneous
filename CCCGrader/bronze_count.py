participants = int(input())
first = 0
second = 0
third = 0
scores = []

for i in range(participants):
    score = int(input())
    scores.append(score)
    if score >= first:
        if score != first:
            third = second
            second = first
            first = score
    elif score >= second:
        if score != second:
            third = second
            second = score
    elif score >= third:
        if score != third:
            third = score

amountOfThirds = 0
for i in scores:
    if i == third:
        amountOfThirds += 1

print(str(third) + " " + str(amountOfThirds))