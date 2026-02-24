teachers = []

def add_teacher(name, email, speciality):
    teacher = {
        'id': len(teachers) + 1,
        'name': name,
        'email': email,
        'speciality': speciality
    }
    teachers.append(teacher)


def list_teachers():
    return teachers


def delete_teacher(id):
    global teachers
    teachers = [t for t in teachers if t['id'] != id]
