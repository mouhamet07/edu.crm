from flask import Blueprint
from app.services.course_service import (
    add_course,
    list_courses,
    delete_course,
    assign_student_to_course
)
from app.services.auth_service import login_required

courses_bp = Blueprint("courses", __name__, url_prefix="/courses")


@courses_bp.route("/test")
def test():
    return "Module COURSES fonctionne "

@courses_bp.route("/add")
@login_required
def add():
    add_course("Math", 1)
    return "Cours ajouté "

@courses_bp.route("/")
@login_required
def index():
    courses = list_courses()
    return str(courses)

@courses_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    delete_course(id)
    return f"Cours {id} supprimé "

@courses_bp.route("/assign/<int:course_id>/<int:student_id>")
@login_required
def assign(course_id, student_id):
    assign_student_to_course(course_id, student_id)
    return f"Étudiant {student_id} assigné au cours {course_id} "