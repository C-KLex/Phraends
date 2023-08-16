import streamlit as st
import pandas as pd
import numpy as np

st.title("Phraends")

st.write("""
NLP Application for Summarizing Finance Article
 """)

# add the drop down menu
sp500_df = pd.read_csv('constituents.csv')
sp500_ls = sp500_df['Symbol'].tolist()
ticker = st.selectbox('Please enter a stock ticker that you would like to learn more about:', sp500_ls)

# ticker = st.text_input('Please enter a stock ticker that you would like to learn more about:')

st.write("""1. """, ticker)
st.write("""2. """, """phrase2""")
st.write("""3. """, """phrase3""")
st.write("""4. """, )
st.write("""5. """, )

st.write("""
🔥 Trending Tickers: 
         """)

st.write("""
⏳ Search History: 
""")