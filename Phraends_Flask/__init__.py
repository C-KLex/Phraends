from Phraends_Flask.Backend.Crawler import Crawler
from Phraends_Flask.Backend.Model_API import ModelAPI

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

    link_list, raw_article_list = Crawler.main(ticker)
    summary_list = ModelAPI.main(raw_article_list)

    return link_list, summary_list