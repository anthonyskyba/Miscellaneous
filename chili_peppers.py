shu = 0

for _ in range(int(input())):
    pepper = input()

    if pepper == "Poblano":
        shu += 1500
    elif pepper == "Mirasol":
        shu += 6000
    elif pepper == "Serrano":
        shu += 15500
    elif pepper == "Cayenne":
        shu += 40000
    elif pepper == "Thai":
        shu += 75000
    elif pepper == "Habanero":
        shu += 125000

print(shu)