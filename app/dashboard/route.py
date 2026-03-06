from flask import render_template, redirect, url_for, session
from app.dashboard import dashboard_bp
from Data.db import students, teachers, courses


@dashboard_bp.route("/dashboard")
def index():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    total_students = len(students)
    total_teachers = len(teachers)
    total_courses = len(courses)

    return render_template(
        "dashboard/dashboard.html",
        total_students=total_students,
        total_teachers=total_teachers,
        total_courses=total_courses
    )