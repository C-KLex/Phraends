from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options() 
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.get('https://www3.nohhi.co.jp/rktrace/trace.html')

search_bar = driver.find_element(By.NAME, "command5")
search_bar.send_keys(num)
search_bar.submit()