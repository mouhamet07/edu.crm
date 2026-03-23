from flask import render_template, request, redirect, url_for,flash
from . import teachers_bp
from app.services.teacher_service import add_teacher, list_teachers, delete_teacher
from app.services.auth_service import login_required, admin_required


@teachers_bp.route("/teachers")
@login_required
def index():
    teachers = list_teachers()
    return render_template("teachers/list.html", teachers=teachers)


@teachers_bp.route("/teachers/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        speciality = request.form.get("speciality")
        add_teacher(name, email, speciality)
        return redirect(url_for("teachers.index"))
    return render_template("teachers/create.html")


@teachers_bp.route("/teachers/delete/<int:id>")
@login_required
@admin_required
def delete_teacher(id):
    if delete_teacher(id):
        flash("Enseignant supprimé", "success")
    else:
        flash("Enseignant non supprimé", "warning")
    return redirect(url_for("teachers.index"))