import requests

API_KEY = "5501394962c50d0cc235ab3c3ab631e1"
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_data(title):
    search_url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title
    }

    response = requests.get(search_url, params=params)
    data = response.json()

    if data.get("results"):
        movie = data["results"][0]
        poster_path = movie.get("poster_path")
        movie_id = movie.get("id")

        poster_url = None
        tmdb_url = None

        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

        if movie_id:
            tmdb_url = f"https://www.themoviedb.org/movie/{movie_id}"

        return poster_url, tmdb_url

    return None, None
