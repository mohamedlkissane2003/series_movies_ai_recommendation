from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def create_model(df):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=8000)
    tfidf_matrix = vectorizer.fit_transform(df["text"])

    model = NearestNeighbors(metric="cosine", algorithm="brute")
    model.fit(tfidf_matrix)

    return model, tfidf_matrix

def recommend_movie(title, df, model, tfidf_matrix, top_n=8):
    title = title.lower().strip()

    matches = df[df["primaryTitle"].str.lower().str.contains(title)]

    if matches.empty:
        return ["Movie not found"]

    idx = matches.index[0]
    movie_cluster = df.iloc[idx]["cluster"]

    cluster_indices = df[df["cluster"] == movie_cluster].index

    distances, indices = model.kneighbors(tfidf_matrix[idx], n_neighbors=len(cluster_indices))

    recommendations = []
    for i in indices[0]:
        if i != idx and i in cluster_indices:
            recommendations.append(df.iloc[i]["primaryTitle"])
        if len(recommendations) == top_n:
            break

    return recommendations
