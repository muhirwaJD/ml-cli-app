import streamlit as st

st.title('Muhirwa')

st.info('This is my first ML app')

# Data frame from a github repo
with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
