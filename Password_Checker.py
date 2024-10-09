import tkinter as tk
import re

def check_password_strength(password):
    """Check the strength of the given password and provide feedback."""
    remaining = []
    if len(password) < 8:
        remaining.append("at least 8 characters")
    if not re.search(r"\d", password):
        remaining.append("at least 1 digit")
    if not re.search(r"[a-z]", password):
        remaining.append("at least 1 lowercase letter")
    if not re.search(r"[A-Z]", password):
        remaining.append("at least 1 uppercase letter")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        remaining.append("at least 1 special character (!@#$%^&*)")

    if not remaining:
        return "Strong", None
    else:
        return "Weak", remaining

def on_password_entry(event):
    """Handle real-time password entry."""
    password = password_entry.get()
    strength, missing_criteria = check_password_strength(password)

    if strength == "Strong":
        label_strength.config(text="Strong password!", fg="green")
    else:
        label_strength.config(
            text=f"Your password is weak. Missing: {', '.join(missing_criteria)}", 
            fg="red"
        )

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the password entry label and entry widget
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show=' ', width=50)
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", on_password_entry)

# Label to display password strength
label_strength = tk.Label(root, text="", fg="red")
label_strength.pack(pady=5)

# Run the application
root.mainloop()
