from flask import Flask, render_template, request
from preprocessing import load_and_clean_data
from recommender import create_model, recommend_movie
from clustering import apply_clustering
from tmdb_api import get_movie_data

app = Flask(__name__)

df = load_and_clean_data(limit=5000)
model, tfidf_matrix = create_model(df)

clusters, _ = apply_clustering(tfidf_matrix)
df["cluster"] = clusters

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        movie_title = request.form["movie"]
        titles = recommend_movie(movie_title, df, model, tfidf_matrix)

        for title in titles:
            poster, link = get_movie_data(title)
            recommendations.append({
                "title": title,
                "poster": poster,
                "link": link
            })

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
