import tkinter as tk
from tkinter import messagebox
from auth import Auth  # For receptionist authentication

def login_receptionist():
    email = login_email_entry.get()
    password = login_password_entry.get()
    
    if email and password:
        token = Auth.login(email, password)  # Validate with database
        if "Invalid" in token:
            messagebox.showerror("Login Failed", token)
        else:
            messagebox.showinfo("Login Success", "Welcome Receptionist!")
            root.destroy()  # Close login window and open main app
            import gui  # Load receptionist dashboard
    else:
        messagebox.showerror("Error", "Enter Email and Password")

def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    
    # Hardcoded admin credentials
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Admin Login", "Admin Access Granted!")
        root.destroy()  # Close login window and open admin panel
        import admin_dashboard  # Load admin panel
    else:
        messagebox.showerror("Login Failed", "Incorrect Admin Credentials")

# GUI Setup
root = tk.Tk()
root.title("Login")
root.geometry("400x400")

# Receptionist Login Section
tk.Label(root, text="Receptionist Login", font=("Arial", 12)).pack(pady=5)
tk.Label(root, text="Email:").pack()
login_email_entry = tk.Entry(root)
login_email_entry.pack()

tk.Label(root, text="Password:").pack()
login_password_entry = tk.Entry(root, show="*")
login_password_entry.pack()

tk.Button(root, text="Login as Receptionist", command=login_receptionist, width=20).pack(pady=10)

# Admin Login Section
tk.Label(root, text="Admin Login", font=("Arial", 12)).pack(pady=5)
tk.Label(root, text="Username:").pack()
admin_username_entry = tk.Entry(root)
admin_username_entry.pack()

tk.Label(root, text="Password:").pack()
admin_password_entry = tk.Entry(root, show="*")
admin_password_entry.pack()

tk.Button(root, text="Login as Admin", command=admin_login, width=20).pack(pady=10)

root.mainloop()
