from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# ---------------------------- APP CONFIG ---------------------------- #
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# ---------------------------- DATABASE ---------------------------- #
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# ---------------------------- LOGIN MANAGER ---------------------------- #
login_manager = LoginManager()
login_manager.login_view = "login"      # Redirect unauthorized users to login page
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# ---------------------------- USER TABLE ---------------------------- #
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)


with app.app_context():
    db.create_all()


# ---------------------------- ROUTES ---------------------------- #
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


# ---------------------------- REGISTER ---------------------------- #
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        email = request.form.get("email")

        # Check if user already exists
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if user:
            flash("You've already signed up with that email. Please log in instead.")
            return redirect(url_for("login"))

        # Create user
        hashed_password = generate_password_hash(
            request.form.get("password"),
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            email=email,
            password=hashed_password,
            name=request.form.get("name")
        )

        db.session.add(new_user)
        db.session.commit()

        # Log them in immediately
        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


# ---------------------------- LOGIN ---------------------------- #
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Look for user
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist. Please try again.")
            return redirect(url_for("login"))

        if not check_password_hash(user.password, password):
            flash("Password incorrect. Please try again.")
            return redirect(url_for("login"))

        # Login successful
        login_user(user)
        return redirect(url_for("secrets"))

    return render_template("login.html", logged_in=current_user.is_authenticated)


# ---------------------------- PROTECTED ROUTE ---------------------------- #
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


# ---------------------------- LOGOUT ---------------------------- #
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# ---------------------------- FILE DOWNLOAD ---------------------------- #
@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static/files",
        path="cheat_sheet.pdf",
        as_attachment=True
    )


# ---------------------------- RUN APP ---------------------------- #
if __name__ == "__main__":
    app.run(debug=True)
