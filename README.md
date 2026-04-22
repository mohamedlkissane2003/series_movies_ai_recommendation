# Movies & Series AI Recommendation System

An intelligent movie and series recommendation engine powered by machine learning and natural language processing. This Flask-based web application provides personalized recommendations based on content similarity analysis.

## Features

- **Smart Recommendations**: Uses TF-IDF vectorization and machine learning to find similar movies/series
- **Intelligent Clustering**: Groups content into meaningful clusters for better similarity detection
- **Movie Details**: Fetches poster images and TMDB links for recommended movies
- **Web Interface**: Clean, user-friendly Flask web application
- **Data-Driven**: Processes and analyzes movie data for accurate recommendations

## Tech Stack

- **Backend**: Flask
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn, NLTK
- **API Integration**: TMDB (The Movie Database)
- **Frontend**: HTML, CSS

## Project Structure

```
series_movies_ai_recommendation/
├── app.py                 # Main Flask application
├── preprocessing.py       # Data loading and cleaning
├── recommender.py         # Recommendation model and logic
├── clustering.py          # K-means clustering implementation
├── tmdb_api.py           # TMDB API integration
├── requirements.txt      # Python dependencies
├── data/
│   └── movies.tsv        # Movie dataset
├── templates/
│   └── index.html        # Web interface template
└── static/
    └── style.css         # Styling
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd series_movies_ai_recommendation
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data** (required for text processing)
   ```bash
   python -m nltk.downloader punkt stopwords
   ```

## Usage

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:5000`
   - Enter a movie or series title
   - Get personalized recommendations with posters and TMDB links

## How It Works

1. **Data Preprocessing**: Movie data is loaded and cleaned from the TSV file
2. **Vectorization**: Uses TF-IDF to convert movie descriptions into numerical vectors
3. **Clustering**: K-means clustering groups similar movies together
4. **Recommendation**: When a user searches, the system finds movies with similar vectors
5. **Enrichment**: Movie posters and TMDB links are fetched via the TMDB API

## Dependencies

- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning algorithms
- `nltk` - Natural language processing
- `flask` - Web framework
- `requests` - HTTP library for API calls

## Configuration

The TMDB API key is configured in `tmdb_api.py`. Ensure you have a valid API key from [The Movie Database](https://www.themoviedb.org/settings/api).

## Future Enhancements

- User ratings and feedback integration
- Collaborative filtering for multi-user recommendations
- Genre and year-based filtering
- Advanced NLP for better understanding of movie descriptions
- Database integration for scalability

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
