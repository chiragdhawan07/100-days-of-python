import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Amazon Product URL
URL = "https://www.amazon.in/dp/B0FQFJBBVY?_encoding=UTF8&psc=1&ref=cm_sw_r_cp_ud_dp_TBHCVEZFEAM9EE9HHK3P"

# Target price (set to your desired alert value)
TARGET_PRICE = 25910

# Email credentials from .env
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
RECIEVER_EMAIL = os.getenv("RECIEVER_EMAIL")

# Request headers 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/141.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Connection": "keep-alive",
}

time.sleep(2)

# Fetch page
response = requests.get(URL, headers=headers)
print("HTTP Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print("🔍 Page title:", soup.title)

# Extract product title
title_tag = soup.select_one("#productTitle, span.a-size-large.product-title-word-break")
if not title_tag:
    raise Exception("❌ Could not find product title — Amazon may have blocked the request.")
product_title = title_tag.get_text(strip=True)

# Extract product price
price_tag = soup.select_one(".a-price .a-offscreen, span.a-price-whole")
if not price_tag:
    raise Exception("❌ Could not find product price — page structure may have changed.")
price_text = price_tag.get_text().replace("₹", "").replace(",", "").strip()

try:
    price = float(price_text.split(".")[0])
except ValueError:
    raise Exception(f"❌ Could not convert price: {price_text}")

# Show results
print(f"✅ Product: {product_title}")
print(f"💰 Current Price: ₹{price}")

# --- Email Alert Section ---
if price < TARGET_PRICE:
    print("✅ Price dropped below your target! Sending email...")
    subject = f"Price Drop Alert! {product_title} now ₹{price}"
    body = f"{product_title}\nCurrent price: ₹{price}\nBuy now: {URL}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIEVER_EMAIL,
                msg=message.encode("utf-8")
            )
        print("📩 Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)
else:
    print("⏳ Price still above your target.")
