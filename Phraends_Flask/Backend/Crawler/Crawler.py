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
