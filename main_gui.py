import tkinter as tk
import subprocess
import threading
import uvicorn
from fastapi import FastAPI
import os
import signal
import sys

# FastAPI Setup
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Doctor Appointment System API"}

@app.get("/register")
def register():
    return {"message": "Registration endpoint"}

@app.get("/login")
def login():
    return {"message": "Login endpoint"}

def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Tkinter Functions
def open_register():
    subprocess.Popen(["python", "register_gui.py"])  # Opens Registration Page

def open_login():
    subprocess.Popen(["python", "login_gui.py"])  # Opens Login Page

# Function to stop FastAPI server
def stop_fastapi():
    print("Stopping FastAPI server...")
    os.kill(os.getpid(), signal.SIGINT)  # Send a keyboard interrupt signal to stop Uvicorn

# GUI Setup
root = tk.Tk()
root.title("Doctor Appointment System")
root.geometry("400x300")

tk.Label(root, text="Welcome to Doctor Appointment System", font=("Arial", 14)).pack(pady=20)

register_button = tk.Button(root, text="Register Receptionist", command=open_register, width=20, height=2)
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login (Receptionist/Admin)", command=open_login, width=20, height=2)
login_button.pack(pady=10)

# Start FastAPI in a separate thread
fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
fastapi_thread.start()

# Ensure FastAPI server stops when the Tkinter window is closed
def on_closing():
    stop_fastapi()  # Stop FastAPI server
    root.destroy()  # Close the Tkinter window
    sys.exit()      # Exit the program

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
