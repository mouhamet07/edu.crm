from Data.db import students, teachers, courses


def get_total_students():
    return len(students)


def get_total_teachers():
    return len(teachers)


def get_total_courses():
    return len(courses)


def get_recent_courses():
    recent_courses = []
    for course in courses:
        teacher_name = next((t['name'] for t in teachers if t['id'] == course['teacher_id']), 'Inconnu')
        recent_courses.append({
            'id': course['id'],
            'title': course['title'],
            'teacher': teacher_name
        })
    return recent_courses