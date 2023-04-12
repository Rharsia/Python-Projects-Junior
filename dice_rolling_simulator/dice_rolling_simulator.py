import random
import msvcrt

# single dice roll
# result = random.randint(1,6)
# result

# any number of dices
n_dices = int(input("Number of dices to roll: "))

def dice_roll(n_dices):
    results = []
    if n_dices > 0:
        for i in range(n_dices):
            results.append(random.randint(1,6))
        return results
    else:
        return ("No dices were rolled.")

# while True:
#     print(dice_roll(n_dices))
#     input()
#     if msvcrt.kbhit() and msvcrt.getch() == b"\x1b":
#         break

while True:
    print(dice_roll(n_dices))
    while True:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == 27:  # Escape key
                exit()
            break