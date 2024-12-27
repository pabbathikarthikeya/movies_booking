import json
MOVIE_FILE="movies.json"
def load_movies():
    try:
        with open(MOVIE_FILE,'r') as file:
            movies=json.load(file)
        return movies
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        print("Error loading movies. Please check the file format.")
        return []
def display_movies(movies):
    print("Movies currently showing:")
    for i,movie in enumerate(movies,1):
        print(f"{i}. {movie['title']}")
        for timing in movie['show_timings']:
            print(f"    - {timing}")