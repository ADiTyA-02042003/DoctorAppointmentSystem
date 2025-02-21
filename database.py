# database.py
import sqlite3
from hashlib import sha256

# Initialize the database
def init_db():
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    
    # Create users table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  role TEXT NOT NULL)''')
    
    # Add a default admin account if it doesn't exist
    admin_username = "admin"
    admin_password = sha256("admin123".encode()).hexdigest()  # Hash the default password
    c.execute("SELECT * FROM users WHERE username = ? AND role = 'admin'", (admin_username,))
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  (admin_username, admin_password, 'admin'))
    
    conn.commit()
    conn.close()

# Function to register a new user
def register_user(username, password, role='user'):
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    hashed_password = sha256(password.encode()).hexdigest()
    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  (username, hashed_password, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists
    finally:
        conn.close()

# Function to handle login
def login(username, password, role):
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    hashed_password = sha256(password.encode()).hexdigest()
    c.execute("SELECT id FROM users WHERE username = ? AND password = ? AND role = ?",
              (username, hashed_password, role))
    user = c.fetchone()
    conn.close()
    return user[0] if user else None

# Function to handle password reset
def forgot_password(username, role, new_password):
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    hashed_password = sha256(new_password.encode()).hexdigest()
    c.execute("UPDATE users SET password = ? WHERE username = ? AND role = ?",
              (hashed_password, username, role))
    conn.commit()
    rows_updated = c.rowcount
    conn.close()
    return rows_updated > 0

# Function to fetch all users from the database
def fetch_all_users():
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

# Function to remove a user by ID
def remove_user(user_id):
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    rows_deleted = c.rowcount
    conn.close()
    return rows_deleted > 0

# Function to edit a user's details
def edit_user(user_id, new_username, new_password, new_role):
    conn = sqlite3.connect('appointment_system.db')
    c = conn.cursor()
    hashed_password = sha256(new_password.encode()).hexdigest()
    c.execute("UPDATE users SET username = ?, password = ?, role = ? WHERE id = ?",
              (new_username, hashed_password, new_role, user_id))
    conn.commit()
    rows_updated = c.rowcount
    conn.close()
    return rows_updated > 0