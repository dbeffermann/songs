import streamlit as st
import pickle
import re
import os

with open('naive_bayes_1.0.0.pkl', 'rb') as fid:
    modelo = pickle.load(fid)
    
with open('naive_bayes_plus_pop_1.0.0.pkl', 'rb') as fid:
    modelo_plus_pop = pickle.load(fid)

lyric = st.text_area('Escribe')

modelo = option = st.sidebar.selectbox('Selecciona un modelo:',tuple([i for i in os.listdir(os.getcwd()) if i.endswith('.pkl')]))
if lyric:
    prediccion = ''.join(modelo.predict([lyric])).capitalize() if modelo == 'Naive Bayes' else ''.join(modelo_plus_pop.predict([lyric])).capitalize()
    st.write('Sentiment:', prediccion)

    st.image(f"{prediccion}.jpeg", caption=f'{prediccion}')


