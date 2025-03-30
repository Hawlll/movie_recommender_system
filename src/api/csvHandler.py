import csv

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