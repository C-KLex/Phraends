from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


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
        open("the_news_texts.txt", mode="r") (txt file): the txt file contains the five articles
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
    driver.implicitly_wait(5)
    f = open("the_news_texts.txt", "w")
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
        search_point = driver.find_element(By.XPATH, '//*[@id="mntl-sc-page_1-0"]').text
        f.write("This is the %dth article \r\n\n" % (i + 1))
        f.write(str(search_point))
        f.write("\n\n\n")
        # window_handles[0] is a first window
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    return (
        links,
        open("the_news_texts.txt", mode="r"),
    )  # type .read() can read the content


def get_news_from_dow_jones(ticker):  # apple
    """
    Summary: 
        Search the ticker name in Dow Jones, and then crawl down the first five articles.
    
    Args:
        ticker (string): the ticker name of the stock
    
    Returns:
        links (list): the links to the five articles
        open("the_news_texts.txt", mode="r") (txt file): the txt file contains the five articles
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
    driver.implicitly_wait(5)
    f = open("the_news_texts.txt", "w")
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
        f.write("This is the %dth article \r\n\n" % (i + 1))
        f.write(str(search_point))
        f.write("\n\n\n")
        # window_handles[0] is a first window
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    return (
        links,
        open("the_news_texts.txt", mode="r"),
    )  # type .read() can read the content


def get_news_from_cnbc(ticker):
    """
    Summary: 
        Search the ticker name in cnbd, and then crawl down the first five articles.
    
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
        By.XPATH, "/html/body/div[3]/div/div[1]/header/div[3]/div/div/div[3]/section/div[2]/div[1]/section/form/input[2]"
    )
    search.send_keys(str(ticker))
    search.send_keys(Keys.RETURN)

    # Collect the 5 latest news content
    links = []
    driver.implicitly_wait(5)
    f = open("the_news_texts.txt", "w")
    for i in range(0, 5):
        if i == 0:
            elem = driver.find_element(By.XPATH, '//*[@id="QuotePage-latestNews-0-0"]/div/div/a')
        else:
            elem = driver.find_element(
                By.XPATH, f'//*[@id="QuotePage-latestNews-0-{i+1}"]/div/div/a'
            )
        
        url_element = elem.get_attribute("href")
        links.append(url_element)
        # Open the new window
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(url_element)
        time.sleep(1)
        search_point = driver.find_element(By.XPATH, '//*[@id="SpecialReportArticle-ArticleBody-6"]').text
        f.write("This is the %dth article \r\n\n" % (i + 1))
        f.write(str(search_point))
        f.write("\n\n\n")
        # window_handles[0] is a first window
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    return (
        links,
        open("the_news_texts.txt", mode="r"),
    )  # type .read() can read the content


def get_news_from_barrons(ticker):
    """
    Summary: 
        Search the ticker name in barrons, and then crawl down the first five articles.
    
    Args:
        ticker (string): the ticker name of the stock
    
    Returns:
        links (list): the links to the five articles
        open("the_news_texts.txt", mode="r") (txt file): the txt file contains the five articles
    """
    driver = webdriver.Chrome()
    driver.get("https://www.barrons.com/")

    # Click the search button
    search_point = driver.find_element(By.CLASS_NAME, "NavBarButtonSearch__Search-sc-bktrl8-0 dLJnEY")
    search_point.click()

    # Send in the ticker name
    search = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div[1]/div/header/div/div[3]/div[2]/form/div/input"
    )
    search.send_keys(str(ticker))
    search.send_keys(Keys.RETURN)

    # Collect the 5 latest news content
    links = []
    driver.implicitly_wait(5)
    f = open("the_news_texts.txt", "w")
    for i in range(0, 5):
        if i == 0:
            elem = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div[3]/div[1]/div[2]/article[1]/div[1]/div[2]/h4/a')
        else:
            elem = driver.find_element(
                By.XPATH, f'//*[@id="root"]/div/div/div/div[1]/div/div/div[3]/div[1]/div[2]/article[{i+1}]/div[1]/div[2]/h4/a'
            )
        
        url_element = elem.get_attribute("href")
        links.append(url_element)
        # Open the new window
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(url_element)
        time.sleep(1)
        search_point = driver.find_element(By.XPATH, '/html/body/div[8]/div[6]/div[2]/article/div[2]').text
        f.write("This is the %dth article \r\n\n" % (i + 1))
        f.write(str(search_point))
        f.write("\n\n\n")
        # window_handles[0] is a first window
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    return (
        links,
        open("the_news_texts.txt", mode="r"),
    )  # type .read() can read the content