import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('Muhirwa')

st.info('This is my first ML app')

# Data frame from a github repo
with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw

# Data visualization
with st.expander('Data Visualization'):
  st.write('**Scatter plot**')
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', x_label='bill_length', y_label='body_mass', color='species', width="stretch", height="content")

  st.write('**Bar Graph**')
  st.bar_chart(data=df, x='bill_length_mm', y='body_mass_g', x_label='bill_length', y_label='body_mass', color='species', horizontal=False, sort=True, width="stretch", height="content")

# More data preparation allowing a user to add different features
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))
