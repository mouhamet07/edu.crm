from Data.db import courses

def add_course(title, teacher_id):
    course_id = len(courses) + 1

    course = {
        "id": course_id,
        "title": title,
        "teacher_id": teacher_id,
        "student_ids": []
    }

    courses.append(course)
    return course


def list_courses():
    return courses


def assign_student_to_course(course_id, student_id):
    for course in courses:
        if course["id"] == course_id:
            if student_id not in course["student_ids"]:
                course["student_ids"].append(student_id)
            return course

    return None


def delete_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return