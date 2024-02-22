size = int(input())

while True:
    yobi = int(input())
    if size > yobi:
        size += yobi
    else:
        break

print(size)