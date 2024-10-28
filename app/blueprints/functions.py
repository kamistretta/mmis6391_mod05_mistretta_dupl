# functions.py

def filter_movies(movies, title=None, director=None, release_year=None):
    """Filter movies based on title, director, and release year."""
    filtered_movies = movies

    if title:
        filtered_movies = [movie for movie in filtered_movies if title.lower() in movie['title'].lower()]

    if director:
        filtered_movies = [movie for movie in filtered_movies if director.lower() in movie['director'].lower()]

    if release_year:
        filtered_movies = [movie for movie in filtered_movies if movie['release_year'] == release_year]

    return filtered_movies

