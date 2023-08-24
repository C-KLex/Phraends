import streamlit as st
import pandas as pd
import os
import yfinance as yf
import plotly.graph_objects as go

import Phraends_Flask.util.get_yearlist
from Phraends_Flask.util.save_search_history import save_search_history
from Phraends_Flask.util.get_trending_tickers import get_top_trending_tickers
from Phraends_Flask.util.phrases_output import phrases_output_example

# Text heading for website
st.title("Phraends")
st.write("NLP Application for Summarizing Financial News")

# add the drop down menu
sp500_df = pd.read_csv('constituents.csv')
sp500_ls = sp500_df['Symbol'].tolist()
sections = ['Risk Factors', 'Quantitative and Qualitative Disclosure', 'Management Discussion']
years = Phraends_Flask.util.get_yearlist.get_yearlist()


tab1, tab2= st.tabs(["News", "Annual Reports"])

with tab1:
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

        # get link and summary
        links, summaries = Phraends_Flask.get_5_summary_from_5_articles(ticker)

        # new: Output key phrases onto website
        st.write("Key links and summaries for the stock ticker you entered:")
        for i, (link, summary) in enumerate(zip(links, summaries)):
            num = i + 1
            st.write(f'{num}. link: ' + link)
            st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; summary: ' + summary)

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

with tab2:

    ticker = st.selectbox('Please enter a stock ticker that you would like to learn more about:', sp500_ls, key="2")
    year = st.selectbox('Year:', years)
    section = st.selectbox('Section:', sections)

    st.write("")
    button = st.button("Run")

    if button:
        api_returns = Phraends_Flask.get_summary_from_annualreport(ticker, year, section)
        for num in range(len(api_returns)):
            st.write(str(num+1) + ". ", api_returns[num])
