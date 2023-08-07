from Phraends_Flask.Backend.Edgar_Crawler import edgar_crawler
from Phraends_Flask.Backend.Edgar_Crawler import extract_items
from Phraends_Flask.Backend.Edgar_Crawler import target_content

if __name__ == "__main__":
    edgar_crawler.main()
    extract_items.main()
    target_content.target_content("amzn")
