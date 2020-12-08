import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    with open(DATA_FILE, "r", encoding="utf8") as f:
        movie_titles =  json.load(f)
    
    movies = [Movie(movie_title) for movie_title in movie_titles]
    return movies

class Movie():
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title


    def _get_movies(self):
        with open(DATA_FILE, "r", encoding="utf8") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w", encoding="utf8") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()

        # Vérifier que le film n'est pas déjà dans la liste
        if self.title not in movies:
            # Si ce n'est pas le cas, on l'ajoute
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            """
            Si c'est le cas, on affiche un message pour indiquer
            que le film est déjà dans la liste (avec le module
            logging).
            """
            logging.warning(f"Le film {self.title} est déjà présent")
            return False

        
    def remove_from_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()

        # Vérifier que le film existe dans la liste
        if self.title in movies:
            # Si c'est le cas, on l'enlève
            movies.remove(self.title)
            self._write_movies(movies)


if __name__ == "__main__":
    movies = get_movies()

    # print(movies)

    for movie in movies:
        print(movie)