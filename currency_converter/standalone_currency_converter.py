import requests

api_key = "a45d9bff39b144f6bfece005f11df14c"
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

response = requests.get(url)
data = response.json()
rates = data["rates"]


def convert_currency(amount, from_currency, to_currency):
    if from_currency != "USD":
        # convert from USD to currency
        amount = amount / rates[from_currency]

    return round(amount * rates[to_currency])

def get_data():
    
    while True:
        from_currency = input("Currency to be converted from: ")
        try: 
            from_currency = from_currency.upper()
            break
        except SyntaxError:
            print("Invalid input, try again.")

    while True:
        to_currency = input("Currency to by converted into: ")
        try:
            to_currency = to_currency.upper()
            break
        except SyntaxError:
            print("Invalid input, try again.")
    
    while True:
        amount = input("Amount to be converted: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print("Invalid input, try again.")

    return (amount, from_currency, to_currency)

def convert():
    data = get_data()
    amount = data[0]
    from_currency = data[1]
    to_currency = data[2]

    converted_amount = convert_currency(amount, from_currency, to_currency)

    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")


convert()