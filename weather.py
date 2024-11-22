from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Patna"):
    # requests_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    requests_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(requests_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")
    if not bool(city.strip()):
        city = "Bengaluru"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)

    























# import requests
# from dotenv import load_dotenv
# import os
# from pprint import pprint


# load_dotenv()

# def get_current_weather():
#     print('\n*** Get Current Weather Conditions ***\n')
    
#     city = input("\nPlease enter a city name:\n")
    
#     request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

#     weather_data = requests.get(request_url).json()

#     # print(request_url)

#     # pprint(weather_data)

#     print(f'\nCurrent weather for {weather_data["name"]}\n')
#     print(f'\nThe temp is {weather_data["main"]["temp"]}\n')
#     print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.\n')

# if __name__ == "__main__":
#     get_current_weather()    