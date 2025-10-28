from flask import Flask, render_template, request
import requests
import smtplib
import os
from datetime import datetime
from dotenv import load_dotenv  # optional but clean for secrets

# Load environment variables (optional: create a .env file)
load_dotenv()

app = Flask(__name__)

# Fetch blog posts from API
posts = requests.get("https://api.npoint.io/4f8faa064a2861af459b").json()

# Add author & default date if missing
for post in posts:
    post["author"] = "Chirag Dhawan"
    if "date" not in post or not post["date"]:
        post["date"] = datetime.now().strftime("%B %d, %Y")

# Environment variables for security
OWN_EMAIL = os.getenv("OWN_EMAIL", "your_email@example.com")
OWN_PASSWORD = os.getenv("OWN_PASSWORD", "your_app_password_here")


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        sent = send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=sent, error=not sent)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    """Send contact form email to site owner"""
    try:
        email_message = (
            f"Subject: New Contact Message\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Message:\n{message}"
        ).encode('utf-8')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_EMAIL, msg=email_message)
        return True
    except Exception as e:
        print(f"❌ Email send failed: {str(e)}")
        return False


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = next((p for p in posts if p["id"] == index), None)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
