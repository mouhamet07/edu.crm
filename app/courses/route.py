from flask import render_template, request, redirect, url_for, flash
from . import courses_bp
from Data.db import courses, students
from app.services.course_service import (
    add_course,
    list_courses,
    delete_course,
    assign_student_to_course
)
from app.services.auth_service import login_required


@courses_bp.route("/courses")
@login_required
def index():
    return render_template(
        "courses/list.html",
        courses=list_courses()
    )


@courses_bp.route("/courses/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        teacher_id = request.form.get("teacher")

        resultat = add_course(name, teacher_id)

        if resultat is None:
            flash(f"Le cours '{name}' existe déjà")
        else:
            flash(f"Le cours '{name}' a été ajouté avec succès")

        return redirect(url_for("courses.index"))

    return render_template("courses/create.html")


@courses_bp.route("/courses/delete/<int:id>")
@login_required
def delete(id):
    resultat = delete_course(id)

    if resultat:
        flash("Le cours a été supprimé avec succès")
    else:
        flash("Le cours n'a pas été trouvé")

    return redirect(url_for("courses.index"))


@courses_bp.route("/courses/assign", methods=["GET", "POST"])
@login_required
def assign():
    if request.method == "POST":
        student_id = int(request.form.get("student"))
        course_id = int(request.form.get("course"))

        resultat = assign_student_to_course(course_id, student_id)

        if resultat:
            flash("L'étudiant a été assigné au cours")
        else:
            flash("Impossible d'assigner l'étudiant")

        return redirect(url_for("courses.index"))

    return render_template(
        "courses/assign.html",
        students=students,
        courses=courses
    )