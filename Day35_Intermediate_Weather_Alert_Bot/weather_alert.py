import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# --- Load environment variables ---
load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_whatsapp = os.getenv("MY_WHATSAPP_NUMBER")
my_phone = os.getenv("MY_PHONE_NUMBER")

# --- Weather API setup ---
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 30.900965
MY_LONG = 75.857277

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,        # next 4 forecast entries (3-hour steps each)
    "units": "metric"
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# --- Weather check ---
will_rain = False
for forecast in data["list"]:
    condition_code = forecast["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

client = Client(account_sid, auth_token)

# --- Choose message ---
if will_rain:
    alert_message = "Weather Alert: Bring an umbrella ☔. It might rain today!"
else:
    alert_message = "Good news 🌤️ No rain expected today. Enjoy your day!"

print(alert_message)

# --- Send WhatsApp message ---
try:
    message = client.messages.create(
        body=alert_message,
        from_="whatsapp:+14155238886",  # Twilio WhatsApp Sandbox number
        to=my_whatsapp
    )
    print(f"WhatsApp message status: {message.status}")
except Exception as e:
    print(f"⚠️ Failed to send WhatsApp message: {e}")

# --- SMS code (disabled for now) ---
"""
try:
    message = client.messages.create(
        body=alert_message,
        from_="+12364999602",   # your Twilio SMS number
        to=my_phone
    )
    print(f"SMS status: {message.status}")
except Exception as e:
    print(f"⚠️ Failed to send SMS: {e}")
"""
