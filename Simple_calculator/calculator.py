# create an operation function
def get_operation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter operation (1/2/3/4): ")

    return operation

# get numbers function
def get_numbers():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    numbers = (num1, num2)
    return numbers

# create the calculator function
def calculator():

    print("Welcome to my simple calculator")
    operation = get_operation()
    numbers = get_numbers()

    if operation == "1":
        result = f"{numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}"
    elif operation == "2":
        result = f"{numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}"
    elif operation == "3":
        result = f"{numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}"
    elif operation == "4":
        result = f"{numbers[0]} / {numbers[1]} = {numbers[0] / numbers[1]}"
    else:
        result = "Invalid input"

    return result

# put it in a loop
while True:

    calculator()

    end = input("Continue? (y/n): ")

    if end == "y":
        continue
    elif end == "n":
        break
    else:
        print("Invalid input")
        continue