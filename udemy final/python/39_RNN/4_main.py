## Creating streamlit app

import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb

word_index=imdb.get_word_index()
model=load_model('model_imdb.h5')
reverse_words_index={value:key for key,value in word_index.items()}

model=load_model('model_imdb.h5')

def decode_review(encoded_review):
    return ' '.join([reverse_words_index.get(i-3,'?') for i in encoded_review])

def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review


def predict_sentiment(review):
    preprocessed_review=preprocess_text(review)
    prediction=model.predict(preprocessed_review)
    sentiment='positive' if prediction[0][0]>0.5 else 'negative'
    return sentiment,prediction[0][0]

import streamlit as st
st.title('Sentiment Analysis')
st.write('Enter a review:')
user_input=st.text_area('Movie review')
if st.button('Classify'):
    preprocessed_review=preprocess_text(user_input)
    prediction=model.predict(preprocessed_review)
    sentiment='positive' if prediction[0][0]>0.5 else 'negative'

else :
    st.write('Please enter a review')
