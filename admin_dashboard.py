import tkinter as tk
from tkinter import messagebox
import sqlite3

def fetch_doctors():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()

    doctor_list.delete(0, tk.END)  # Clear list before updating
    for doctor in doctors:
        doctor_list.insert(tk.END, 
            f"ID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}, Degree: {doctor[4]}, Availability: {doctor[3]}")

def fetch_receptionists():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    receptionists = cursor.fetchall()
    conn.close()
    
    receptionist_list.delete(0, tk.END)
    for r in receptionists:
        receptionist_list.insert(tk.END, f"ID: {r[0]}, Name: {r[1]}, Email: {r[2]}")

def add_doctor():
    name = doctor_name_entry.get()
    specialization = doctor_specialization_entry.get()
    degree = doctor_degree_entry.get()

    if name and specialization and degree:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialization, degree) VALUES (?, ?, ?)", 
                       (name, specialization, degree))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Doctor added successfully!")
        fetch_doctors()
    else:
        messagebox.showerror("Error", "Please enter all details")


def remove_doctor():
    try:
        selected = doctor_list.get(doctor_list.curselection())
        doctor_id = selected.split(",")[0].split(": ")[1]  # Extract ID
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM doctors WHERE id=?", (doctor_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Doctor removed successfully!")
        fetch_doctors()
    except:
        messagebox.showerror("Error", "Select a doctor to remove")

def update_availability():
    try:
        selected = doctor_list.get(doctor_list.curselection())
        doctor_id = selected.split(",")[0].split(": ")[1]  # Extract ID
        new_availability = "UNAVAILABLE" if "AVAILABLE" in selected else "AVAILABLE"

        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE doctors SET availability=? WHERE id=?", (new_availability, doctor_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Doctor availability updated to {new_availability}")
        fetch_doctors()
    except:
        messagebox.showerror("Error", "Select a doctor to update availability")

def add_receptionist():
    name = receptionist_name_entry.get()
    email = receptionist_email_entry.get()
    password = receptionist_password_entry.get()

    if name and email and password:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Receptionist added successfully!")
        fetch_receptionists()
    else:
        messagebox.showerror("Error", "Please enter all details")

def remove_receptionist():
    try:
        selected = receptionist_list.get(receptionist_list.curselection())
        receptionist_id = selected.split(",")[0].split(": ")[1]  # Extract ID
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (receptionist_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Receptionist removed successfully!")
        fetch_receptionists()
    except:
        messagebox.showerror("Error", "Select a receptionist to remove")

# GUI Setup
root = tk.Tk()
root.title("Admin Dashboard")
root.geometry("500x600")

# Doctor Management
tk.Label(root, text="Doctors", font=("Arial", 14)).pack()
doctor_list = tk.Listbox(root, width=80)
doctor_list.pack()

tk.Button(root, text="Fetch Doctors", command=fetch_doctors).pack()
tk.Button(root, text="Remove Doctor", command=remove_doctor).pack()
tk.Button(root, text="Update Availability", command=update_availability).pack()

tk.Label(root, text="Doctor Name:").pack()
doctor_name_entry = tk.Entry(root)
doctor_name_entry.pack()

tk.Label(root, text="Degree:").pack()
doctor_degree_entry = tk.Entry(root)
doctor_degree_entry.pack()


tk.Label(root, text="Specialization:").pack()
doctor_specialization_entry = tk.Entry(root)
doctor_specialization_entry.pack()

tk.Button(root, text="Add Doctor", command=add_doctor).pack()

# Receptionist Management
tk.Label(root, text="Receptionists", font=("Arial", 14)).pack()
receptionist_list = tk.Listbox(root, width=60)
receptionist_list.pack()

tk.Button(root, text="Fetch Receptionists", command=fetch_receptionists).pack()
tk.Button(root, text="Remove Receptionist", command=remove_receptionist).pack()

tk.Label(root, text="Receptionist Name:").pack()
receptionist_name_entry = tk.Entry(root)
receptionist_name_entry.pack()

tk.Label(root, text="Email:").pack()
receptionist_email_entry = tk.Entry(root)
receptionist_email_entry.pack()

tk.Label(root, text="Password:").pack()
receptionist_password_entry = tk.Entry(root, show="*")
receptionist_password_entry.pack()

tk.Button(root, text="Add Receptionist", command=add_receptionist).pack()

root.mainloop()
