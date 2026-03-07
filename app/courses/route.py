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
    r1= add_course("Math", 1)
    if r1 is None:
        return "Le cours 'Math' existe déjà"
    else:
        return f"Le cours '{r1['title']}' a été ajouté avec succès"

@courses_bp.route("/")
@login_required
def index():
    courses = list_courses()
    return str(courses)

@courses_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    if delete_course(id):
        return "Le cours a ete supprime avec succes"
    return "Le cours n'a pas ete trouve"


@courses_bp.route("/assign/<int:course_id>/<int:student_id>")
@login_required
def assign(course_id, student_id):
    result = assign_student_to_course(course_id, student_id)
    if result == False:
        return "Ce cours n'existe pas ou l'Étudiant y est déjà inscrit"
    return f"L'étudiant {student_id} a été ajouté au cours {course_id}"