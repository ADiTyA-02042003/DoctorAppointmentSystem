import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Alter the table if it already exists (for existing databases)
cursor.execute("PRAGMA table_info(doctors)")
columns = [col[1] for col in cursor.fetchall()]
if "degree" not in columns:
    cursor.execute("ALTER TABLE doctors ADD COLUMN degree TEXT")

# Create Doctors table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT NOT NULL,
                    degree TEXT NOT NULL,
                    availability TEXT DEFAULT 'AVAILABLE'
                )''')

# Create Patients table
cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    phone TEXT NOT NULL
                )''')

# Create Appointments table
cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER,
                    doctor_id INTEGER,
                    date TEXT,
                    time TEXT,
                    FOREIGN KEY (patient_id) REFERENCES patients(id),
                    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
                )''')

# Create Users table (Receptionists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database setup complete.")
