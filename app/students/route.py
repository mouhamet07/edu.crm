from flask import render_template, request, redirect, url_for
from . import students_bp
from Data.db import students


@students_bp.route("/students")
def index():
    return render_template(
        "students/list.html",
        students=students
    )


@students_bp.route("/students/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")

        students.append({
            "name": name,
            "email": email
        })

        return redirect(url_for("students.index"))

    return render_template("students/create.html")


@students_bp.route("/students/delete/<int:id>")
def delete_student(id):

    if id < len(students):
        students.pop(id)

    return redirect(url_for("students.index"))