import requests

API_KEY = '6e1459c841a45c152650b135d1ccc147'
API_URL = "https://api.themoviedb.org/3/discover/movie"

GENRES = {
    'horror': 27,
    'comedy': 35,
    'action': 28,
    'drama': 18,
    'romance': 10749,
    'thriller': 53
}

def get_movies_by_genre(genre):
    genre_id = GENRES.get(genre)
    if genre_id:
        params = {
            "api_key": API_KEY,
            "with_genres": genre_id,
            "language": "en-US",
            "sort_by": "popularity.desc",
        }
        try:
            response = requests.get(API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            movies = data.get("results", [])
            return [movie['title'] for movie in movies]
        except requests.RequestException as e:
            print(f"Error during API request: {e}")
            return []
    return []
