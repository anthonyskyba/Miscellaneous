word = input()
rows = int(input())
columns = int(input())
grid = {}

for i in range(rows):
    row = input().split(" ")

    for j in range(len(row)):
        grid[str(j + 1) + "x" + str(i + 1)] = row[j]

print(grid)

for coordinate in grid:
    c1 = int(coordinate.split("x")[0])
    c2 = int(coordinate.split("x")[1])

    # if grid[coordinate] == word[0]:
    #     try:
    #         if grid[str(c1 + 1) + "x" + str(c2)] == 


# MENU
# 5
# 7
# F T R U B L K
# P M N A X C U
# A E R C N E O
# M N E U A R M
# M U N E M N S