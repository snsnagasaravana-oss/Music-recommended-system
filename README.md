TuneMatch - Music Recommendation System

TuneMatch is a simple content-based music recommendation system built using Python, Pandas, Scikit-learn, and Streamlit.


 Features

- Select a song from the dataset
- Get 5 similar song recommendations
- Uses TF-IDF and Cosine Similarity
- Considers energy and danceability
- Simple Streamlit web interface

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

Recommendation Algorithm

The system uses:

1. TF-IDF for text-based song features
2. Cosine Similarity for comparing songs
3. Energy and Danceability for numerical similarity
4. Combined similarity score for recommendations

 How to Run

```bash
pip install pandas numpy scikit-learn streamlit
streamlit run app.py
