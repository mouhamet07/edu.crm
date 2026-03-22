from Data.db import courses,teachers
from app.services.student_service import get_student_by_id


def add_course(title, teacher_id):

    for course in courses:
        if course["title"].lower() == title.lower():
            return None
    max_id = 0
    for course in courses:
        if course["id"] > max_id:
            max_id = course["id"]
    course_id = max_id + 1

    if teacher_id:
        teacher_id = int(teacher_id)
    else:
        teacher_id = None

    course = {
        "id": course_id,
        "title": title,
        "teacher_id": teacher_id,
        "student_ids": []
    }
    courses.append(course)
    return course

def list_courses():
    result = []
    for course in courses:
        if not course["teacher_id"]:
            teacher = "Non assigné"
        else:
            teacher = teachers[int(course["teacher_id"]) - 1]["name"]

        students = []
        for student_id in course["student_ids"]:
            student = get_student_by_id(student_id)
            if student:
                students.append(student["name"])

        result.append({
            "id": course["id"],
            "title": course["title"],
            "teacher": teacher,
            "students": students
        })
    return result


def assign_student_to_course(course_id, student_id):
    student = get_student_by_id(student_id)
    if not student:
        return False
    for course in courses:
        if course["id"] == course_id:
            if student_id not in course["student_ids"]:
                course["student_ids"].append(student_id)
            return True
    return False

def delete_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return True
    return False

def assign_teacher_to_course(course_id, teacher_id):
    for course in courses:
        if course["id"] == course_id:
            course["teacher_id"] = int(teacher_id)
            return True
    return False

def search_courses(mot):
    all_courses = list_courses()
    result = []

    for course in all_courses:
        if mot.lower() in course["title"].lower():
            result.append(course)

    return result

def update_course(course_id, title, teacher_id):
    for course in courses:
        if course["id"] == course_id:
            course["title"] = title
            course["teacher_id"] = teacher_id if teacher_id else None
            return True
    return False

def remove_student_from_course(course_id, student_id):
    for course in courses:
        if course["id"] == course_id:
            if student_id in course["student_ids"]:
                course["student_ids"].remove(student_id)
                return True
    return False

def get_course_by_id(course_id):
    for course in courses:
        if course["id"] == course_id:
            return course
    return None