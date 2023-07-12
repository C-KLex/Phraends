from transformers import pipeline
import requests
import re
from bs4 import BeautifulSoup


def retrieve_article_text(url):
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, "html.parser")
    article_element = soup.find("div", class_="article__content")
    article_text = article_element.get_text(
        strip=True) if article_element else ""
    return article_text


def generate_summarized_sentences(article_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarized_output = summarizer(
        article_text, max_length=130, min_length=30, do_sample=False)
    summarized_text = summarized_output[0]["summary_text"].strip(
    ) if summarized_output else ""
    sentences = re.split(
        r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", summarized_text)
    return sentences


def main():
    url = "https://www.cnn.com/2023/07/06/tech/twitter-meta-threads-legal-threat/index.html"

    # Retrieve the article
    article_text = retrieve_article_text(url)

    # Generate summarized sentences
    summarized_sentences = generate_summarized_sentences(article_text)

    # Print the summarized sentences
    print("Summarized Sentences:")
    for i, sentence in enumerate(summarized_sentences, start=1):
        print(f"{i}. {sentence}")


if __name__ == "__main__":
    main()
