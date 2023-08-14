# from Phraends_Flask.Backend.Edgar_Crawler import edgar_crawler
# from Phraends_Flask.Backend.Edgar_Crawler import extract_items
# from Phraends_Flask.Backend.Edgar_Crawler import target_content
from Phraends_Flask.Backend.Crawler import Crawler

if __name__ == "__main__":
    ticker = "GM"
    # Websites
    website_articles, links = Crawler.main(ticker)
    print(website_articles)
    print(links)
    # SEC
    # target_content.indict_target_company(ticker)
    # edgar_crawler.main()
    # extract_items.main()
    # print(target_content.target_content(ticker))
