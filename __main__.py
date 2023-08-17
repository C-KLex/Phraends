import streamlit as st
import pandas as pd
import os
import yfinance as yf
import plotly.graph_objects as go

from Phraends_Flask.util.save_search_history import save_search_history
from Phraends_Flask.util.get_trending_tickers import get_top_trending_tickers
from Phraends_Flask.util.phrases_output import phrases_output_example

# Text heading for website
st.title("Phraends")
st.write("NLP Application for Summarizing Financial News")

# add the drop down menu
sp500_df = pd.read_csv('constituents.csv')
sp500_ls = sp500_df['Symbol'].tolist()
ticker = st.selectbox('Please enter a stock ticker that you would like to learn more about:', sp500_ls)

# Create path to find search history within 'util' folder
phraends_folder = os.path.join(os.getcwd(), 'Phraends_Flask')
data_folder = os.path.join(phraends_folder, 'util')
search_history_csv = os.path.join(data_folder, 'search_history.csv')
search_history_df = pd.read_csv(search_history_csv, header=0,usecols=["Ticker"])

# Get top 5 trending tickers and print them on website
trending_tickers = get_top_trending_tickers(search_history_csv)
st.write("🔥 Trending Tickers: " + ", ".join(trending_tickers))

# Get 5 most recent searched tickers and print them on website
most_recent_tickers = search_history_df['Ticker'].tail(5).tolist()
st.write("⏳ Search History: ", ", ".join(most_recent_tickers))

# Once the user enters a ticker, save search history, run model, and output key phrases
if ticker:
    # Save the user-entered ticker to search history
    save_search_history(ticker)

    # Run the function that generates key phrases into a list (this will be replaced by model function eventually)
    key_phrases = phrases_output_example()

    # Output key phrases onto website
    st.write("Key phrases for the stock ticker you entered:")
    for i, sentence in enumerate(key_phrases, start=1):
        st.write(f"{i}. {sentence}")


# Print stock chart of selected ticker onto website
if ticker:
    stock_data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
    if not stock_data.empty:
        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                            open=stock_data['Open'],
                                            high=stock_data['High'],
                                            low=stock_data['Low'],
                                            close=stock_data['Close'])])
        fig.update_layout(title=f'{ticker} Stock Chart',
                          xaxis_title='Date',
                          yaxis_title='Price',
                          xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)
    else:
        st.write(f"No stock data found for {ticker}. Please check the ticker symbol.")
