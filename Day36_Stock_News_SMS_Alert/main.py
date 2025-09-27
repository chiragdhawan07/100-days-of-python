import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# ================= CONFIG ================= #
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")   # your number
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Twilio number

# Step 1: Get Stock Data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json().get("Time Series (Daily)")

if not data:
    print("⚠️ Error: Stock data not available. Check API key/limits.")
    exit()

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Calculate Difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((abs(difference) / yesterday_closing_price) * 100, 2)

print(f"Yesterday: {yesterday_closing_price}")
print(f"Day before: {day_before_yesterday_closing_price}")
print(f"Change: {up_down}{diff_percent}%")

# Step 2: If big change, fetch News
if diff_percent > 1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    if not articles:
        print("⚠️ No news articles found.")
        exit()

    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"📰 Headline: {article['title']}\n"
        f"📝 Brief: {article['description']}"
        for article in three_articles
    ]

    for article in formatted_articles:
        print(article)

    # Step 3: Send SMS via Twilio
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_=TWILIO_PHONE_NUMBER,
                to=MY_PHONE_NUMBER
            )
            print(f"✅ SMS sent: {message.sid}")
    except Exception as e:
        print(f"⚠️ SMS sending failed: {e}")
else:
    print("📉 Change not big enough, no news fetched.")
