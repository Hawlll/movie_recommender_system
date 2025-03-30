
import json
import urllib.request
import os
from csvHandler import csvReader, csvWriter
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def newData(API_KEY, numPages):

    for num in range(numPages):
        movieURL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={num + 1}"
        requestURL = urllib.request.urlopen(movieURL)

        data = requestURL.read()
        encode = requestURL.info().get_content_charset("UTF-8")
        jsonResponse = json.loads(data.decode(encode))

        for result in range(20):
            movieTitle = jsonResponse['results'][result]['title']
            genreIds = list(jsonResponse['results'][result]['genre_ids'])
            movieRating = jsonResponse['results'][result]['vote_average']
            movieDesc = jsonResponse['results'][result]['overview']

            csvWriter(movieTitle, genreIds, movieRating, movieDesc)

def main():
    userChoice = input("""What do you want to do (Pick A Number):\n
1) Create new dataset \n
2) Open existing dataset \n
--> """)
    
    if userChoice == "1":
        numPages = int(input("Enter the number of pages for the dataset \n--> "))

        newData(API_KEY, numPages)

    elif userChoice == "2":
        movieData = csvReader()
        print(movieData)
        