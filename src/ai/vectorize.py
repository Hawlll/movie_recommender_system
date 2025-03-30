from api.get_data import genreDefiner
from constants import INDEX_0, INDEX_1, INDEX_2, INDEX_3, INDEX_4, INDEX_5, VECTOR_LENGTH

def vectorize(movieData):

    """
    Vectorizes movieData into the following format

    Ex: [1,0,1,1,1,0,8.9]

    Indexes 0-5 are movie genres. Index 6 is a movie rating

    Index 0: Is the movie an Action or Adventure
    Index 1: Is the movie a Horror or Thriller
    Index 2: Is the movie Science Fiction or Fantasies
    Index 3: Is the movie Drama or Romance
    Index 4: Is the movie History, war, or western
    Index 5: Is the movie Family
    Index 6: least preferred movie rating
    """

    vector = [0*VECTOR_LENGTH]

    genres = movieData["genre_ids"]

    genres = set(genreDefiner(genres))

    for i, elem in enumerate([INDEX_0, INDEX_1, INDEX_2, INDEX_3, INDEX_4, INDEX_5]):

        if genres.issubset(elem):

            vector[i] = 1
    
    vector[-1] = movieData["movie_rating"]

    return vector








if __name__ == "__main__":

    print("File is not meant for running..")