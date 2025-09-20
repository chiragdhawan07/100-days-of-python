# 🌅 Day 33 – Sunrise & Sunset Email Notifier  

This project fetches **sunrise and sunset times** for Ludhiana (or any city by latitude & longitude) using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).  
It then converts the times from **UTC to IST**, displays them in the terminal, and sends them as a neat **email report** using Python’s `smtplib`.  

---

## 🚀 Features  
- 🌍 Fetches real sunrise & sunset times from the API  
- 🕒 Converts UTC → IST automatically  
- 💻 Displays the results in the terminal  
- 📧 Sends an email report with the times  
- 🔑 Uses **Gmail App Passwords** for safe login  

---

## 🛠 Skills Practiced  
- Python basics & API integration (`requests`)  
- Date & time manipulation with `datetime`  
- Sending emails via `smtplib` and `MIMEText`  
- Using credentials safely with placeholders  
- Automating useful real-world tasks  

---

## 📸 Screenshots  

### ✅ Terminal Output  
![Terminal Screenshot](screenshot_terminal.png)  

### 📧 Email Received  
![Email Screenshot](screenshot_email.png)  

---

## ⚙️ Setup & Usage  

1. **Clone this repo**  
```bash
git clone https://github.com/your-username/day33-sunrise-sunset-email.git
cd day33-sunrise-sunset-email
```
2. **Install dependencies**
```bash
pip install requests
```
3. **Fill in your details inside `main.py`:**
```bash
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"   # create from Google Account > Security > App Passwords
TO_EMAIL = "receiver_email@gmail.com"
```
⚠️ Important: Use a Gmail App Password instead of your normal password.
4. **Run the script**
```bash
python main.py
```
5. **Check your terminal and inbox 📥**

---

## 📅 Challenge  
This project is part of my **100 Days of Python** challenge 🎯  

👉 Day 33 of 100  
🔗 [Main Challenge Repo](https://github.com/chiragdhawan07/100-days-of-python)  
