from flask import render_template, request, redirect, url_for
from . import courses_bp
from Data.db import courses, students, student_courses


@courses_bp.route("/courses")
def index():

    return render_template(
        "courses/list.html",
        courses=courses
    )


@courses_bp.route("/courses/create", methods=["GET","POST"])
def create():

    if request.method == "POST":

        name = request.form.get("name")

        courses.append({
            "name": name
        })

        return redirect(url_for("courses.index"))

    return render_template("courses/create.html")


@courses_bp.route("/courses/delete/<int:id>")
def delete_course(id):

    if id < len(courses):
        courses.pop(id)

    return redirect(url_for("courses.index"))


@courses_bp.route("/courses/assign", methods=["GET","POST"])
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