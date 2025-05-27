import pandas as pd
import numpy as np
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer   #

st.write("# Clients Reviews Analysis")     # Titulo do modelo de predição de satisfação;

user_input = st.text_input("Please, write a review about our service: ")    # Comentario do utilizador;

nltk.download("vader_lexicon")      # dados de entrada ja existentes em inglês no nltk para treinar o modelo;

s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write("## not good nor bad")
elif score["neg"] != 0:
    st.write("## Negative review")
elif score["pos"] != 0:
    st.write("## Positive review")

# Make it run in the terminal with "streamlit run sentiment_analysis.py" from
### the "venv" in "C:\Users\sophi\FrMarques\LyonData WCS new\Exame final\HELP NaturalLanguageProcessing"