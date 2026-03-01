from flask import Blueprint, render_template, request, redirect, url_for, flash
from application.services.student_service import (
    list_students,
    add_student,
    delete_student
)

students_bp = Blueprint(
    "students",
    __name__,
    url_prefix="/students"
)


@students_bp.route("/")
def students_list():
    students = list_students()
    return "Liste des etudiants"
    # return render_template("students/list.html", students=students)


@students_bp.route("/create", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        add_student(name, email)
        flash("Étudiant ajouté avec succès", "success")
        return redirect(url_for("students.students_list"))
    
    return "Ajouter avec succes"

    # return render_template("students/create.html")


@students_bp.route("/delete/<int:id>")
def delete_student_route(id):
    delete_student(id)
    flash("Étudiant supprimé", "warning")
    return redirect(url_for("students.students_list"))