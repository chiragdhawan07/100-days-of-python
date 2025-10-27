from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

# Fetch posts from API
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

# Add author and date to each post
for post in posts:
    post["author"] = "Chirag Dhawan"
    # Add a default date if not present in API
    if "date" not in post or not post["date"]:
        post["date"] = datetime.now().strftime("%B %d, %Y")  # e.g. October 27, 2025

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
