from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.teacher_service import add_teacher, list_teachers, delete_teacher

teachers_bp = Blueprint("teachers", __name__, url_prefix="/teachers")


@teachers_bp.route("/")
def teachers_list():
    teachers = list_teachers()
    return render_template("teachers/list.html", teachers=teachers)


@teachers_bp.route("/create", methods=["GET", "POST"])
def create_teacher():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        speciality = request.form["speciality"]
        add_teacher(name, email, speciality)
        return redirect(url_for("teachers.teachers_list"))
    return render_template("teachers/create.html")


@teachers_bp.route("/delete/<int:id>")
def delete_teacher_route(id):
    if delete_teacher(id):
        flash("Enseignant supprimé", "success")
    else:
        flash("Enseignant non supprimé", "warning")
    return redirect(url_for("teachers.teachers_list"))