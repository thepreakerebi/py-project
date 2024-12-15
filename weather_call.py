import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_current_weather(city="Kigali"):
    print("Get current weather conditions")

    # city = input("Please enter a city name: ")
    request_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + f"&appid={API_KEY}&units=metric"

    weather_data = requests.get(request_url).json()
    # if weather_data.status_code == 200:
    #     # pprint(response.json())
    #     print(f"The temperature in {city} is {weather_data['main']['temp']} degrees Celsius")
    # else:
    #     return None

    return weather_data

if __name__ == "__main__":   
    print('\n*** Get current weather conditions ***\n')
    city = input("\nPlease enter a city name: ") 

    # check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = "Kigali"
        # print("City name cannot be empty or contain only spaces")
        # exit()

    weather_data = get_current_weather(city)
    print('\n')
    pprint(weather_data)