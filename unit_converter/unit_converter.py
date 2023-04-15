# This program will convert different units be it temperature, weight, distance

# start by user_input
def user_input():
    while True:
        unit_from = input("Enter units FROM which you wish to convert: ")
        try:
            unit_from = unit_from.lower()
            break
        except SyntaxError:
            print("Invalid input, try again.")

    while True:
        unit_to = input("Enter units INTO which you wish to convert: ")
        try:
            unit_to = unit_to.lower()
            break
        except SyntaxError:
            print("Invalid input, try again.")

    while True:
        amount = input("Input the amount: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print("Invalid input, try again.")

    return (unit_from, unit_to, amount)

x = user_input()

print(x[0])