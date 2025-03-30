from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from pathlib import Path
import sys

curDir = Path(__file__).resolve()
curDir = curDir.parent.parent
sys.path.insert(0, str(curDir))

from constants import VECTOR_LENGTH


def getPfvector(X, random_state=42):

    X = np.array(X)

    if X.shape[1] != VECTOR_LENGTH:

        print(f"Input X is not length {VECTOR_LENGTH}")

        return -1

    # Find the optimal number of clusters using silehoutte scores
    silehoutteScores = []

    for k in range(2, X.shape[0]):

        model = KMeans(k, random_state=random_state, n_init="auto")

        lbls = model.fit_predict(X)

        score = silhouette_score(X, lbls)
        silehoutteScores.append((score, k))
    
    # Train KMeans on optimal clusters and return the averaged clusters
    kOpt = max(silehoutteScores)[1]

    knn = KMeans(kOpt, random_state=random_state, n_init="auto")

    knn.fit(X)

    clusters = knn.cluster_centers_

    pfVector = np.average(clusters, axis=0)

    return pfVector

if __name__ == "__main__":

    print("File is not meant for running..")


