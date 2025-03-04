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

def get_movie_recommendation(genre_name):
    """
    Fetches a random movie from a specified genre using the TMDB API.
    """
    API_KEY = "fc270c3610a2f60a6aa52ac2ab0a6886"  # Replace with your actual TMDB API key
    BASE_URL = "https://api.themoviedb.org/3"
    
    # Fetch all available genres
    genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    genre_response = requests.get(genre_url)
    
    if genre_response.status_code == 200:
        genres = genre_response.json()["genres"]
        genre_dict = {genre["name"].lower(): genre["id"] for genre in genres}
        
        if genre_name.lower() in genre_dict:
            genre_id = genre_dict[genre_name.lower()]
            movie_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
            movie_response = requests.get(movie_url)
            
            if movie_response.status_code == 200:
                movies = movie_response.json()["results"]
                if movies:
                    movie = random.choice(movies)
                    print(f"Recommended Movie: {movie['title']}")
                    print(f"Overview: {movie['overview']}")
                else:
                    print("No movies found for this genre.")
            else:
                print("Error fetching movies. Check your API key.")
        else:
            print("Genre not found. Check the genre name.")
    else:
        print("Error fetching genres. Check your API key.")

if __name__ == "__main__":
    # Task 1: Get weather data for Tashkent
    city = "Tashkent"
    get_weather(city)
    
    # Task 2: Get movie recommendation for a genre
    genre = input("Enter a movie genre: ")
    get_movie_recommendation(genre)
