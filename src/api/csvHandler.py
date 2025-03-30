import csv

# writes the data sent as a parameter to a file
def csvWriter(movieTitle, genreIds, movieRating, movieDesc, posterUrl):
    infoList = [movieTitle, genreIds, movieRating, movieDesc, posterUrl]

    with open("movieData.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(infoList)

# reads the data in the csv file back into a list
def csvReader():
    data = []

    with open("movieData.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            # next few lines converts the string in position 1 to a list
            # that contains each movie's genre id numbers
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