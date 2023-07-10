from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# Go to SEC company search website
driver.get("https://www.sec.gov/edgar/searchedgar/companysearch")

# Enter the company name we want to look up
search = driver.find_element(By.ID, "edgar-company-person")
search.send_keys("MSFT")
search.send_keys(Keys.RETURN)

# Wait for the internet to work
wait = WebDriverWait(driver, 10)
time.sleep(5)

# Get the most recent three 10-Q and one 10-K report
link1 = driver.find_element(
    By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[1]/a[1]"
).get_attribute("href")
link2 = driver.find_element(
    By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[2]/a[1]"
).get_attribute("href")
link3 = driver.find_element(
    By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[3]/a[1]"
).get_attribute("href")
link4 = driver.find_element(
    By.XPATH, "/html/body/main/div[4]/div[2]/div[3]/div/div/ul/li[4]/a[1]"
).get_attribute("href")

