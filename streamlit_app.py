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
