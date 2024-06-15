import tkinter as tk
from tkinter import messagebox
import math

def prime_checker(number):
    if number <= 1:
        return "It's not a prime number."
    n = math.isqrt(number)
    factor = 0
    for i in range(1, n + 1):
        if number % i == 0:
            factor += 1
    if factor == 1:
        return "It's a prime number."
    else:
        return "It's not a prime number."

def check_prime():
    try:
        number = int(entry.get())
        result = prime_checker(number)
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

# Set up the main application window
root = tk.Tk()
root.title("Prime Number Checker")

# Create and place the input field and labels
tk.Label(root, text="Enter a number:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create and place the check button
check_button = tk.Button(root, text="Check", command=check_prime)
check_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
