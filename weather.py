import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_current_weather():
    print("Get current weather conditions")

    city = input("Please enter a city name: ")
    request_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + f"&appid={API_KEY}&units=metric"

    response = requests.get(request_url)
    weather_data = response.json()
    if response.status_code == 200:
        # pprint(response.json())
        print(f"The temperature in {city} is {weather_data['main']['temp']} degrees Celsius")
    else:
        return None

if __name__ == "__main__":    
    get_current_weather()