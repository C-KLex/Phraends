import streamlit as st  
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

import Phraends_Pkg.Backend as backend
from Phraends_Pkg.Frontend import Frontend_Util

CONSTITUENTS_CSV_PATH = "./Phraends_Pkg/Frontend/constituents.csv"

class App():

    def __init__(self):
        # register the var used globally within the class
        self.sp500_ls = None 
        self.sections = None 
        self.years = None 

    def main_view(self):

        # Text heading for website
        st.title("Phraends")
        st.write("NLP Application for Summarizing Financial News")

        # add the drop down menu
        sp500_df = pd.read_csv(CONSTITUENTS_CSV_PATH)
        self.sp500_ls = sp500_df['Symbol'].tolist()
        self.sections = ['Risk Factors', 'Quantitative and Qualitative Disclosure', 'Management Discussion']
        self.years = Frontend_Util.get_year_list()

        tab1, tab2= st.tabs(["News", "Annual Reports"])

        with tab1:
            self.news_tap_view() 

        with tab2:
            self.annual_report_view()

        return 

    def news_tap_view(self):
        
        ticker = st.selectbox('Please enter a stock ticker that you would like to learn more about:', self.sp500_ls)
        
        st.write("")
        tab1_button = st.button("Run", key="tab1")

        if tab1_button:
            
            self.news_tap_summary_section_view(ticker)
            self.news_tap_stock_price_section_view(ticker)

        return 
    
    def news_tap_summary_section_view(self, ticker):
        links, summaries = backend.get_5_summary_from_5_articles(ticker)

        st.write("Key links and summaries for the stock ticker you entered:")
        for i, (link, summary) in enumerate(zip(links, summaries)):
            num = i + 1
            st.write(f'{num}. link: ' + link)
            st.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; summary: ' + summary)
        
        return 

    def news_tap_stock_price_section_view(self, ticker):

        stock_data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
        
        if stock_data.empty:
            st.write(f"No stock data found for {ticker}. Please check the ticker symbol.") 

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

        return 

    def annual_report_view(self):
        ticker = st.selectbox('Please enter a stock ticker that you would like to learn more about:', self.sp500_ls, key="2")
        year = st.selectbox('Year:', self.years)
        section = st.selectbox('Section:', self.sections)

        st.write("")
        tab2_button = st.button("Run",key="tab2")

        if tab2_button:
            api_returns = Phraends_Flask.get_summary_from_annualreport(ticker, year, section)
            for num in range(len(api_returns)):
                st.write(str(num+1) + ". ", api_returns[num])
        
        return 