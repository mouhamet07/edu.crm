from flask import render_template, request, redirect, url_for, flash
from . import students_bp
from app.services.student_service import get_student_courses
from app.services.auth_service import login_required, admin_required
from app.services.student_service import validate_email, list_students
from app.services.student_service import (
    list_students,
    add_student,
    delete_student as delete_student_service,
    search_students,
    paginate_students,
    update_student,
    get_student_by_id,
    toggle_student_status
)

@students_bp.route("/students")
@login_required
def index():

    query = request.args.get("q")
    page = int(request.args.get("page", 1))
    per_page = 3

    if query:
        students = search_students(query)
        total_pages = 1 
    else:
        all_students = list_students()
        total = len(all_students)

        students = paginate_students(page, per_page)

        total_pages = (total + per_page - 1) // per_page

    return render_template(
        "students/list.html",
        students=students,
        page=page,
        total_pages=total_pages
    )

@students_bp.route("/students/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        photo = request.form.get("photo")
        result = add_student(name, email, photo)
        if result == "invalid_email":
            flash("Email invalide (doit être @gmail.com)", "danger")
        elif result is None:
            flash("Cet email existe déjà", "danger")
        else:
            flash("Étudiant ajouté avec succès", "success")
            return redirect(url_for("students.index"))
    return render_template("students/create.html")

@students_bp.route("/students/delete/<int:id>")
@admin_required
@login_required
def delete_student(id):

    result = delete_student_service(id)

    if result:
        flash("Étudiant supprimé avec succès", "success")
    else:
        flash("Étudiant introuvable", "danger")

    return redirect(url_for("students.index"))

@students_bp.route("/students/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    student = get_student_by_id(id)
    if not student:
        flash("Étudiant introuvable", "danger")
        return redirect(url_for("students.index"))
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if not validate_email(email):
            flash("Email invalide (doit être @gmail.com)", "danger")
            return redirect(url_for("students.update", id=id))
        for s in list_students():
            if s["email"].lower() == email.lower() and s["id"] != id:
                flash("Cet email est déjà utilisé", "danger")
                return redirect(url_for("students.update", id=id))
        update_student(id, name, email)
        flash("Étudiant modifié", "success")
        return redirect(url_for("students.index"))
    return render_template("students/update.html", student=student)

@students_bp.route("/students/toggle-status/<int:id>")
@login_required
def toggle_status(id):

    toggle_student_status(id)

    flash("Statut mis à jour", "success")

    return redirect(url_for("students.index"))


@students_bp.route("/students/<int:id>/courses")
@login_required
def student_courses_view(id):

    student = get_student_by_id(id)

    if not student:
        flash("Étudiant introuvable", "danger")
        return redirect(url_for("students.index"))

    courses = get_student_courses(id)

    return render_template(
        "students/courses.html",
        student=student,
        courses=courses
    )