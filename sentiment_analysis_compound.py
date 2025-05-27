import pandas as pd
import numpy as np
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

st.write("# Análise de Satisfação do Cliente")

user_input = st.text_input("Please, write a review about our service:")

nltk.download("vader_lexicon")  # só é necessário na primeira vez

#if user_input:  # garantir que o campo não está vazio
#    s = SentimentIntensityAnalyzer()
#    score = s.polarity_scores(user_input)

#    if score["compound"] == 0:
#        st.write("Not good nor bad")
#    elif score["neg"] > score["pos"]:
#        st.write("## Negative review")
#    else:
#        st.write("## Positive review")

import matplotlib.pyplot as plt
       
if user_input:
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(user_input)

    st.write(f"**Compound score:** {score['compound']:.4f}")

    labels = ["Negative", "Neutral", "Positive"]
    values = [score["neg"], score["neu"], score["pos"]]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.write("### Sentiment distribution")
    st.pyplot(fig)

    if score["compound"] >= 0.05:
        st.write("## Positive review")
    elif score["compound"] <= -0.05:
        st.write("## Negative review")
    else:
        st.write("## Neutral review")
