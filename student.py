import re
import json

STUDENT_DB = 'data/students.json'
COURSES = ['B.Tech', 'BCA', 'MCA', 'MBA']

def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(-?[a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$', email)


def register_student():
    print("\n--- Student Registration ---")

    name = input("Name: ").strip()
    if not re.match(r'^[A-Za-z ]{2,}$', name):
        print("Invalid name.")
        return

    regno = input("Registration Number (REG-YYYY-NNNN): ").strip()
    if not re.match(r'^REG-\d{4}-\d{4}$', regno):
        print("Invalid registration number format.")
        return

    age = int(input("Age: ").strip())
    if not (18 <= age <= 25):
        print("Age must be between 18 and 25.")
        return

    email = input("Email: ").strip()
    if not is_valid_email(email):
        print("Invalid email.")
        return

    phone = input("Phone (10 digits): ").strip()
    if not re.match(r'^\d{10}$', phone):
        print("Invalid phone number.")
        return

    print("Available Courses:", ", ".join(COURSES))
    course = input("Course: ").strip()
    if course not in COURSES:
        print("Invalid course selection.")
        return

    student = {
        "name": name,
        "registration_number": regno,
        "age": age,
        "email": email,
        "phone": phone,
        "course": course
    }

    try:
        with open(STUDENT_DB, 'r') as f:
            students = json.load(f)
    except:
        students = []

    students.append(student)
    with open(STUDENT_DB, 'w') as f:
        json.dump(students, f, indent=4)

    print("Student registered successfully!")

def list_students():
    try:
        with open(STUDENT_DB, 'r') as f:
            students = json.load(f)
    except:
        print("No student records found.")
        return

    print("\n--- Student List ---")
    for idx, s in enumerate(students, 1):
        print(f"{idx}. {s['name']} | {s['registration_number']} | {s['email']} | {s['course']}")
