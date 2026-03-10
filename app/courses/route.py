from flask import render_template, request, redirect, url_for, flash
from . import courses_bp
from app.services.course_service import (
    add_course,
    list_courses,
    delete_course,
    assign_student_to_course
)
from app.services.teacher_service import (list_teachers)
from app.services.student_service import (list_students)
from app.services.auth_service import login_required

@courses_bp.route("/courses")
@login_required
def index():
    courses = list_courses()
    return render_template(
        "courses/list.html",
        courses=courses
    )

@courses_bp.route("/courses/create", methods=["GET","POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        id =  request.form.get("id")
        r1= add_course(name, id)
        if r1 is None:
            flash(f"Le cours '{name}' existe déjà")
        else:
            flash(f"Le cours '{name}' a été ajouté avec succès")
        return redirect(url_for("courses.index"))
    teachers = list_teachers()
    return render_template("courses/create.html", teachers=teachers)


@courses_bp.route("/courses/delete/<int:id>")
@login_required
def delete_course(id):
    if delete_course(id):
        flash("Le cours a ete supprime avec succes")
    flash("Le cours n'a pas ete trouve")
    return redirect(url_for("courses.index"))


@courses_bp.route("/courses/assign", methods=["GET","POST"])
@login_required
def assign():
    if request.method == "POST":
        student_id = int(request.form.get("student"))
        course_id = int(request.form.get("course"))
        result = assign_student_to_course(course_id, student_id)
        if result == False:
            flash("Ce cours n'existe pas ou l'Étudiant y est déjà inscrit", "danger")
        else:
            flash(f"L'étudiant {student_id} a été ajouté au cours {course_id}", "success")
        return redirect(url_for("courses.index"))
    students=list_students()
    courses=list_courses()
    return render_template(
        "courses/assign.html",
        students=students,
        courses=courses
    )