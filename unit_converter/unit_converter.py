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

# create a unit list for everything
lengths = ["mm", "cm", "km", "m", "km", "in", "ft", "yd", "mi", "nm"]
temperatures = ["C", "F", "K"]
weights = ["g", "kg", "lb", "oz", "t"]

# find out what we are converting
def realm_to_convert(uin):
    unit = uin[0]
    unit_to = uin[1]
    if unit in lengths and unit_to in lengths:
        return "length"
    elif unit in temperatures and unit_to in temperatures:
        return "temperature"
    elif unit in weights and unit_to in weights:
        return "weight"
    else:
        print("Invalid units, try again.")
        converter()


def converter():
    uin = user_input()
    realm = realm_to_convert(uin)
    
    print(realm)

converter()