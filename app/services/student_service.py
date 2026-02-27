students = []
current_id = 1


def list_students():
    return students


def add_student(name, email):
    global current_id

    student = {
        "id": current_id,
        "name": name,
        "email": email
    }

    students.append(student)
    current_id += 1
    return student


def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]


def get_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None