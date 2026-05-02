import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")

# Rename columns (clean naming)
df = df.rename(columns={
    "Title": "title",
    "Genre": "genre",
    "Description": "description",
    "Director": "director",
    "Actors": "actors"
})

# Keep required columns
df = df[['title', 'genre', 'description', 'director', 'actors']]

# Handle missing values
df.fillna('', inplace=True)

# Combine features
df['content'] = (
    df['genre'] + " " +
    df['description'] + " " +
    df['director'] + " " +
    df['actors']
)

# Convert text → vectors
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(df['content']).toarray()

# Compute similarity
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(df, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("✅ Model created successfully with your dataset!")