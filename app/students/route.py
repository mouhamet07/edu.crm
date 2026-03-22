from flask import render_template, request, redirect, url_for, flash
from . import students_bp
from app.services.auth_service import login_required
from app.services.student_service import (
    list_students,
    add_student,
    delete_student as remove_student,
    get_student_by_id
)

PER_PAGE = 8


@students_bp.route("/students")
@login_required
def index():
    students = list_students()

    # Recherche
    query = request.args.get("q", "").strip().lower()
    if query:
        students = [
            s for s in students
            if query in s["name"].lower() or query in s["email"].lower()
        ]

    # Filtre statut
    status = request.args.get("status", "")
    if status == "actif":
        students = [s for s in students if s["active"]]
    elif status == "inactif":
        students = [s for s in students if not s["active"]]

    # Pagination
    page = request.args.get("page", 1, type=int)
    total = len(students)
    total_pages = max(1, -(-total // PER_PAGE))
    page = max(1, min(page, total_pages))

    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    students_page = students[start:end]

    return render_template(
        "students/list.html",
        students=students_page,
        query=query,
        status=status,
        page=page,
        total_pages=total_pages,
        total=total,
        per_page=PER_PAGE
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
            flash("Email déjà utilisé", "danger")

        return redirect(url_for("students.index"))

    return render_template("students/create.html")


@students_bp.route("/students/delete/<int:id>")
@login_required
def delete_student(id):
    if remove_student(id):
        flash("Étudiant supprimé", "success")
    else:
        flash("Étudiant non supprimé", "warning")
    return redirect(url_for("students.index"))


@students_bp.route("/students/detail/<int:id>")
@login_required
def detail(id):
    student = get_student_by_id(id)

    if not student:
        flash("Étudiant introuvable", "danger")
        return redirect(url_for("students.index"))

    return render_template("students/detail.html", student=student)


@students_bp.route("/students/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    student = get_student_by_id(id)

    if not student:
        flash("Étudiant introuvable", "danger")
        return redirect(url_for("students.index"))

    if request.method == "POST":
        student["name"] = request.form.get("name")
        student["email"] = request.form.get("email")
        flash("Étudiant modifié avec succès", "success")
        return redirect(url_for("students.index"))

    return render_template("students/edit.html", student=student)