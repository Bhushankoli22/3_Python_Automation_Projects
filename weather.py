from urllib import response
from requests import request
import requests


API_KEY = "287698fdc73675525adf61bf9436f95a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200 :
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    print(f"Weather of {city} is",weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print(f"Temperature of {city} is",temperature,"Celsius")
else:
    print("An error occured.")