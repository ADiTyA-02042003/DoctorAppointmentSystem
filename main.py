# main.py
import tkinter as tk
from tkinter import messagebox, Toplevel, simpledialog
import database  # Import the database module

# Function to handle user login
def user_login():
    username = user_username_entry.get()
    password = user_password_entry.get()
    user_id = database.login(username, password, 'user')
    if user_id:
        welcome_page(username, "User")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Function to handle admin login
def admin_login():
    username = admin_username_entry.get()
    password = admin_password_entry.get()
    admin_id = database.login(username, password, 'admin')
    if admin_id:
        admin_page()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Function to handle password reset
def reset_password():
    def update_password():
        username = username_reset_entry.get()
        role = role_reset_entry.get().lower()
        new_password = new_password_entry.get()
        if database.forgot_password(username, role, new_password):
            messagebox.showinfo("Success", "Password updated successfully!")
        else:
            messagebox.showerror("Error", "Username not found.")

    reset_window = Toplevel(root)
    reset_window.title("Reset Password")
    tk.Label(reset_window, text="Username").grid(row=0, column=0)
    username_reset_entry = tk.Entry(reset_window)
    username_reset_entry.grid(row=0, column=1)
    tk.Label(reset_window, text="Role (user/admin)").grid(row=1, column=0)
    role_reset_entry = tk.Entry(reset_window)
    role_reset_entry.grid(row=1, column=1)
    tk.Label(reset_window, text="New Password").grid(row=2, column=0)
    new_password_entry = tk.Entry(reset_window, show='*')
    new_password_entry.grid(row=2, column=1)
    tk.Button(reset_window, text="Update Password", command=update_password).grid(row=3, column=1, pady=10)

# Function to display admin page
def admin_page():
    admin_window = Toplevel(root)
    admin_window.title("Admin Page")
    tk.Label(admin_window, text="Admin Activities").pack()

    # Button to view all users
    tk.Button(admin_window, text="View All Users", command=view_all_users).pack(pady=10)

    # Button to remove a user
    tk.Button(admin_window, text="Remove User", command=remove_user_page).pack(pady=10)

    # Button to edit a user
    tk.Button(admin_window, text="Edit User", command=edit_user_page).pack(pady=10)

# Function to display all users in a new window
def view_all_users():
    users = database.fetch_all_users()
    if not users:
        messagebox.showinfo("Info", "No users found in the database.")
        return

    # Create a new window to display the data
    data_window = Toplevel(root)
    data_window.title("All Users")

    # Create a text widget to display the data
    text_widget = tk.Text(data_window, wrap=tk.NONE)
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Insert data into the text widget
    text_widget.insert(tk.END, "ID\tUsername\tRole\n")
    text_widget.insert(tk.END, "-" * 30 + "\n")
    for user in users:
        text_widget.insert(tk.END, f"{user[0]}\t{user[1]}\t{user[3]}\n")

    # Disable editing of the text widget
    text_widget.config(state=tk.DISABLED)

# Function to remove a user
def remove_user_page():
    user_id = simpledialog.askinteger("Remove User", "Enter the ID of the user to remove:")
    if user_id:
        if database.remove_user(user_id):
            messagebox.showinfo("Success", "User removed successfully!")
        else:
            messagebox.showerror("Error", "User not found or could not be removed.")

# Function to edit a user
def edit_user_page():
    user_id = simpledialog.askinteger("Edit User", "Enter the ID of the user to edit:")
    if user_id:
        new_username = simpledialog.askstring("Edit User", "Enter new username:")
        new_password = simpledialog.askstring("Edit User", "Enter new password:", show='*')
        new_role = simpledialog.askstring("Edit User", "Enter new role (user/admin):")
        if new_username and new_password and new_role:
            if database.edit_user(user_id, new_username, new_password, new_role):
                messagebox.showinfo("Success", "User updated successfully!")
            else:
                messagebox.showerror("Error", "User not found or could not be updated.")

# Function to display registration page
def registration_page():
    def register():
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        if username and password:
            if database.register_user(username, password):
                messagebox.showinfo("Success", "Registration successful! You can now log in.")
                registration_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    registration_window = Toplevel(root)
    registration_window.title("Registration")
    tk.Label(registration_window, text="Username").grid(row=0, column=0)
    reg_username_entry = tk.Entry(registration_window)
    reg_username_entry.grid(row=0, column=1)
    tk.Label(registration_window, text="Password").grid(row=1, column=0)
    reg_password_entry = tk.Entry(registration_window, show='*')
    reg_password_entry.grid(row=1, column=1)
    tk.Button(registration_window, text="Register", command=register).grid(row=2, column=1, pady=10)

# Function to display the login options page
def login_options_page():
    login_window = Toplevel(root)
    login_window.title("Login Options")

    # User Login
    tk.Label(login_window, text="User Login").grid(row=0, column=0, pady=10)
    tk.Label(login_window, text="Username").grid(row=1, column=0)
    global user_username_entry
    user_username_entry = tk.Entry(login_window)
    user_username_entry.grid(row=1, column=1)
    tk.Label(login_window, text="Password").grid(row=2, column=0)
    global user_password_entry
    user_password_entry = tk.Entry(login_window, show='*')
    user_password_entry.grid(row=2, column=1)
    tk.Button(login_window, text="Login", command=user_login).grid(row=3, column=1, pady=5)

    # Admin Login
    tk.Label(login_window, text="Admin Login").grid(row=4, column=0, pady=10)
    tk.Label(login_window, text="Username").grid(row=5, column=0)
    global admin_username_entry
    admin_username_entry = tk.Entry(login_window)
    admin_username_entry.grid(row=5, column=1)
    tk.Label(login_window, text="Password").grid(row=6, column=0)
    global admin_password_entry
    admin_password_entry = tk.Entry(login_window, show='*')
    admin_password_entry.grid(row=6, column=1)
    tk.Button(login_window, text="Login", command=admin_login).grid(row=7, column=1, pady=5)

    # Forgot Password
    tk.Label(login_window, text="Forgot Password").grid(row=8, column=0, pady=10)
    tk.Button(login_window, text="Reset Password", command=reset_password).grid(row=9, column=1, pady=5)

# Function to display the welcome page after login
def welcome_page(username, role):
    welcome_window = Toplevel(root)
    welcome_window.title("Welcome")
    tk.Label(welcome_window, text=f"Welcome to the Doctor Appointment System, {role} {username}!").pack(pady=20)
    tk.Button(welcome_window, text="Close", command=welcome_window.destroy).pack(pady=10)

# Main application logic
def main():
    database.init_db()  # Initialize the database

    global root

    root = tk.Tk()
    root.title("Doctor Appointment System")

    # First Page: Register or Login
    tk.Label(root, text="Welcome to the Doctor Appointment System").pack(pady=20)
    tk.Button(root, text="Register", command=registration_page).pack(pady=10)
    tk.Button(root, text="Login", command=login_options_page).pack(pady=10)

    # Exit Button
    tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()