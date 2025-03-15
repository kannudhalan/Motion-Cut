import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

CSV_FILE = "expenses.csv"
CATEGORY_CHOICES = ["Food", "Transportation", "Entertainment", "Utilities", "Healthcare", "Other"]

def check_file_exists():
    if not os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "description", "category", "date"])
            writer.writeheader()

def add_expense():
    """Adds a new expense to the CSV file."""
    amount = amount_entry.get()
    description = description_entry.get()
    category = category_var.get()
    date = datetime.now().strftime("%Y-%m-%d")

    if not amount or not description or category == "Select":
        messagebox.showerror("Error", "Please enter all details correctly.")
        return

    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    expense = {"amount": amount, "description": description, "category": category, "date": date}
    
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "description", "category", "date"])
        writer.writerow(expense)
    
    messagebox.showinfo("Success", "Expense added successfully!")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    category_var.set("Select")

def view_monthly_summary():
    """Shows total expenses for a given month."""
    month = month_entry.get()
    total = 0
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"].startswith(month):
                    total += float(row["amount"])
        messagebox.showinfo("Monthly Summary", f"Total expenses for {month}: ${total:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")

def view_category_summary():
    """Displays total expenses for each category."""
    category_totals = {category: 0 for category in CATEGORY_CHOICES}

    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row["category"]
                if category in category_totals:
                    category_totals[category] += float(row["amount"])
        
        summary_text = "\n".join([f"{cat}: ${total:.2f}" for cat, total in category_totals.items()])
        messagebox.showinfo("Category Summary", summary_text)
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")

app = tk.Tk()
app.title("Expense Tracker")
app.geometry("400x500")
app.configure(bg="lightblue")

tk.Label(app, text="Amount ($):", bg="black").pack(pady=5)
amount_entry = tk.Entry(app)
amount_entry.pack(pady=5)

tk.Label(app, text="Description:", bg="black").pack(pady=5)
description_entry = tk.Entry(app)
description_entry.pack(pady=5)

tk.Label(app, text="Category:", bg="black").pack(pady=5)
category_var = tk.StringVar(value="Select")
category_dropdown = tk.OptionMenu(app, category_var, *CATEGORY_CHOICES)
category_dropdown.pack(pady=5)

tk.Button(app, text="Add Expense", command=add_expense, bg="green", fg="white").pack(pady=10)

tk.Label(app, text="Enter Month (YYYY-MM) for Summary:", bg="black").pack(pady=5)
month_entry = tk.Entry(app)
month_entry.pack(pady=5)
tk.Button(app, text="View Monthly Summary", command=view_monthly_summary, bg="green", fg="white").pack(pady=10)

tk.Button(app, text="View Category Summary", command=view_category_summary, bg="green", fg="white").pack(pady=10)

check_file_exists()
app.mainloop()