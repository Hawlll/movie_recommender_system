from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from pathlib import Path
import sys
import pandas as pd

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
    
    # Train KMeans on optimal clusters and return the averaged weighted clusters
    kOpt = max(silehoutteScores)[1]

    knn = KMeans(kOpt, random_state=random_state, n_init="auto")

    lbls = knn.fit_predict(X)

    lbls_series = pd.Series(lbls)

    clusters = knn.cluster_centers_

    cluster_counts = lbls_series.value_counts()

    #Apply weights (neighbors/sample_size) to each cluster
    for i in range(len(cluster_counts)):

        clusters[i] *= cluster_counts[i] / X.shape[0]

    pfVector = np.average(clusters, axis=0)

    return pfVector


movie_data = [
    [1, 0, 1, 0, 0, 0, 7.5],  # Action/Sci-Fi, Rating 7.5
    [0, 1, 0, 1, 0, 0, 6.2],  # Horror/Drama, Rating 6.2
    [1, 0, 1, 1, 0, 0, 8.2],  # Action/Sci-Fi/Drama, Rating 8.2
    [0, 1, 0, 0, 0, 1, 5.8],  # Horror/Family, Rating 5.8
    [0, 0, 1, 0, 1, 0, 7.9],  # Sci-Fi/History, Rating 7.9
    [1, 0, 0, 1, 0, 0, 8.5],  # Action/Drama, Rating 8.5
    [0, 1, 1, 0, 0, 0, 6.8],  # Horror/Sci-Fi, Rating 6.8
    [1, 1, 0, 0, 1, 0, 7.0],  # Action/Horror/History, Rating 7.0
    [0, 0, 0, 1, 0, 1, 9.1],  # Drama/Family, Rating 9.1
    [1, 0, 1, 1, 1, 0, 8.7]   # Action/Sci-Fi/Drama/History, Rating 8.7
]
print(getPfvector(movie_data))

if __name__ == "__main__":

    print("File is not meant for running..")


