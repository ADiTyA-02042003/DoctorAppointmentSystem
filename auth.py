import sqlite3
import bcrypt
import jwt
import datetime

SECRET_KEY = "your_secret_key"  # Change this to a secure key

class Auth:
    @staticmethod
    def register_receptionist(name, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                           (name, email, hashed_password))
            conn.commit()
            return "Registration Successful"
        except sqlite3.IntegrityError:
            return "Email already exists!"
        finally:
            conn.close()

    @staticmethod
    def login(email, password):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, password FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user:
            user_id, name, hashed_password = user
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                token = jwt.encode({'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, 
                                   SECRET_KEY, algorithm="HS256")
                return token
            else:
                return "Invalid Password!"
        return "User Not Found!"

    @staticmethod
    def admin_login(username, password):
        ADMIN_CREDENTIALS = {"username": "admin", "password": "admin123"}
        if username == ADMIN_CREDENTIALS["username"] and password == ADMIN_CREDENTIALS["password"]:
            token = jwt.encode({'role': 'admin', 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)}, 
                               SECRET_KEY, algorithm="HS256")
            return token
        return "Invalid Admin Credentials"
