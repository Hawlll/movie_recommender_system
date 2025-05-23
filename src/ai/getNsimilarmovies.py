import sys
from pathlib import Path

curDir = Path(__file__).resolve()
curDir = curDir.parent.parent
sys.path.insert(0, str(curDir))

from ai import getDf, getScore, vectorize
from api import genreIdmap

def getNsimilarmovies(N, pfVector):

    # Returns n number of movies from ranking in most similar

    df = getDf.getDf()
    df.drop_duplicates(inplace=True, subset=["title"])

    df["dist_to_pfVector"] = df.apply(lambda row: getScore.getScore(pfVector, vectorize.vectorize(row.to_numpy())), axis=1)
    df["genre_ids"] = df["genre_ids"].apply(lambda row: [genreIdmap.genreIdmap(id) for id in row])

    return df.nsmallest(N, "dist_to_pfVector").to_numpy().tolist()

if __name__ == "__main__":

    print("File is not meant for running..")

    



