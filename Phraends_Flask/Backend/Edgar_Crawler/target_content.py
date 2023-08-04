import json
from Phraends_Flask.Backend.Edgar_Crawler.datasets import EXTRACTED_FILINGS
import sys


def get_key(dictionary: dict):
    smallest_val = min(dictionary.values())
    for key, value in dictionary.items():
        if value == smallest_val:
            return key
    return "key doesn't exist"


sys.path.append(
    "/Users/jordanwen/Desktop/sec/edgar-crawler/datasets/EXTRACTED_FILINGS/1018724_10K_2021_0001018724-22-000005.json"
)


# Opening JSON file
with open("datasets/EXTRACTED_FILINGS/1018724_10K_2021_0001018724-22-000005.json") as f:
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
print(sec_content)
# Closing file
f.close()
