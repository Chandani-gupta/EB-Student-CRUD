EB Student CRUD API

A Student Management REST API developed using Python and FastAPI with an SQLite database.

Features

- Create a new student
- View all students
- View a student by ID
- Update student details
- Delete a student
- Data validation using Pydantic
- Interactive API documentation with Swagger UI

Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

Project Structure

EB-Student-CRUD/
├── main.py
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── .gitignore
└── students.db

Installation and Setup

1. Clone the Repository

git clone https://github.com/Chandani-gupta/EB-Student-CRUD.git
cd EB-Student-CRUD

2. Create a Virtual Environment

python -m venv .venv

3. Activate the Virtual Environment

Windows:

.venv\Scripts\Activate.ps1

4. Install Dependencies

pip install -r requirements.txt

5. Run the Application

uvicorn main:app --reload

6. Open API Documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

API Endpoints

Method| Endpoint| Description
GET| "/"| Check API status
POST| "/students/"| Create a student
GET| "/students/"| Get all students
GET| "/students/{student_id}"| Get a student by ID
PUT| "/students/{student_id}"| Update a student
DELETE| "/students/{student_id}"| Delete a student

Purpose

This project demonstrates CRUD operations, REST API development, request validation, and database integration using FastAPI and SQLite.

Author

Chandani Gupta
