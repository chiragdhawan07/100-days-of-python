# 🛒 Day 47 – Amazon Price Tracker

A Python script that tracks the price of a product on Amazon and automatically sends you an email alert when the price drops below your target!  

---

## 📸 Output Screenshots

| 🖥️ Terminal Output | 📧 Email Alert |
|:------------------:|:--------------:|
| <img src="assets/images/terminal_output.png" width="420"/> | <img src="assets/images/email_output.png" width="420"/> |

---

## 🚀 How It Works

1. Fetches your Amazon product page using `requests`.  
2. Scrapes the product title and price with `BeautifulSoup`.  
3. Compares the current price with your target.  
4. Sends an email alert instantly when the price drops below your desired value.  

---

## 🛠 Skills Used

- Web Scraping (`requests`, `BeautifulSoup`)  
- HTML Parsing (`lxml`)  
- Secure Environment Variables (`python-dotenv`)  
- Email Automation (`smtplib`)  

---

## 📅 Challenge

Day 46 of my [#100DaysOfPython](https://github.com/chiragdhawan07/100-days-of-python) challenge.  
Building automation projects that make life easier one day at a time! 🐍  
