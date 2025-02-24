import tkinter as tk
import subprocess

def open_register():
    subprocess.Popen(["python", "register_gui.py"])  # Opens Registration Page

def open_login():
    subprocess.Popen(["python", "login_gui.py"])  # Opens Login Page

# GUI Setup
root = tk.Tk()
root.title("Doctor Appointment System")
root.geometry("400x300")

tk.Label(root, text="Welcome to Doctor Appointment System", font=("Arial", 14)).pack(pady=20)

register_button = tk.Button(root, text="Register Receptionist", command=open_register, width=20, height=2)
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login (Receptionist/Admin)", command=open_login, width=20, height=2)
login_button.pack(pady=10)

root.mainloop()
