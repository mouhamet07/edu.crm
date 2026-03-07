from flask import render_template, request, redirect, url_for
from . import courses_bp
from Data.db import courses, students, student_courses
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
    return render_template("courses/create.html")


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
        if student_id not in student_courses:
            student_courses[student_id] = []
        student_courses[student_id].append(course_id)
        return redirect(url_for("courses.index"))
    return render_template(
        "courses/assign.html",
        students=students,
        courses=courses
    )