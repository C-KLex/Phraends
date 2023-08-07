import json
import pandas as pd
from sec_cik_mapper import StockMapper
from datetime import datetime
from Phraends_Flask.Backend.Edgar_Crawler.datasets import EXTRACTED_FILINGS


def get_key(dictionary: dict):
    smallest_val = min(dictionary.values())
    for key, value in dictionary.items():
        if value == smallest_val:
            return key
    return "key doesn't exist"


def target_content(ticker: str):
    """
    Summary:
        Obtain the wanted parts in annual report.

    Args:
        ticker (string): the ticker name of the stock.

    Returns:
        sec_content (list): a list containing the parts of annual report we want.
    """
    # Open JSON file
    with open("Phraends_Flask/Backend/Edgar_Crawler/config.json") as f:
        data = json.load(f)

    # Open FILINGS_METADATA.csv
    filings = pd.read_csv(
        "Phraends_Flask/Backend/Edgar_Crawler/datasets/FILINGS_METADATA.csv",
        parse_dates=["Date"],
    )
    # Initialize a stock mapper instance
    mapper = StockMapper()
    # Get mapping from ticker to company name
    company_name = mapper.ticker_to_company_name[ticker.upper()].upper()
    target_rows = filings[filings["Company"] == company_name]
    date_before = datetime(int(data["edgar_crawler"]["start_year"]), 1, 1)
    # Only obtain the latest annual report
    target_rows = target_rows[target_rows["Date"] > date_before].iloc[-1]
    target_filename = target_rows["filename"].replace(".htm", ".json")

    # Open JSON file
    with open(
        f"Phraends_Flask/Backend/Edgar_Crawler/datasets/EXTRACTED_FILINGS/{target_filename}"
    ) as f:
        data = json.load(f)

    sec_content = []
    order_risk = {}
    order_quant = {}
    order_manage = {}
    # Iterating through the json list
    # for i in data:
    #     print(i)
    for key, value in data.items():
        if key in [
            "item_1",
            "item_1A",
            "item_1B",
            "item_2",
            "item_3",
            "item_4",
            "item_5",
            "item_6",
            "item_7",
            "item_7A",
            "item_8",
            "item_9",
            "item_9A",
            "item_9B",
            "item_10",
            "item_11",
            "item_12",
            "item_13",
            "item_14",
            "item_15",
        ]:
            value.replace("\n", " ").replace("\t", " ").replace("\u2019", "'")
            position_risk = value.find("Risk Factors")
            position_quant = value.find(
                "Quantitative and Qualitative Disclosures About Market Risk"
            )
            position_manage = value.find(
                "Management\u2019s Discussion and Analysis of Financial Condition and Results of Operations"
            )

            if position_risk != -1:
                order_risk[key] = position_risk
            if position_quant != -1:
                order_quant[key] = position_quant
            if position_manage != -1:
                order_manage[key] = position_manage

    sec_content.append(
        data[get_key(order_risk)]
        .replace("\n", " ")
        .replace("\t", " ")
        .replace("\u2019", "'")
    )
    sec_content.append(
        data[get_key(order_quant)]
        .replace("\n", " ")
        .replace("\t", " ")
        .replace("\u2019", "'")
    )
    sec_content.append(
        data[get_key(order_manage)]
        .replace("\n", " ")
        .replace("\t", " ")
        .replace("\u2019", "'")
    )
    # Closing file
    f.close()
    return sec_content


# if __name__ == "__main__":
#     target_content("aapl")
