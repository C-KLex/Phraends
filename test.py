from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import streamlit as st

options = Options() 
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

url = f"http://www.investopedia.com/search?q=MMM"
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


st.write(links)