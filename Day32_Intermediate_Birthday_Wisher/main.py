from datetime import datetime
import pandas as pd
import smtplib
import random

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "password"
MY_SMTP = "smtp.gmail.com"

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Load CSV data
data = pd.read_csv("birthdays.csv")

# Create dictionary with (month, day) as key
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

# Check if today matches a birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Pick a random template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        letter_contents = letter_file.read()
        letter_contents = letter_contents.replace("[NAME]", birthday_person["name"])

    # Send email
    with smtplib.SMTP(MY_SMTP, 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_contents}"
        )
    print("✅ Email sent successfully.")
else:
    print("📅 No birthdays today.")
