from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import yfinance as yf

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
    driver = webdriver.Chrome()
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


def get_news_from_investopedia(ticker):
    """
    Summary:
        Search the ticker name in investopedia, and then crawl down the first five articles.

    Args:
        ticker (string): the ticker name of the stock

    Returns:
        links (list): the links to the five articles
        articles (list): the list contains the five articles
    """
    driver = webdriver.Chrome()
    driver.get("https://www.investopedia.com/")

    # Click the search button
    search_point = driver.find_element(By.CLASS_NAME, "general-search__icon-button")
    search_point.click()

    # Send in the ticker name
    search = driver.find_element(
        By.XPATH, "/html/body/header/div[1]/div[3]/ul/li/div/form/div/input"
    )
    search.send_keys(str(ticker))
    search.send_keys(Keys.RETURN)

    # Collect the 5 latest news content
    links = []
    articles = []
    driver.implicitly_wait(5)
    for i in range(0, 5):
        if i == 0:
            elem = driver.find_element(By.XPATH, '//*[@id="search-results__link_1-0"]')
        else:
            elem = driver.find_element(
                By.XPATH, f'//*[@id="search-results__link_1-0-{i}"]'
            )
        url_element = elem.get_attribute("href")
        links.append(url_element)
        # Open the new window
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(url_element)
        time.sleep(1)
        # search_point = driver.find_element(By.XPATH, '//*[@id="mntl-sc-page_1-0"]').text
        try:
            search_point = driver.find_element(
                By.CSS_SELECTOR, "#mntl-sc-block-callout-body_1-0"
            ).text
            articles.append(str(search_point).replace("\n", " "))
        except:
            print("wrong page")
        # window_handles[0] is a first window
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    return links, articles


def get_news_from_dow_jones(ticker):  # apple
    """
    Summary:
        Search the ticker name in Dow Jones, and then crawl down the first five articles.

    Args:
        ticker (string): the ticker name of the stock

    Returns:
        links (list): the links to the five articles
        articles (list): the list contains the five articles
    """
    driver = webdriver.Chrome()
    driver.get("https://www.dowjones.com/")

    # Click the search button
    search_point = driver.find_element(
        By.XPATH, "/html/body/div[2]/header/div/div[2]/a[1]"
    )
    search_point.click()

    # Send in the ticker name
    search = driver.find_element(
        By.XPATH, "/html/body/div[6]/div/div/div/div/div/div[3]/form/input"
    )
    search.send_keys(str(ticker))
    search.send_keys(Keys.RETURN)

    # Collect the 5 latest news content
    links = []
    articles = []
    driver.implicitly_wait(5)
    for i in range(0, 5):
        if i == 0:
            elem = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/section[2]/div/div/ul/li[2]/div[1]/div[2]/h3/a",
            )
        else:
            elem = driver.find_element(
                By.XPATH,
                f"/html/body/div[2]/section[2]/div/div/ul/li[2]/div[{i+1}]/div[2]/h3/a",
            )
        url_element = elem.get_attribute("href")
        links.append(url_element)
        # Open the new window
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(url_element)
        time.sleep(1)
        search_point = driver.find_element(
            By.XPATH, "/html/body/div[2]/section[2]/div/div/div/div"
        ).text
        articles.append(str(search_point).replace("\n", " "))
        # window_handles[0] is a first window
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    return links, articles

  
def get_news_from_cnbc(ticker):
    """
    Summary: 
        Search the ticker name in cnbc, and then crawl down the first five articles.
    
    Args:
        ticker (string): the ticker name of the stock
    
    Returns:
        links (list): the links to the five articles
        open("the_news_texts.txt", mode="r") (txt file): the txt file contains the five articles
    """
    driver = webdriver.Chrome()
    driver.get("https://www.cnbc.com/")

    # Click the search button
    search_point = driver.find_element(By.CLASS_NAME, "icon-search")
    search_point.click()

    # Send in the ticker name
    search = driver.find_element(
        By.XPATH, '//*[@id="SearchEntry-searchForm"]/input[2]'
    )
    search.send_keys(str(ticker))
    search.send_keys(Keys.RETURN)

    # Collect the 5 latest news content
    links = []
    articles = []
    driver.implicitly_wait(5)

    skip_time = 0
    for i in range(0, 5):
        
        try: 
            # club or pro
            skip_sign1 = driver.find_element(By.XPATH, f'//*[@id="QuotePage-latestNews-0-{i}"]/div/div/a[1]/img')
            skip_time = skip_time + 1
            continue

        except:
            
            try:
                # pure video
                skip_sign2 = driver.find_element(By.XPATH, f'//*[@id="QuotePage-latestNews-0-{i}"]/div/div/a/img')
                skip_time = skip_time + 1
                continue

            except:
                try:
                    elem = driver.find_element(By.XPATH, f'//*[@id="QuotePage-latestNews-0-{i}"]/div/div/a')
                    url_element = elem.get_attribute("href")
                    links.append(url_element)
                    # Open the new window
                    driver.execute_script("window.open()")
                    driver.switch_to.window(driver.window_handles[i-skip_time + 1])
                    driver.get(url_element)
                    time.sleep(5)
                    try: 
                        search_point = driver.find_element(By.CLASS_NAME, 'ArticleBody-articleBody').text
                        articles.append(str(search_point).replace("\n", " "))
                    except:
                        print("can't find article body")
                    # window_handles[0] is a first window
                    driver.switch_to.window(driver.window_handles[0])  

                except: 
                    pass

    driver.quit()
    return links, articles


def main(ticker: str):
    """
    Summary:
        Call every functions that can crawl the articles, and append all the articles to one list.

    Args:
        ticker (string): the ticker name of the stock

    Returns:
        articles (list): the list contains the articles
    """
    company_name = get_company_name_from_ticker_name(ticker)
    articles = []
    investo = get_news_from_investopedia(ticker)[1]
    dow = get_news_from_dow_jones(company_name)[1]
    cnbc = get_news_from_cnbc(ticker)[1]

    articles.append(investo)
    articles.append(dow)
    articles.append(cnbc)

    return articles


if __name__ == "__main__":
    main()
