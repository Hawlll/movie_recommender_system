from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from src.constants import VECTOR_LENGTH


def getPfvector(X, random_state=42, max_clusters=10):

    X = np.array(X)

    if X.shape[1] != VECTOR_LENGTH:

        print(f"Input X is not length {VECTOR_LENGTH}")

        return -1

    # Find the optimal number of clusters using silehoutte scores
    silehoutteScores = []

    for k in range(k, max_clusters+1):

        model = KMeans(k, random_state=random_state)

        model.fit(X)

        score = silhouette_score(X, model.labels_)
        silehoutteScores.append((score, k))
    
    # Train KMeans on optimal clusters and return the averaged clusters
    kOpt = max(silehoutteScores)[1]

    knn = KMeans(kOpt, random_state=random_state)

    knn.fit(X)

    clusters = knn.cluster_centers_

    pfVector = np.average(clusters, axis=1)

    return pfVector



