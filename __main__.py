import streamlit as st
import pandas as pd
import numpy as np
import os
from Phraends_Flask.static.read_text_file import read_text_file

st.title("Phraends")

st.write("""
NLP Application for Summarizing Finance Article
 """)

ticker = st.text_input('Please enter a stock ticker that you would like to learn more about:')

## Retrieve file path for text output file that contains phrases to be output
phraends_folder = os.path.join(os.getcwd(), 'Phraends_Flask')
data_folder = os.path.join(phraends_folder, 'static')
file_name = 'phrases_output.txt'
file_path = os.path.join(data_folder, file_name)

# Read in text from file
sentences = read_text_file(file_path)

# Output key phrases onto website
st.write("Key phrases for the stock ticker you entered:")
for i, sentence in enumerate(sentences, start=1):
    st.write(f"{i}. {sentence}")

st.write("""
🔥 Trending Tickers: 
         """)

st.write("""
⏳ Search History: 
""")