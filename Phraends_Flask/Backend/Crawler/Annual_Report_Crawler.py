from Phraends_Flask.Backend.Edgar_Crawler import edgar_crawler
from Phraends_Flask.Backend.Edgar_Crawler import extract_items
from Phraends_Flask.Backend.Edgar_Crawler import target_content


def main():
    ticker = "GM"
    # SEC
    # Tell the function which company we are interested in
    target_content.indict_target_company(ticker)
    # Start downloading it
    edgar_crawler.main()
    extract_items.main()
    # Extract the parts we want
    sec_target_content = target_content.target_content(ticker)
    print(sec_target_content)
