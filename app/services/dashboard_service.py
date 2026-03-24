from Data.db import students, teachers, courses


def get_total_students():
    return len(students)


def get_total_teachers():
    return len(teachers)


def get_total_courses():
    return len(courses)


def get_recent_students(limit=3):
    sorted_students = sorted(students, key=lambda x: x["id"], reverse=True)
    return sorted_students[:limit]


def get_top_course():
    if not courses:
        return None, 0

    top = None
    max_count = 0

    for course in courses:
        count = len(course.get("student_ids", []))
        if count > max_count:
            max_count = count
            top = course

    return top, max_count


def get_top_teacher():
    if not teachers:
        return None, 0

    teacher_count = {}

    for course in courses:
        t_id = course.get("teacher_id")
        if t_id:
            teacher_count[t_id] = teacher_count.get(t_id, 0) + 1

    if not teacher_count:
        return None, 0

    top_id = max(teacher_count, key=teacher_count.get)
    top_teacher = next((t for t in teachers if t["id"] == top_id), None)

    return top_teacher, teacher_count[top_id]