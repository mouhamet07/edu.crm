from Data.db import students, teachers, courses


def get_total_students():
    return len(students)


def get_total_teachers():
    return len(teachers)


def get_total_courses():
    return len(courses)


def get_recent_courses():
    recent_courses = []
    for i, course in enumerate(courses):
        teacher = teachers[i % len(teachers)]
        recent_courses.append({
            "id": i + 1,
            "title": course,
            "teacher": teacher
        })
    return recent_courses