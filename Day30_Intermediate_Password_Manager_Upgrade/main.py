from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ---------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get().strip().capitalize()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please fill out all fields.")
        return
    
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nSave?"
    )
    
    if is_ok:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Saved", message="Password saved successfully!")

# ---------------------------- SEARCH PASSWORD ------------------------------ #
def find_password():
    website = website_entry.get().strip().capitalize()
    if not website:
        messagebox.showwarning(title="Oops", message="Please enter a website to search.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
        return
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is corrupted.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showwarning(title="Not Found", message=f"No details for '{website}' exist.")

# ---------------------------- UI SETUP ------------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

# Logo
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website
Label(text="Website:").grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

Button(text="Search", width=13, command=find_password).grid(column=2, row=1)

# Email/Username
Label(text="Email/Username:").grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# Password + Generate button
Label(text="Password:").grid(column=0, row=3)
password_frame = Frame(screen)
password_frame.grid(column=1, row=3, columnspan=2, sticky="ew")

password_entry = Entry(password_frame)
password_entry.pack(side=LEFT, fill=X, expand=True)

Button(password_frame, text="Generate Password", command=generate_password).pack(side=LEFT, padx=5)

# Add button
Button(text="Add", width=36, command=add_password).grid(column=1, row=4, columnspan=2)

# Align columns 
screen.grid_columnconfigure(1, weight=1)

screen.mainloop()
