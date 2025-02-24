import sqlite3

class Doctor:
    def __init__(self, name, specialization, degree):
        self.name = name
        self.specialization = specialization
        self.degree = degree

    def save_to_db(self):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialization, degree) VALUES (?, ?, ?)", 
                       (self.name, self.specialization, self.degree))
        conn.commit()
        conn.close()


class Patient:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def save_to_db(self):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, age, phone) VALUES (?, ?, ?)", (self.name, self.age, self.phone))
        conn.commit()
        conn.close()

class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def save_to_db(self):
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (?, ?, ?, ?)", 
                       (self.patient_id, self.doctor_id, self.date, self.time))
        conn.commit()
        conn.close()
