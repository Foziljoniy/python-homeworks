import requests
import random

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

    # Task 2: Get movie recommendation for a genre
    genre = input("Enter a movie genre: ")
    get_movie_recommendation(genre)

   
