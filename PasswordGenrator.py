import random
import tkinter as tk
from tkinter import messagebox, ttk

# Function to generate the password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    try:
        nr_letters = int(entry_letters.get())
        nr_symbols = int(entry_symbols.get())
        nr_numbers = int(entry_numbers.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    result_label.config(text=f"Your password is: {password}")

# Set up the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Create a frame for input fields
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.pack(pady=20)

# Labels and Entry widgets for input
ttk.Label(input_frame, text="How many letters would you like in your password?", font=("Arial", 10)).grid(column=0, row=0, sticky="W")
entry_letters = ttk.Entry(input_frame, width=5)
entry_letters.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(input_frame, text="How many symbols would you like?", font=("Arial", 10)).grid(column=0, row=1, sticky="W")
entry_symbols = ttk.Entry(input_frame, width=5)
entry_symbols.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(input_frame, text="How many numbers would you like?", font=("Arial", 10)).grid(column=0, row=2, sticky="W")
entry_numbers = ttk.Entry(input_frame, width=5)
entry_numbers.grid(column=1, row=2, padx=10, pady=5)

# Button to generate the password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Configure the grid
for child in input_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the application
root.mainloop()
