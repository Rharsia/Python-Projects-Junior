# 1) sign up for a free API key
# 2) install requests library into Python
# 3) make the app

import requests

# API key and base URL for OpenWeatherMape
api_key = "f863f2b4679723f139f41d5e8b55948f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# prompt the user for the city name
city = input("Enter city name: ")

# Create the URL for the API request
url = f"{base_url}q={city}&appid={api_key}"

print(url)

# send the API request and get the response
response = requests.get(url)

# parse the JSON data from the response
data = response.json()

# check if the API returne an error
if data["cod"] != "404":
    # Extract the weather information from the JSON data
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    # Display the weather information to the user
    print(f"Current weather in {city}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")

else:
    print("City not found.")