# This program will convert different units be it temperature, weight, distance

# start by user_input
def user_input():
    while True:
        unit_from = input("Enter units FROM which you wish to convert: ")
        try:
            unit_from = unit_from.lower()
            if unit_from == "c" or unit_from == "k" or unit_from == "f":
                unit_from = unit_from.upper()
            break
        except SyntaxError:
            print("Invalid input, try again.")

    while True:
        unit_to = input("Enter units INTO which you wish to convert: ")
        try:
            unit_to = unit_to.lower()
            if unit_to == "c" or unit_to == "k" or unit_to == "f":
                unit_to = unit_to.upper()
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
    elif unit in temperatures and unit_to in temperatures:
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
    result = round(result, 2)

    answer = f"{amount} {from_unit} is equal to {result} {to_unit}."
    return answer

# uin = ("mi", "km", 1)
# length_converter(uin)

# weight
def weight_converter(uin):
    conversion_factors = {"g": 1, "mg": 0.001, "kg": 1000, "t": 1000000, "lb": 453.59, "oz": 28.35}
    from_unit = uin[0]
    to_unit = uin[1]
    amount = uin[2]

    # convert to grams
    grams = amount * conversion_factors[from_unit]

    # convert from grams to to_unit
    result = grams / conversion_factors[to_unit]
    result = round(result, 2)

    answer = f"{amount} {from_unit} is equal to {result} {to_unit}."
    return answer

# uin = ("lb", "kg", 1)
# weight_converter(uin)

# temperature
def temperature_convert(uin):
    from_unit = uin[0]
    to_unit = uin[1]
    amount = uin[2]

    # convert all to Celsius
    if from_unit == "C":
        celsius = amount
    elif from_unit == "K":
        celsius = amount - 273.15
    elif from_unit == "F":
        celsius = (amount - 32) * (5/9)

    # convert celsius to to_unit
    if to_unit == "C":
        result = celsius
    elif to_unit == "K":
        result = celsius + 273.15
    elif to_unit == "F":
        result = (celsius * 5/9) + 32

    result = round(result, 2)

    answer = f"{amount} {from_unit} is equal to {result} {to_unit}."
    return answer

uin = ("C", "K", 199)
temperature_convert(uin)

def converter():
    while True:
        uin = user_input()

        realm = realm_to_convert(uin)

        if realm == "invalid":
            continue
        elif realm == "length":
            result = length_converter(uin)
        elif realm == "weight":
            result = weight_converter(uin)
        elif realm == "temperature":
            result = temperature_convert(uin)

        return result

converter()