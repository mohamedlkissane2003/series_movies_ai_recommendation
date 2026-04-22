from sklearn.cluster import KMeans

def apply_clustering(tfidf_matrix, n_clusters=8):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(tfidf_matrix)
    return clusters, kmeans
