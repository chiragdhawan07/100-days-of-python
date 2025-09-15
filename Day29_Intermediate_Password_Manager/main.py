from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please fill out all fields.")
        return
    
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nSave?"
    )
    
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Saved", message="Password saved successfully!")

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

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

# Align columns properly
screen.grid_columnconfigure(1, weight=1)

screen.mainloop()
