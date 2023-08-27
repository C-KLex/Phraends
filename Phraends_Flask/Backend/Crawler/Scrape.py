import requests
from bs4 import BeautifulSoup

def scrape_cnn(url):
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, "html.parser")
    article_element = soup.find("div", class_="article__content")
    article_text = article_element.get_text(strip=True) if article_element else ""
    return article_text

def scrape_investopedia(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page: {url}")
        return ""

    articles = []
    soup = BeautifulSoup(response.content, 'html.parser')
    article_body = soup.find("div", class_="article-body")
    if article_body:
        paragraphs = article_body.find_all("p")
        for paragraph in paragraphs:
            # Remove leading/trailing spaces and newlines
            paragraph_text = paragraph.get_text().strip()  
            articles.append(paragraph_text)

    # Combine paragraphs into a single text with spaces but no commas
    article_text = " ".join(articles)
    article_text = article_text.replace(",", "")

    return article_text

#def scrape_cnbc(url):

#def scrape_dow_jones(url):