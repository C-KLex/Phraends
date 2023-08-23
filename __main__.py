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
sp500_ls.insert(0, "")
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

# Get user inputs for customization of stock chart
chart_title = st.subheader("Stock Chart")
chart_type = st.selectbox("Select Chart Type:", ["Line", "Area","Candle", "Hollow Candle", "Bar", "Colored Bar", "Histogram", "Scatter"])
time_interval = st.selectbox("Select Time Interval:", ["1 min", "2 mins", "5 mins","30 mins", "1 hour","1 day", "1 week", "1 month", "3 months"])
time_period = st.selectbox("Select Time Period:", ["1D", "5D", "1M", "3M", "6M", "1Y", "2Y", "5Y", "10Y", "YTD", "Max"])
show_volume = st.checkbox("Show Volume")

# Print stock chart of selected ticker onto website
if ticker:
    # Set the appropriate frequency string based on the selected time interval
    if time_interval == "1 min":
        interval = "1m"
    elif time_interval == "2 mins":
        interval = "2m"
    elif time_interval == "5 mins":
        interval = "5m"
    elif time_interval == "30 mins":
        interval = "30m"
    elif time_interval == "1 hour":
        interval = "1h"
    elif time_interval == "1 day":
        interval = "1d"
    elif time_interval == "1 week":
        interval = "1wk"
    elif time_interval == "1 month":
        interval = "1mo"
    elif time_interval == "3 months":
        interval = "3mo"

    # Set the appropriate time period string based on the selected time period
    if time_period == "1D":
        period = "1d"
    elif time_period == "5D":
        period = "5d"
    elif time_period == "1M":
        period = "1mo"
    elif time_period == "3M":
        period = "3mo"
    elif time_period == "6M":
        period = "6mo"
    elif time_period == "1Y":
        period = "1y"
    elif time_period == "2Y":
        period = "2y"
    elif time_period == "5Y":
        period = "5y"
    elif time_period == "10Y":
        period = "10y"
    elif time_period == "YTD":
        period = "ytd"
    elif time_period == "Max":
        period = "max"

    # Check if the selected period and interval combination is valid
    valid_combinations = {
        "1 min": ["1d", "5d"],
        "2 mins": ["5d", "1wk", "1mo"],
        "5 mins": ["5d", "1wk", "1mo"],
        "30 mins": ["5d", "1wk", "1mo"],
        "1 hour": ["5d", "1wk", "1mo", "3mo", "6mo", "1y", "2y"],
        "1 day": ["5d", "1wk", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
        "1 week": ["5d", "1wk", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
        "1 month": ["5d", "1wk", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
        "3 months": ["5d", "1wk", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
        "1 year": ["5d", "1wk", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"],
    }
    
    # Error checking for valid combinations of time period and time interval (e.g., cannot show 1min candles on 10year chart)
    if period not in valid_combinations[time_interval]:
        st.error("Selected combination of period and interval is not compatible. Please choose a different period and interval.")
    else:
        stock_data = yf.download(ticker, period=period, interval=interval)
        
        # Print chart to website
        if not stock_data.empty:
            fig = go.Figure()

            # Print appropriate chart type based on what user has selected
            if chart_type == "Line":
                fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close'))
            elif chart_type == "Candle":
                fig.add_trace(go.Candlestick(x=stock_data.index,
                                            open=stock_data['Open'],
                                            high=stock_data['High'],
                                            low=stock_data['Low'],
                                            close=stock_data['Close']))
            elif chart_type == "Area":
                fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], fill='tozeroy', mode='none', name='Close'))
            elif chart_type == "Hollow Candle":
                # Create hollow candlestick chart using rectangles
                hollow_candles = stock_data[stock_data['Close'] > stock_data['Open']]
                fig.add_trace(go.Scatter(x=hollow_candles.index, y=hollow_candles['High'], mode='markers', marker=dict(size=5), name='High'))
                fig.add_trace(go.Scatter(x=hollow_candles.index, y=hollow_candles['Low'], mode='markers', marker=dict(size=5), name='Low'))
                fig.add_shape(type="rect", x0=hollow_candles.index, y0=hollow_candles['Open'], x1=hollow_candles.index, y1=hollow_candles['Close'], fillcolor='white', line=dict(color='black'))
            elif chart_type == "Bar":
                fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Close'], name='Close'))
            elif chart_type == "Colored Bar":
                # Create colored bar chart based on the daily price change
                price_change = stock_data['Close'] - stock_data['Open']
                fig.add_trace(go.Bar(x=stock_data.index, y=price_change, marker_color=price_change, name='Price Change'))
            elif chart_type == "Histogram":
                # Create histogram of daily price changes
                price_change = stock_data['Close'] - stock_data['Open']
                fig.add_trace(go.Histogram(x=price_change, nbinsx=20, name='Price Change'))
            elif chart_type == "Scatter":
                # Create scatter plot of open and close prices
                fig.add_trace(go.Scatter(x=stock_data['Open'], y=stock_data['Close'], mode='markers', name='Open vs Close'))
            
            if show_volume:
                fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'], name='Volume'))

            fig.update_layout(title=f"{ticker} Stock Chart",
                            xaxis_title='Date',
                            yaxis_title='Price',
                            xaxis_rangeslider_visible=False,
                            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
            st.plotly_chart(fig)
        else:
            st.error(f"No stock data found for {ticker}. Please check the ticker symbol.")
