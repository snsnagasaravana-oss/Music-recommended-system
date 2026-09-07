import streamlit as st
from recommender import df, recommend_songs

st.set_page_config(
    page_title="TuneMatch",
    page_icon="🎵",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background-color: #f7f7f7;
    }

    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🎵 TuneMatch</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Simple Music Recommendation System</div>',
    unsafe_allow_html=True
)

st.subheader("🎧 Select a Song")

selected_song = st.selectbox(
    "Choose your favorite song",
    df["title"].tolist()
)

if st.button("✨ Get Recommendations", use_container_width=True):

    recommendations = recommend_songs(
        selected_song,
        number_of_recommendations=5
    )

    st.success(f"Selected Song: {selected_song}")

    st.subheader("🎵 Recommended Songs")

    for i, (_, song) in enumerate(
        recommendations.iterrows(),
        start=1
    ):
        with st.container(border=True):
            st.markdown(f"### {i}. 🎵 {song['title']}")
            st.write(f"**Artist:** {song['artist']}")
            st.caption(
                f"Genre: {song['genre']}  |  "
                f"Mood: {song['mood']}  |  "
                f"Language: {song['language']}"
            )

st.divider()

st.caption(
    "TuneMatch | Python + Pandas + Scikit-learn + Streamlit"
)