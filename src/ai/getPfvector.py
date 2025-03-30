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

    elif X.shape[0] <= 3:

        return np.average(X, axis=0)

    # Find the optimal number of clusters using silehoutte scores
    silehoutteScores = []

    print(X.shape[0])
    for k in range(2, X.shape[0]):


        model = KMeans(k, random_state=random_state, n_init="auto")

        lbls = model.fit_predict(X)

        score = silhouette_score(X, lbls)
        silehoutteScores.append((score, k))
    
    # Train KMeans on optimal clusters and return the averaged weighted clusters
    print("silethoutte scores: ", silehoutteScores)
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

if __name__ == "__main__":

    print("File is not meant for running..")


