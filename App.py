import streamlit as st
from collections import Counter
import json as js
import pandas as pd
from nltk.tokenize import word_tokenize

from src.data import DATA_DIR
from src.parse_subtitles import Subtitle
from src.utils.io import read_json
from src.difficulty_prediction import predictor

def filter_difficult_words(words, user_level):
    words = map(str.lower, words)
    for word in words:
        word_diff = df[df['Word']==word]['I_Zscore'].squeeze()
        if isinstance(word_diff, float) and word_diff > user_level:
            yield word, word_diff
        else:
            continue

@st.cache
def load_df(fila_path):
    return pd.read_csv(fila_path)

df = load_df(f'{DATA_DIR}/word_difficulty.csv')
st.header(":zap: Learn english with movies")

user_level = st.slider('Enter your English level', min_value = 0, max_value = 10, value = 5)

#read subtitle
uploaded_file = st.file_uploader('Upload a subtitle file', type = ['srt'])
if uploaded_file:
    with open(f'{DATA_DIR}/subtitles/{uploaded_file.name}' ,"wb") as f: 
      f.write(uploaded_file.getbuffer())         
        #st.success("Saved File")
    sub_file_path = f'{DATA_DIR}/subtitles/{uploaded_file.name}'
    s = Subtitle(sub_file_path)


    st.subheader("Vocabulary")
    ind = read_json( 'src/demo/tracker.json').ind
    text = s.subs[ind].text
    st.write(text)


    with st.expander('Difficult Words:', expanded=True):
        words = word_tokenize(text)
        
        difficult_words = filter_difficult_words(words, user_level)
        for word, word_diff in difficult_words:
            st.write(f'- {word}')

    cols = st.columns(2)

    if cols[0].button('Previous'):
        ind -=1

    if cols[1].button('Next'):
        ind += 1

    with open('src/demo/tracker.json', 'w') as f:
        js.dump({'ind': ind}, f)


