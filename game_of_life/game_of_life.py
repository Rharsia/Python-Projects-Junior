# Rules
# 1) Any live cell with fewer than two live neighbors dies, s if by underpopulation
# 2) Any live cell with two or three live neighbors lives on to the next generation
# 3) Any live cell with more than three live neighbors dies, as if by overpopulation
# 4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
import random
from colorama import Fore, Back, Style
# game initiation
def game_initiation():
    gen = 1
    print("This is a simulation of game of life")
    print()

    land_size = get_land_size()
    land = create_land(land_size)

    return (gen, land_size, land)

# get the desired land size
def get_land_size():
    land_size = int(input("Enter the desired land size (integer): "))
    return land_size

# generate the initial land
def create_land(land_size):
    land = []
    for i in range(land_size):
        land.append([])
        for j in range(land_size):
            land[i].append(random.randint(0,1))

    return land

# display the land
def land_display(land):
    for row in land:
        for col in row:
            if col == 1:
                print(Fore.GREEN + ' 1 ', end='')
            else:
                print(Fore.RED + ' 0 ', end='')
        print(Style.RESET_ALL)

# generate another generation
def check_land(land, land_size):
    updated_land = []

    for i in range(land_size):
        updated_land.append([])
        for j in range(land_size):
            live_neighbours = count_live_neighbours(land, i, j)

            if land[i][j] == 1:
                if live_neighbours < 2 or live_neighbours > 3:
                    updated_land[i].append(0)
                elif live_neighbours == 2 or live_neighbours == 3:
                    updated_land[i].append(1)

            elif land[i][j] == 0:
                if live_neighbours == 3:
                    updated_land[i].append(1)
                else:
                    updated_land[i].append(0)

    return updated_land

# find out the number of live cells around
def count_live_neighbours(land, i, j):
    """Count the number of live neighbours for the cell at (i, j)"""
    count = 0

    for x in range(max(0, i-1), min(len(land), i+2)):
        for y in range(max(0, j-1), min(len(land[0]), j+2)):
            if (x, y) != (i, j) and land[x][y] == 1:
                count += 1

    return count

# play the game 
variables = game_initiation()
gen = variables[0]
land_size = variables[1]
land = variables[2]

while True: 
    land_display(land)
    print(f"Generation {gen}")
    updated_land = check_land(land, land_size)
    land = updated_land
    gen += 1
    input()