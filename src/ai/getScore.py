import numpy as np

def getScore(prefVector, movieVector):

    # getScore() calculates the eucledian distance between the group preference vector and a movie vector.
    # The smaller the distance, the greater the similarity.

    prefVector = np.array(prefVector)
    movieVector = np.array(movieVector)


    return np.linalg.norm(prefVector - movieVector)


if __name__ == "__main__":

    print("File is not meant for running..")