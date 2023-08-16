import openai
from Phraends_Flask.Backend.Crawler import Crawler

def summarize_article(article_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Please summarize the articles."
            },
            {
                "role": "user",
                "content": article_text
            }
        ],
        temperature=0.5,
        max_tokens=130,
        top_p=1.0,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )

    return response['choices'][0]['message']['content']

def main(article_texts):
    
    openai.api_key = 'KEY PLACEHOLDER'

    all_summaries = []

    # Set this to True if you want to test the function
    USE_AI = False

    for i, article_text in enumerate(article_texts, start=1):
        
        if USE_AI:
            # Generate summarized text for each article
            summary = summarize_article(article_text)
            all_summaries.append(f"{i}. {summary}")

        else:
            # Just print something instead of running the function
            all_summaries.append(f"Article {i} summary: This is a placeholder summary.")

    return all_summaries

if __name__ == "__main__":
    main()

