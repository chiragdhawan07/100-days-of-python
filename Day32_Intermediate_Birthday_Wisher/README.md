# 🎂 Day 32 – Intermediate Birthday Wisher

A Python automation project that reads birthdays from a CSV file and automatically sends personalized birthday wishes via **email**.  

---

## 🚀 How It Works
1. Save your friends’ names, emails, and birthdays in `birthdays.csv`.
2. Create personalized letter templates with `[NAME]` placeholder in `letter_templates/`.
3. On each run, the script:
   - Checks today’s date.
   - Finds matching birthdays in the CSV.
   - Replaces `[NAME]` with the person’s name in a random letter.
   - Sends the email using **Gmail SMTP**.

---

## 🛠 Skills Used
- `smtplib` for sending emails securely
- `pandas` for CSV handling
- `datetime` for working with dates
- Randomized template selection

---

## 📦 Requirements
- Python 3.10+
- Gmail account with **App Passwords** enabled
- Libraries:
```bash
  pip install pandas
```

---

## 🌍 Running Online (PythonAnywhere)
You can run this project on [PythonAnywhere]([url](https://www.pythonanywhere.com/))
1. Upload your project files (`main.py`, `birthdays.csv`, `letter_templates`).
2. Go to the Tasks tab and schedule `python3.10 main.py` to run daily.
3. Emails will be sent automatically on birthdays 🎉

---

📅 Challenge

This project is part of Day 32 of the 100 Days of Python challenge.
Check out the full repo here 👉 [100-days-of-python]([url](https://github.com/chiragdhawan07/100-days-of-python))
