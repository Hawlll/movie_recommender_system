import json
import urllib.request
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def genreDefiner(idList):
    genreList = []

    genreDict = {28 : "Action",
                 12 : "Adventure",
                 16 : "Animation",
                 35 : "Comedy",
                 80 : "Crime",
                 99 : "Documentary",
                 18 : "Drama",
                 10751 : "Family",
                 14 : "Fantasy",
                 36 : "History",
                 27 : "Horror",
                 10402 : "Music",
                 9648 : "Mystery",
                 10749 : "Romance",
                 878 : "Science Fiction",
                 10770 : "TV Movie",
                 53 : "Thriller",
                 10752 : "War",
                 37 : "Western"}

    for id in (idList):
        if id in genreDict.keys():
            genreList.append(genreDict[id])

    return genreList

def newData(API_KEY, numPages):

    for num in range(numPages):
        movieURL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={num + 1}"
        requestURL = urllib.request.urlopen(movieURL)

        data = requestURL.read()
        encode = requestURL.info().get_content_charset("UTF-8")
        jsonResponse = json.loads(data.decode(encode))

        movieTitle = 1
        movieDesc = 1
        movieGenres = 1
        movieRating = 1

def main():
    numPages = int(input("Enter the number of pages for the dataset \n--> "))

    newData(API_KEY, numPages)

main()