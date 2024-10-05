import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    """Check the strength of the given password."""
    length_check = len(password) >= 8
    digit_check = re.search(r"\d", password) is not None
    lower_check = re.search(r"[a-z]", password) is not None
    upper_check = re.search(r"[A-Z]", password) is not None
    special_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    if length_check and digit_check and lower_check and upper_check and special_check:
        return "Strong"
    elif length_check and (digit_check or lower_check or upper_check):
        return "Moderate"
    else:
        return "Weak"

def on_check_password():
    """Handle the password check button click."""
    password = password_entry.get()
    strength = check_password_strength(password)
   ## messagebox.showinfo("Password Strength", f"Your password is: {strength}")
    label_strength.config(text=strength)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the password entry label and entry widget
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show='', width=30)
password_entry.pack(pady=10)

# Create and place the check button
check_button = tk.Button(root, text="Check Password Strength", command=on_check_password)
check_button.pack(pady=20)

label_strength = tk.Label(root, text="", fg="red")
label_strength.pack(pady=5)
# Run the application
root.mainloop()
