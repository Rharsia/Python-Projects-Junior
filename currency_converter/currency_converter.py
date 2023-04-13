import requests

api_key = "a45d9bff39b144f6bfece005f11df14c"
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

response = requests.get(url)
data = response.json()
rates = data["rates"]

