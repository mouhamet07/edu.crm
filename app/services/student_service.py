from Data.db import students


def list_students():
    return students


def add_student(name, email):
    for student in students:
        if student["email"].lower() == email.lower():
            return None
    student_id = len(students) + 1
    student = {
        "id": student_id,
        "name": name,
        "email": email
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
        if student["id"] == student_id:
            return student
    return None