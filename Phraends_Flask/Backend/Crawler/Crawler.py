from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def get_link_of_10q_10k(ticker):
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
    return links, open("the_news_texts.txt", mode="r")  # .read()
