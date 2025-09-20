import requests
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# Change by you location both latitude and longitude. Currently Location (Ludhiana, Punjab)
MY_LAT = 30.900965 
MY_LONG = 75.857277

# Fill in your email credentials
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"   # create a Gmail App Password
TO_EMAIL = "receiver_email@gmail.com"

# Get sunrise & sunset data
params = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
data = response.json()["results"]

# Convert UTC → IST
def to_ist(utc_string):
    utc_time = datetime.fromisoformat(utc_string.replace("Z", "+00:00"))
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    return ist_time.strftime("%I:%M:%S %p")

sunrise = to_ist(data["sunrise"])
sunset = to_ist(data["sunset"])

message = f"Sunrise in Ludhiana 🌅: {sunrise}\nSunset in Ludhiana 🌇: {sunset}"
print(message)

# Send email
try:
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = Header("Ludhiana Sunrise & Sunset Times ☀️🌙", "utf-8")
    msg["From"] = MY_EMAIL
    msg["To"] = TO_EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, TO_EMAIL, msg.as_string())

    print("Email sent successfully!")
except Exception as e:
    print("Email failed:", e)
