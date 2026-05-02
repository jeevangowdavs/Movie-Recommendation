import streamlit as st
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df = pickle.load(open(os.path.join(BASE_DIR, "movies.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(BASE_DIR, "similarity.pkl"), "rb"))

# Load data
df = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie = movie.lower()

    if movie.strip() == "":
        return ["⚠ Please enter a movie name"]

    if movie not in df['title'].str.lower().values:
        return ["❌ Movie not found"]

    index = df[df['title'].str.lower() == movie].index[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    results = []
    for i in distances[1:11]:
        results.append(df.iloc[i[0]].title)

    return results

# UI
st.title("🎬 Smart Movie Recommender")

movie = st.text_input("Enter movie name:")

if st.button("Recommend"):
    results = recommend(movie)

    st.subheader("Recommendations:")
    for r in results:
        st.write("👉", r)