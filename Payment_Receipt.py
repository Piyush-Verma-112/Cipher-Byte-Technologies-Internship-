import tkinter as tk
from tkinter import messagebox
import datetime

# Function to generate receipt
def generate_receipt():
    customer_name = customer_name_entry.get()
    amount_paid = amount_paid_entry.get()
    payment_method = payment_method_entry.get()

    if not customer_name or not amount_paid or not payment_method:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        amount_paid = float(amount_paid)
    except ValueError:
        messagebox.showerror("Error", "Amount paid must be a number.")
        return
    
    receipt = f"======= Payment Receipt =======\n"
    receipt += f"Customer Name: {customer_name}\n"
    receipt += f"Amount Paid: ${amount_paid:.2f}\n"
    receipt += f"Payment Method: {payment_method}\n"
    receipt += f"Date: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}\n"
    receipt += f"=============================="
    
    receipt_text.delete(1.0, tk.END)  # Clear previous receipt
    receipt_text.insert(tk.END, receipt)

# Creating the main window
root = tk.Tk()
root.title("Payment Receipt Generator")

# Customer Name
customer_name_label = tk.Label(root, text="Customer Name:")
customer_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Amount Paid
amount_paid_label = tk.Label(root, text="Amount Paid ($):")
amount_paid_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
amount_paid_entry = tk.Entry(root)
amount_paid_entry.grid(row=1, column=1, padx=10, pady=10)

# Payment Method
payment_method_label = tk.Label(root, text="Payment Method:")
payment_method_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
payment_method_entry = tk.Entry(root)
payment_method_entry.grid(row=2, column=1, padx=10, pady=10)

# Generate Receipt Button
generate_button = tk.Button(root, text="Generate Receipt", command=generate_receipt)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Receipt Display Area
receipt_text = tk.Text(root, height=10, width=50, wrap=tk.WORD)
receipt_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Running the main event loop
root.mainloop()
