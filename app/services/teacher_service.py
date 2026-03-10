from Data.db import teachers

def add_teacher(name, email, speciality):
    teacher = {
        "id": len(teachers) + 1,
        "name": name,
        "email": email,
        "speciality": speciality
    }
    teachers.append(teacher)
    return teacher


def list_teachers():
    return teachers


def delete_student(teacher_id):
    for teacher in teachers:
        if teacher["id"] == teacher_id:
            teachers.remove(teacher)
            return True
    return False