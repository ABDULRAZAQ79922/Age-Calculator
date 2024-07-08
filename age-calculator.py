import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk

my_window = tk.Tk()
my_window.title("Age Calculator")
my_window.geometry("800x400")
my_window.configure(bg="#f0f0f0")

my_bg_image = Image.open("background.jpeg")
my_bg_image = my_bg_image.resize((500, 400), Image.ANTIALIAS)
my_bg_image_tk = ImageTk.PhotoImage(my_bg_image)

my_bg_label = tk.Label(my_window, image=my_bg_image_tk)
my_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

my_title_label = tk.Label(my_window, text="Age Calculator", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
my_title_label.pack(pady=20)

my_dob_label = tk.Label(my_window, text="Enter your Date of Birth (YYYY-MM-DD):", font=("Helvetica", 12), bg="#f0f0f0")
my_dob_label.pack(pady=10)
my_dob_entry = ttk.Entry(my_window, font=("Helvetica", 12))
my_dob_entry.pack(pady=10)

my_result_label = tk.Label(my_window, text="", font=("Helvetica", 14), bg="#f0f0f0")
my_result_label.pack(pady=20)

def my_calculate_age():
    dob = my_dob_entry.get()
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        my_result_label.config(text=f"You are {age} years old!", fg="green")
    except ValueError:
        my_result_label.config(text="Please enter a valid date in YYYY-MM-DD format.", fg="red")

my_calculate_button = ttk.Button(my_window, text="Calculate Age", command=my_calculate_age)
my_calculate_button.pack(pady=10)

def my_on_enter(e):
    my_calculate_button.config(style="TButton")
    my_window.after(10, lambda: my_calculate_button.config(style="Hover.TButton"))

def my_on_leave(e):
    my_calculate_button.config(style="TButton")
    my_window.after(10, lambda: my_calculate_button.config(style="TButton"))

my_calculate_button.bind("<Enter>", my_on_enter)
my_calculate_button.bind("<Leave>", my_on_leave)

my_style = ttk.Style()
my_style.configure("TButton", font=("Helvetica", 12), padding=10)
my_style.configure("Hover.TButton", font=("Helvetica", 12, "bold"), padding=10, background="#ffaaaa")

my_window.mainloop()
