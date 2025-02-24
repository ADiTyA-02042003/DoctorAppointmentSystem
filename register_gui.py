import tkinter as tk
from tkinter import messagebox
from auth import Auth

def register():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if name and email and password:
        result = Auth.register_receptionist(name, email, password)
        messagebox.showinfo("Registration", result)
    else:
        messagebox.showerror("Error", "All fields are required")

# GUI Setup
root = tk.Tk()
root.title("Register Receptionist")
root.geometry("400x300")

tk.Label(root, text="Receptionist Registration", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Register", command=register, width=15).pack(pady=10)

root.mainloop()
