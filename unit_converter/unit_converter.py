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
lengths = ["mm", "cm", "km", "m", "km", "in", "ft", "yd", "mi", "nmi"]
temperatures = ["C", "F", "K"]
weights = ["g", "kg", "lb", "oz", "t"]

# find out what we are converting
def realm_to_convert(uin):
    unit = uin[0]
    unit_to = uin[1]
    if unit in lengths and unit_to in lengths:
        return "length"
    elif unit.upper() in temperatures and unit_to in temperatures:
        return "temperature"
    elif unit in weights and unit_to in weights:
        return "weight"
    else:
        print("Invalid units, try again.")
        return "invalid"


# length
def length_converter(uin):
    conversion_factors = {"m": 1, "mm": 0.001, "cm": 0.01, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34, "nmi": 1852}
    from_unit = uin[0]
    to_unit = uin[1]
    amount = uin[2]

    # convert to meters
    meters = amount * conversion_factors[from_unit]

    # convert from meters to to_unit
    result = meters / conversion_factors[to_unit]

    answer = f"{amount} {from_unit} is equal to {result} {to_unit}."
    return answer

# uin = ("mi", "km", 1)
# length_converter(uin)

# weight
def weight_converter(uin):
    conversion_factors = {"g": 1, "mg": 0.001, "kg": 1000, "t": 1000000}


def converter():
    uin = user_input()
    realm = realm_to_convert(uin)

    if realm == "length":
        result = length_converter()
    


converter()