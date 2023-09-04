import streamlit as st

from Phraends_Pkg.Backend.Crawler.Crawler import Crawler
from Phraends_Pkg.Backend.Model_API.ModelAPI import ModelAPI

model_api = ModelAPI(True, st.secrets["openai_key"]) # st["openai_key"] will make error when running locally
crawler = Crawler()


def get_5_summary_from_5_articles(ticker: str):
    """
    Summary:
        API for frontend to get 5 summaries from 5 news articles
    
    Args:
        ticker: desired stock ticker

    Returns:
        link_list: 5 links corresponding to the 5 news articles
        summary_list: 5 summaries corresponding to the 5 news articles
    """
    
    link_list = [] 
    summary_list = [] 

    link_list, raw_article_list = crawler.get_articles(ticker)
    summary_list = model_api.main(raw_article_list)
    
    return link_list, summary_list

def get_summary_from_annualreport(ticker, year, section):
    """
    Summary:
        API for frontend to get summaries from annual report
    
    Args:
        ticker: desired stock ticker
        year: desire year of annual report
        section: one of three from 'Risk Factors', 'Quantitative and Qualitative Disclosure' and 'Management Discussion'
        
    Returns:
        years: A list of integer that length will be 10
    """
    # Currently a mock API
    return ['summary1', 'summary2', 'summary3', 'summary4', 'summary5']