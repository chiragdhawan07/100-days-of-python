from tkinter import *


def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = miles * 1.60934
        kilometers_result_label.config(text=f"{km:.2f}")
    except ValueError:   # handles invalid input
        kilometers_result_label.config(text="Invalid")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Input box
miles_input = Entry(width=10, justify="center")
miles_input.grid(column=1, row=0)
miles_input.insert(END, "0")

# Labels
Label(text="Miles").grid(column=2, row=0)
Label(text="is equal to").grid(column=0, row=1)
kilometers_result_label = Label(text="0", font=("Arial", 12, "bold"), fg="blue")
kilometers_result_label.grid(column=1, row=1)
Label(text="Km").grid(column=2, row=1)

# Button
Button(text="Calculate", command=miles_to_km).grid(column=1, row=2)

window.mainloop()
