from transformers import pipeline
from Phraends_Flask.Backend.Crawler import Scrape

def generate_summarized_text(article_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarized_output = summarizer(article_text, max_length=130, min_length=30, do_sample=False)
    summarized_text = summarized_output[0]["summary_text"].strip() if summarized_output else ""
    return summarized_text

def main(article_text):
    summarized_text = generate_summarized_text(article_text)
    return summarized_text

if __name__ == "__main__":
    main()