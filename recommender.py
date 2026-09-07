import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("songs.csv")

df["features"] = (
    df["artist"] + " "
    + df["genre"] + " "
    + df["mood"] + " "
    + df["language"]
)

vectorizer = TfidfVectorizer()
text_matrix = vectorizer.fit_transform(df["features"])

numerical_features = df[["energy", "danceability"]]

scaler = StandardScaler()
numerical_matrix = scaler.fit_transform(numerical_features)

numerical_similarity = cosine_similarity(numerical_matrix)
text_similarity = cosine_similarity(text_matrix)

similarity_matrix = (
    0.7 * text_similarity
    + 0.3 * numerical_similarity
)


def recommend_songs(song_title, number_of_recommendations=5):

    matches = df[
        df["title"].str.lower() == song_title.lower()
    ]

    if matches.empty:
        return pd.DataFrame()

    song_index = matches.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[song_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[
        1:number_of_recommendations + 1
    ]

    recommended_indexes = [
        index for index, score in similarity_scores
    ]

    recommendations = df.iloc[
        recommended_indexes
    ][
        [
            "title",
            "artist",
            "genre",
            "mood",
            "language",
            "energy",
            "danceability"
        ]
    ]

    return recommendations