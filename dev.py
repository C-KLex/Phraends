from Phraends_Flask.Backend.Edgar_Crawler import edgar_crawler
from Phraends_Flask.Backend.Edgar_Crawler import extract_items

if __name__ == "__main__":
    edgar_crawler.main()
    extract_items.main()
