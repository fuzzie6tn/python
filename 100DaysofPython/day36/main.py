import requests
import pandas

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "26W0BL08FVG75CFF"
NEWS_API_KEY = "775f69984aff4121b21d5afc69b125d6"

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
day_before_yesterday_closing_price = before_closing_price["4. close"]
print(day_before_yesterday_closing_price)

# TODO 3. Find the positive difference btw 1 and 2
difference = abs(float(yestarday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# TODO 4. Work out the percentage difference in price btw closing price yesterday and closing price the day before yesterday
percentage_diff = (difference / float(yestarday_closing_price)) * 100
print(percentage_diff)

# TODO 5 6. if the percentage  is greater  than 5  then print("GET NEWS")
news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
if percentage_diff > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    print(articles)

# TODO 7. Use python slice operator to create a list that contains the first 3 articles

    