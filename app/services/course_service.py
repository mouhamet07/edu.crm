from Data.db import courses,teachers
from app.services.student_service import get_student_by_id


def add_course(title, teacher_id):
    for course in courses:
        if course["title"].lower() == title.lower():
            return None
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
    result = []
    for course in courses:
        if course["teacher_id"] is None:
            teacher_name = "Non assigné"
        else:
            teacher_name = teachers[course["teacher_id"] - 1]
        result.append({
            "id": course["id"],
            "title": course["title"],
            "teacher": teacher_name,
           
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