import requests
import pandas

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "26W0BL08FVG75CFF"

# TODO 1. get yesterday's stocking price
# alphavantage is a stock market API
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params) # fetching from the stock endpoint
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()] # list comprehension
yestarday_data = data_list[0]
yestarday_closing_price = yestarday_data["4. close"]
print(yestarday_closing_price)

# TODO 2. Get the day before yesterday's closing stock price
before_closing_price = data_list[1]
day_before_yesterday = before_closing_price["4. close"]
print(day_before_yesterday)