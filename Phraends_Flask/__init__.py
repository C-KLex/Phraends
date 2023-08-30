from Phraends_Flask.Backend.Crawler import Crawler
from Phraends_Flask.Backend.Model_API import ModelAPI
from Phraends_Flask.Backend.Crawler import Scrape
from Phraends_Flask.Backend.Model_API import URLBart
from Phraends_Flask.Backend.Crawler import Scrape
from Phraends_Flask.Backend.Model_API import URLBart

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

def get_summary_from_url(url):
    """
    Summary:
        use BART model to summarize the article from given url
    
    Args:
        url: links from certain news websites

    Returns:
        summarized_text: summary corresponding to the url
    """
    article_text = scrape_article(url)
    summarized_text = generate_summarized_text(article_text)

    return summarized_text
