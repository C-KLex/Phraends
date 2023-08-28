from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page: {url}")
        return ""

    articles = []
    soup = BeautifulSoup(response.content, 'html.parser')

    # Determine class name based on URL domain
    domain = urlparse(url).netloc
    if "investopedia.com" in domain:
        class_name = "article-body"
    elif "cnn.com" in domain:
        class_name = "article__content"
    elif "dowjones.com" in domain:
        class_name = "main"
    elif "cnbc.com" in domain:
        class_name = "ArticleBody-articleBody"
    elif "wcvb.com" in domain:
        class_name = "article-content--body-text"
    elif "foxnews.com" in domain:
        class_name = "article-body"
    elif "yahoo.com" in domain:
        class_name = "caas-body-section"
    elif "reuters.com" in domain:
        class_name = "article-body__content__17Yit"   
    else:
        print(f"Unsupported domain: {domain}")
        return ""

    article_body = soup.find("div", class_=class_name)
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
