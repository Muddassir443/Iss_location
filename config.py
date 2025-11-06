import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWZ_API = "e0cdd19b403643008f49431b1ec8d865"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "SPN03WIADQCMYH57"

stock_parameter = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME
}
response = requests.get(url=STOCK_ENDPOINT)