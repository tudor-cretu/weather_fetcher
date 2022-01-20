import requests

API_KEY = "4ab7b0b06c3a58c91585f05039d82b5f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    name = data["name"]
    country = data["sys"]["country"]
    print(name, "-", country)
    weather = data["weather"][0]["description"]
    print("Weather:", weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
