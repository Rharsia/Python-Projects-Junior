import random

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

while True:
    dice_roll(n_dices)    
    input()