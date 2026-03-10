from flask import render_template, request, redirect, url_for, flash
from . import students_bp
from app.services.auth_service import login_required
from app.services.student_service import (
    list_students,
    add_student,
    delete_student
)

@students_bp.route("/students")
@login_required
def index():
    students = list_students()
    return render_template(
        "students/list.html",
        students=students
    )


@students_bp.route("/students/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if add_student(name, email):
            flash("Étudiant ajouté avec succès", "success")
        else:
            flash("Erreur lors de l'ajout", "danger")
        return redirect(url_for("students.index"))
    return render_template("students/create.html")


@students_bp.route("/students/delete/<int:id>")
@login_required
def delete_student(id):
    if delete_student(id):
        flash("Étudiant supprimé", "success")
    else:
        flash("Étudiant non supprimé", "warning")
    return redirect(url_for("students.students_list"))