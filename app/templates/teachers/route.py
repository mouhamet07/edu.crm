from flask import render_template, request, redirect, url_for
from . import teachers_bp
from Data.db import teachers


@teachers_bp.route("/teachers")
def index():
    return render_template(
        "teachers/list.html",
        teachers=teachers
    )


@teachers_bp.route("/teachers/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        speciality = request.form.get("speciality")

        teachers.append({
            "name": name,
            "email": email,
            "speciality": speciality
        })

        return redirect(url_for("teachers.index"))

    return render_template("teachers/create.html")


@teachers_bp.route("/teachers/delete/<int:id>")
def delete_teacher(id):

    if id < len(teachers):
        teachers.pop(id)

    return redirect(url_for("teachers.index"))