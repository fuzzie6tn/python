import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "26W0BL08FVG75CFF"
NEWS_API_KEY = "775f69984aff4121b21d5afc69b125d6"

TWILIO_SID = "AC374d00f3d9b65735e032c4c4f99c6e81"


# Get yesterday's stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()

# Handle missing key
time_series = data.get("Time Series (Daily)")
if not time_series:
    print("Error: 'Time Series (Daily)' key missing in response.")
    print(data)
    exit()

data_list = [value for (key, value) in time_series.items()]
yestarday_data = data_list[0]
yestarday_closing_price = yestarday_data["4. close"]
print("Yesterday's closing price:", yestarday_closing_price)

before_closing_price = data_list[1]
day_before_yesterday_closing_price = before_closing_price["4. close"]
print("Day before yesterday's closing price:", day_before_yesterday_closing_price)

# Calculate difference
difference = float(yestarday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"

# Calculate percentage difference
percentage_diff = round((difference / float(yestarday_closing_price)) * 100, 2)
print("Percentage difference:", percentage_diff)

# Get news if percentage difference exceeds 5%
if abs(percentage_diff) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get('articles', [])
    three_articles = articles[:3]

    # Format articles
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percentage_diff}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_pass)

    for article in formatted_articles:
        try:
            message = client.messages.create(
                body=article,
                from_="+17752788860",  # Twilio number
                to="",   # Your phone number
            )
            print(f"Message sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")
