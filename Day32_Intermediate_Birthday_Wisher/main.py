from datetime import datetime
import pandas as pd
import smtplib
from email.message import EmailMessage
import random

MY_EMAIL = "your-email@gmail.com"
MY_PASSWORD = "password"
MY_SMTP = "smtp.gmail.com"

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Load CSV data
data = pd.read_csv("birthdays.csv")

# Create dictionary with (month, day) as key
birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

# Check if today matches a birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Pick a random template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r", encoding="utf-8") as letter_file:
        letter_contents = letter_file.read().replace("[NAME]", birthday_person["name"])

    # Create email
    msg = EmailMessage()
    msg["From"] = MY_EMAIL
    msg["To"] = birthday_person["email"]
    msg["Subject"] = "Happy Birthday!"
    msg.set_content(letter_contents)

    # Send email
    with smtplib.SMTP(MY_SMTP, 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(msg)

    print("✅ Email sent successfully.")
else:
    print("📅 No birthdays today.")
