from Data.db import students, courses
import re


def validate_email(email):
    """Valide que l'email se termine par @gmail.com"""
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

def list_students():
    for student in students:
        student.setdefault("photo", "https://via.placeholder.com/50")
        student.setdefault("status", "actif")
    return students


def add_student(name, email, photo):
    if not validate_email(email):
        return "invalid_email"
    for student in students:
        if student["email"].lower() == email.lower():
            return None
    student_id = max([s["id"] for s in students], default=0) + 1
    student = {
        "id": student_id,
        "name": name,
        "email": email,
        "status": "actif",
        "photo": photo if photo else f"https://ui-avatars.com/api/?name={name}"
    }
    students.append(student)
    return student

def delete_student(student_id):
    for student in students:
        if student.get("id") == student_id:
            students.remove(student)
            return True
    return False


def get_student_by_id(student_id):

    for student in students:
        if student.get("id") == student_id:
            return student
    return None


def search_students(query):
    return [
        s for s in students
        if query.lower() in s["name"].lower()
    ]


def paginate_students(page, per_page=3):

    start = (page - 1) * per_page
    end = start + per_page

    return students[start:end]


def update_student(student_id, name, email):

    for student in students:
        if student.get("id") == student_id:
            student["name"] = name
            student["email"] = email
            return True

    return False


def toggle_student_status(student_id):

    for student in students:

        if student.get("id") == student_id:

            if student.get("status", "actif") == "actif":
                student["status"] = "inactif"
            else:
                student["status"] = "actif"

            return True

    return False


def get_student_courses(student_id):

    result = []

    for course in courses:
        if student_id in course.get("student_ids", []):
            result.append(course)

    return result