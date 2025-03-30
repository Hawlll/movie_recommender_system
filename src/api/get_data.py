import csv
import json
import urllib.request
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def genreDefiner(genreIds):
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

    for id in (genreIds):
        if id in genreDict.keys():
            genreList.append(genreDict[id])

    return genreList

def csvWriter(movieTitle, genreIds, movieRating, movieDesc):
    infoList = [movieTitle, genreIds, movieRating, movieDesc]

    with open("movieData.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(infoList)


def csvReader():
    data = []

    with open("movieData.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            convertedList = []
            toConvert = row[1]
            toConvert = toConvert.replace("[", "")
            toConvert = toConvert.replace("]", "")
            toConvert = toConvert.split(",")

            for num in toConvert:

                if len(num) > 0:
                    convertedList.append(int(num))
                    
            row[1] = convertedList
            
            data.append(row)

        return data


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
        

main()