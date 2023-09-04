from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import yfinance as yf
import streamlit as st

from Phraends_Pkg.Backend.Crawler import Scrape


WEBDRIVER_PATH = "./Phraends_Pkg/Backend/Crawler/chromedriver.exe"


def get_chrome_driver():
    options = Options() 
    options.add_argument("--headless=new")
    options.add_argument('--disable-gpu')
    
    #options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver = webdriver.Chrome(options=options)
    return driver
    
class Crawler:
    
    def __init__(self):
        self.WEBDRIVER_PATH = "./Phraends_Pkg/Backend/Crawler/chromedriver.exe"

    def get_company_name_from_ticker_name(self, ticker: str):
        """
        Summary:
            To avoid the problem that specific websites cannot obtain article from ticker name,
            we write this function to obtain the company name of the stock ticker.

        Args:
            ticker (string): the ticker name of the stock.

        Returns:
            company name (string): the name of the company.
        """
        company_name = yf.Ticker(ticker).info["longName"].split(" ", 1)[0]
        return company_name


    def get_link_of_10q_10k(self, ticker):
        """
        Summary:
            WebCrawl the most recent quarterly and annually report from SEC

        Description:
            Currently this function only returns the links of the reports.

        Args:
            ticker (string): the ticker name of the stock

        Returns:
            list_of_links (list): The list contains the four links of the reports.
        """
        driver = get_chrome_driver()
        # Go to SEC company search website
        driver.get("https://www.sec.gov/edgar/searchedgar/companysearch")

        # Enter the company name we want to look up
        search = driver.find_element(By.ID, "edgar-company-person")
        search.send_keys(ticker)
        search.send_keys(Keys.RETURN)

        # Wait for the internet to work
        wait = WebDriverWait(driver, 10)
        time.sleep(5)

        list_of_links = []
        # Get the most recent three 10-Q and one 10-K report
        link1 = driver.find_element(
            By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[1]/a[1]"
        ).get_attribute("href")
        list_of_links.append(link1)
        link2 = driver.find_element(
            By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[2]/a[1]"
        ).get_attribute("href")
        list_of_links.append(link2)

        link3 = driver.find_element(
            By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[3]/a[1]"
        ).get_attribute("href")
        list_of_links.append(link3)

        link4 = driver.find_element(
            By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[4]/a[1]"
        ).get_attribute("href")
        list_of_links.append(link4)

        return list_of_links


    def get_news_link_from_investopedia(self, ticker):
        """
        ticker names -> 5 string (links or empty string but 5 members in total) 
        """
        url = f"http://www.investopedia.com/search?q={ticker}"
        driver = get_chrome_driver()
        driver.get(url)


        links = []
        search_result_block_links = driver.find_elements(By.CSS_SELECTOR, "#search-results__results_1-0 a")


        for e in search_result_block_links:
            l = e.get_attribute("href")
            links.append(str(l))
        
        try:
            end_index = links.index("None")
            links = links[:end_index]
        except:
            pass 

        return links

    def get_news_link_from_cnbc(self, ticker):
        """
            ticker names -> 5 string (links or empty string but 5 members in total) 
        """
        def is_valid_link(link):

            if link == "https://www.cnbc.com/investingclub/":
                return False 
            elif link == "https://www.cnbc.com/pro/":
                return False
            elif link.startswith("https://www.cnbc.com/video/"):
                return False

            return True

        url = f"https://www.cnbc.com/quotes/{ticker}?qsearchterm={ticker}"
        driver = get_chrome_driver()
        driver.get(url)

        links = []
        latest_on_block = driver.find_elements(By.CSS_SELECTOR, "#MainContentContainer > div > div.QuotePageBuilder-row > div.QuotePageBuilder-mainContent.QuotePageBuilder-col > div.QuotePageTabs > div:nth-child(3) a")
        for e in latest_on_block:

            l = e.get_attribute("href")

            if not is_valid_link(l):
                continue 

            links.append(str(l))

        content_from_out_affiliate_block = driver.find_elements(By.CSS_SELECTOR, "#MainContentContainer > div > div.QuotePageBuilder-row > div.QuotePageBuilder-mainContent.QuotePageBuilder-col > div.QuotePageTabs > div:nth-child(5) a")
        for e in content_from_out_affiliate_block:

            l = e.get_attribute("href")

            links.append(str(l))
            
        return links[0:5]

    def random_pick_links(self, links, num=5):
        """
        Summary:
            A function that helps to pick url randomly.

        Args:
            links (list[str]): A list of urls
            num (int, optional): The number of desire output links. Defaults to 5.

        Returns:
            list[str]: A list of urls that pick randomly from links.
        """
        if num < len(links):
            rlinks = random.sample(links, num)
        return rlinks

    def scrape_links(self, links):
        """
        Summary:
            Get articlse from links by using scrape.py. It will also delete websites that need subscription.

        Args:
            links (list[str]): A list of urls

        Returns:
            list[str]: A list of urls
            list[str]: A list of articles
        """
        articles = []
        remove_list = []
        for link in links:
            article = Scrape.scrape_article(link)
            if len(article) > 400:
                articles.append(article)
            else:
                remove_list.append(link)
        
        for link in remove_list:
            links.remove(link)

        return links, articles

    def get_articles(self, ticker):
        """
        Summary:
            The main funtion of crawler. It will return a list of links and a list of articles from finance websites.

        Args:
            ticker (str): Ticker name of a company

        Returns:
            list[str]: A list of urls
            list[str]: A list of articles
        """
        links = self.get_news_link_from_investopedia(ticker)  + self.get_news_link_from_cnbc(ticker)
        rlinks = self.random_pick_links(links)
        rlinks, articles = self.scrape_links(rlinks)
        print(articles)
        return rlinks, articles