Start Running the program from main_gui.py file 
admin username is "admin"
admin password is "admin123"







To run the fastAPI file first execute " python fastAPI.py" in terminal

then execute "uvicorn fastAPI:app --reload"





How to run in Postman??

# ----------------------- Doctor Endpoints -----------------------

1. Add Doctor
URL: http://127.0.0.1:8000/add_doctors
Method: POST
Payload (JSON):
json
Copy
Edit
{
  "name": "Dr. John Doe",
  "specialization": "Cardiology",
  "degree": "MBBS, MD",
  "email": "johndoe@example.com"
}
Response:
json
Copy
Edit
{ "message": "Doctor added successfully" }




2. View All Doctors
URL: http://127.0.0.1:8000/view_doctors?page=1&limit=5
Method: GET
Response:
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Dr. John Doe",
    "specialization": "Cardiology",
    "degree": "MBBS, MD",
    "email": "johndoe@example.com"
  }
]



3. Get Doctor by ID
URL: http://127.0.0.1:8000/get_doctor_by_id_doctors/{doctor_id}
Method: GET
Example: http://127.0.0.1:8000/get_doctor_by_id_doctors/1
Response:
json
Copy
Edit
{
  "id": 1,
  "name": "Dr. John Doe",
  "specialization": "Cardiology",
  "degree": "MBBS, MD",
  "email": "johndoe@example.com"
}



4. Update Doctor
URL: http://127.0.0.1:8000/update_doctors/{doctor_id}
Method: PUT
Example: http://127.0.0.1:8000/update_doctors/1
Payload (JSON):
json
Copy
Edit
{
  "name": "Dr. John Smith",
  "specialization": "Neurology",
  "degree": "MBBS, MD",
  "email": "johnsmith@example.com"
}
Response:
json
Copy
Edit
{ "message": "Doctor updated successfully" }



5. Delete Doctor
URL: http://127.0.0.1:8000/delete_doctors/{doctor_id}
Method: DELETE
Example: http://127.0.0.1:8000/delete_doctors/1
Response:
json
Copy
Edit
{ "message": "Doctor deleted successfully" }





# ----------------------- Patients Endpoints -----------------------
1. Add Patient
URL: http://127.0.0.1:8000/add_patients
Method: POST
Payload (JSON):
json
Copy
Edit
{
  "name": "Jane Doe",
  "age": 29,
  "phone": "9876543210",
  "email": "janedoe@example.com"
}
Response:
json
Copy
Edit
{ "message": "Patient registered successfully" }



2. View All Patients
URL: http://127.0.0.1:8000/get_patients
Method: GET
Response:
json
Copy
Edit
[
  {
    "id": 1,
    "name": "Jane Doe",
    "age": 29,
    "phone": "9876543210",
    "email": "janedoe@example.com"
  }
]


# ----------------------- Appointment Endpoints -----------------------
1. Book Appointment
URL: http://127.0.0.1:8000/book_appointment
Method: POST
Payload (JSON):
json
Copy
Edit
{
  "patient_id": 1,
  "doctor_id": 1,
  "date": "2024-02-29",
  "time": "10:30 AM",
  "illness": "Fever"
}
Response:
json
Copy
Edit
{ "message": "Appointment booked successfully" }


2. Update Appointment
URL: http://127.0.0.1:8000/update_appointments
Method: PUT
Payload (JSON):
json
Copy
Edit
{
  "appt_id": 1,
  "new_date": "2024-03-01",
  "new_time": "11:00 AM"
}
Response:
json
Copy
Edit
{ "message": "Appointment updated successfully" }
3. Cancel Appointment
URL: http://127.0.0.1:8000/cancel_appointments/{appt_id}
Method: DELETE
Example: http://127.0.0.1:8000/cancel_appointments/1
Response:
json
Copy
Edit
{ "message": "Appointment canceled successfully" }




