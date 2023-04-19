# Rules
# 1) Any live cell with fewer than two live neighbors dies, s if by underpopulation
# 2) Any live cell with two or three live neighbors lives on to the next generation
# 3) Any live cell with more than three live neighbors dies, as if by overpopulation
# 4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction

land_size = 15

land = []

for i in range(land_size):
    land.append([])
    for j in range(land_size):
        land[i].append(1)

def land_display(land):
    for i in land:
        print(i)

land_display(land)