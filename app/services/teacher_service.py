from Data.db import teachers, courses
import re

def validate_email(email):
    """Valide que l'email se termine par @gmail.com"""
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

def add_teacher(name, email, speciality):
    if not validate_email(email):
        return None, "L'email doit être au format @gmail.com"
    
    teacher = {
        "id": len(teachers) + 1,
        "name": name,
        "email": email,
        "speciality": speciality
    }
    teachers.append(teacher)
    return teacher, None


def list_teachers():
    return teachers

def delete_teacher(teacher_id):
    for teacher in teachers:
        if teacher["id"] == teacher_id:
            teachers.remove(teacher)
            return True
    return False

def search_teachers(query):
    query = query.lower()
    return [teacher for teacher in teachers if query in teacher["name"].lower() or query in teacher["email"].lower()]

def update_teacher(teacher_id, name, email, speciality):
    if not validate_email(email):
        return False, "L'email doit être au format @gmail.com"
    
    for teacher in teachers:
        if teacher["id"] == teacher_id:
            teacher["name"] = name
            teacher["email"] = email
            teacher["speciality"] = speciality
            return True, None
    return False, "Enseignant non trouvé"

def filter_teachers_by_speciality(speciality):
    return [teacher for teacher in teachers if teacher["speciality"].lower() == speciality.lower()]

def get_teacher_courses(teacher_id):
    return [course for course in courses if course["teacher_id"] == teacher_id]

def count_teacher_courses(teacher_id):
    return len(get_teacher_courses(teacher_id))