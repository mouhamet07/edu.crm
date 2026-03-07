from flask import render_template, request, redirect, url_for, flash
from . import students_bp

from app.services.student_service import (
    list_students,
    add_student,
    delete_student as delete_student_service
)


@students_bp.route("/students")
def index():

    students = list_students()

    return render_template(
        "students/list.html",
        students=students
    )


@students_bp.route("/students/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")

        result = add_student(name, email)

        if result is None:
            flash("Cet email existe déjà", "danger")
        else:
            flash("Étudiant ajouté avec succès", "success")

        return redirect(url_for("students.index"))

    return render_template("students/create.html")


@students_bp.route("/students/delete/<int:id>")
def delete_student(id):

    student_id = id + 1

    result = delete_student_service(student_id)

    if result:
        flash("Étudiant supprimé avec succès", "success")
    else:
        flash("Étudiant introuvable", "danger")

    return redirect(url_for("students.index"))