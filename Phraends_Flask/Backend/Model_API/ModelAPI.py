import openai
import random
from Phraends_Flask.Backend.Crawler import Crawler
import streamlit as st 

def choose_random_articles(article_n, num=5):
    if num > len(article_n):
        num = len(article_n)

    article_5 = random.sample(article_n, num)
    return article_5

def summarize_article(article):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please summarize the articles."
            },
            {
                "role": "user",
                "content": article
            }
        ],
        temperature=0.5,
        max_tokens=130,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )

    return response['choices'][0]['message']['content']

def main(article_5):
    
    openai.api_key = st.secrets["openai_key"]

    all_summaries = []

    # Set this to True if you want to test the function
    USE_AI = False

    for i, article in enumerate(article_5, start=1):
        
        if USE_AI:
            # Generate summarized text for each article
            summary = summarize_article(article)
            all_summaries.append(f"{i}. {summary}")

        else:
            # Just print something instead of running the function
            all_summaries.append(f"Article {i} summary: This is a placeholder summary.")

    return all_summaries

if __name__ == "__main__":
    main()

