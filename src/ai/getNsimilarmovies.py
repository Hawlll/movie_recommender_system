import sys
from pathlib import Path

curDir = Path(__file__).resolve()
curDir = curDir.parent.parent
sys.path.insert(0, str(curDir))

from ai import getDf, getScore, vectorize

def getNsimilarmovies(N, pfVector):

    # Returns n number of movies from ranking in most similar 

    df = getDf.getDf()
    df.drop_duplicates(inplace=True, subset=["title"])

    df["dist_to_pfVector"] = df.apply(lambda row: getScore.getScore(pfVector, vectorize.vectorize(row.to_numpy())), axis=1)

    return df.nsmallest(N, "dist_to_pfVector")

if __name__ == "__main__":

    print("File is not meant for running..")

    



