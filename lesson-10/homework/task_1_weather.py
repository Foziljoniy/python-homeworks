import requests
import random

def get_weather(city):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.
    """
    API_KEY = "e36e29436a1696b3654ec66e2eabbeba"  # Replace with your actual OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Fetch temperature in Celsius
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Error fetching weather data. Check your API key or city name.")



if __name__ == "__main__":
    # Task 1: Get weather data for Tashkent
    city = "Tashkent"
    get_weather(city)
    
   
