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

amount = 447655
from_currency = "CZK"
to_currency = "USD"

converted_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")