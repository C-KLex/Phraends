from transformers import pipeline

def generate_summarized_text(article_text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Split the article text into smaller chunks
    max_chunk_length = 4500 
    chunks = [article_text[i:i+max_chunk_length] for i in range(0, len(article_text), max_chunk_length)]

    sum_texts = []

    for chunk in chunks:
        summarized_output = summarizer(chunk, max_length=300, min_length=50, do_sample=False)
        sum_text = summarized_output[0]["summary_text"].strip() if summarized_output else ""
        sum_texts.append(sum_text)

    # Combine the summarized chunks into the final summarized text
    summarized_text = " ".join(sum_texts)

    return summarized_text