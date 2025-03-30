import json
import urllib.request
import os
from csvHandler import csvReader, csvWriter
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

# get data from the API call using json
def newData(API_KEY, numPages):

    # looks up multiple "pages" of movie data from the api
    for num in range(numPages):
        # constructs the api call based on page number and makes an http
        # request to the api call and retreives the response
        movieURL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={num + 1}"
        requestURL = urllib.request.urlopen(movieURL)

        # reads the raw data from the api and decodes the response data
        #into a Python dictionary
        data = requestURL.read()
        encode = requestURL.info().get_content_charset("UTF-8")
        jsonResponse = json.loads(data.decode(encode))

        # extracts movie data from the first 20 movies in the response
        for result in range(20):
            movieTitle = jsonResponse['results'][result]['title']
            genreIds = list(jsonResponse['results'][result]['genre_ids'])
            movieRating = jsonResponse['results'][result]['vote_average']
            movieDesc = jsonResponse['results'][result]['overview']
            posterPath = jsonResponse['results'][result]['poster_path']
            posrterUrl = f"https://image.tmdb.org/t/p/w500/{posterPath}"

            # writes the data to a file for use in the AI functionality
            csvWriter(movieTitle, genreIds, movieRating, movieDesc ,posrterUrl)

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
        print(movieData[0])
        

main()