# Write your solution here
def find_movies(database: list, search_term: str):


    movies_in = []

    for movie in database:
        if search_term.casefold() in movie["name"].casefold():
            movies_in.append(movie)


    return movies_in
            


if __name__ == "__main__":
    database = [{'name': 'The Birds', 'director': 'Alfred Hitchcock', 'year': 1963, 'runtime': 119}, {'name': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972, 'runtime': 175}, {'name': 'Jaws', 'director': 'Steven Spielberg', 'year': 1975, 'runtime': 124}, {'name': 'Star Wars', 'director': 'George Lucas', 'year': 1977, 'runtime': 121}]

    my_movies = find_movies(database, "ja")
    print(my_movies)