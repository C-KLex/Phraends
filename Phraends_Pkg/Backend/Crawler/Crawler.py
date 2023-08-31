from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import yfinance as yf

WEBDRIVER_PATH = "./Phraends_Pkg/Backend/Crawler/chromedriver.exe"

def get_chrome_driver():
    service = Service(executable_path = WEBDRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def get_company_name_from_ticker_name(ticker: str):
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


def get_link_of_10q_10k(ticker):
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


def get_news_link_from_investopedia(ticker):
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
    
    end_index = links.index("None")
    links = links[:end_index]

    # pick first links if available
    picked_links = [] 
    if len(links) != 5:
        picked_links += [""] * (5 - len(picked_links))

    return picked_links[:5] 

def get_news_from_cnbc(ticker):
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

    for l in links:
        print(l)

    if len(links) != 5:
        links += [""] * (5 - len(links))

    return links[:5]

